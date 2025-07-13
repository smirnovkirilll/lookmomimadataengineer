#!/bin/env python
# note: given export CSV file https://support.mozilla.org/en-US/kb/exporting-your-pocket-list
#   enrich those entries with additional info (locally) and store result to s3 and postgresql DB


import logging
import os
import threading
from bs4.builder import ParserRejectedMarkup
from requests import Session
from requests.exceptions import ConnectionError, MissingSchema
from urllib3.exceptions import MaxRetryError, NewConnectionError, NameResolutionError

from loader.common.helpers import (
    get_domain_by_url,
    get_title_by_url,
    get_unshorten_url,
    make_clean_url,
    _requests_session,
    _timestamp_to_dttm,
)
from loader.common.table_transfer import TableTransfer


logger = logging.getLogger('logging pocket_export')
logger.setLevel(logging.INFO)


ExceptionTuple = (
    ConnectionError,
    MissingSchema,
    MaxRetryError,
    NewConnectionError,
    NameResolutionError,
    ParserRejectedMarkup,
    UnicodeDecodeError,
)


def enrich_row(
        row: dict[str: str],
        rename_only: bool = True,
        session: Session = None,
) -> dict[str: str]:
    """enrich pocket entry dict if it does not contain new not-empty keys yet"""

    logger.info(f'Start processing {row=}')

    def _get_unshorten_url(_url, _session):
        try:
            return get_unshorten_url(_url, _session), False
        except ExceptionTuple:
            return _url, True

    def _get_title_by_url(_url, _session, _original_title):
        try:
            return get_title_by_url(_url, _session), False
        except ExceptionTuple:
            return _original_title, True

    if rename_only:
        if row.get('processing_status') in ('RENAMED', 'PROCESSED'):
            enriched_row = row
        else:
            enriched_row = {
                'original_url': row['url'],
                'original_title': row['title'],
                'time_added': row['time_added'],
                'tags': row['tags'],
                'status': row['status'],
                'processing_status': 'RENAMED',
                'clean_url': '',
                'unshorten_url': '',
                'domain_url': '',
                'clean_title': '',
                'utc_added_dttm': '',
                'errors': False,
            }
    else:
        if row.get('processing_status') == 'PROCESSED':
            enriched_row = row
        elif row.get('processing_status') == 'RENAMED':
            clean_url = make_clean_url(row['original_url'])
            unshorten_url, error_uu = _get_unshorten_url(clean_url, session)
            clean_title, error_ct = _get_title_by_url(unshorten_url, session, row['original_title'])
            errors = error_uu or error_ct

            enriched_row = {
                'original_url': row['original_url'],
                'original_title': row['original_title'],
                'time_added': row['time_added'],
                'tags': row['tags'],
                'status': row['status'],

                'clean_url': clean_url,
                'unshorten_url': unshorten_url,
                'domain_url': get_domain_by_url(unshorten_url),
                'clean_title': clean_title,
                'utc_added_dttm': _timestamp_to_dttm(int(row['time_added'])),

                'processing_status': 'PROCESSED',
                'errors': errors,
            }
        else:
            clean_url = make_clean_url(row['url'])
            unshorten_url, error_uu = _get_unshorten_url(clean_url, session)
            clean_title, error_ct = _get_title_by_url(unshorten_url, session, row['title'])
            errors = error_uu or error_ct

            enriched_row = {
                'original_url': row['url'],
                'original_title': row['title'],
                'time_added': row['time_added'],
                'tags': row['tags'],
                'status': row['status'],

                'clean_url': clean_url,
                'unshorten_url': unshorten_url,
                'domain_url': get_domain_by_url(unshorten_url),
                'clean_title': clean_title,
                'utc_added_dttm': _timestamp_to_dttm(int(row['time_added'])),

                'processing_status': 'PROCESSED',
                'errors': errors,
            }

    # if threading in use https://stackoverflow.com/a/78112476
    threading.current_thread().return_value = enriched_row
    logger.info(f'Finished processing {enriched_row=}')

    return enriched_row


def enrich_group_of_rows(
        list_of_rows: list[dict[str: str]],
        rename_only: bool = True,
) -> list[dict[str: str]]:

    threads = []
    enriched_rows = []
    session = _requests_session()

    for row in list_of_rows:
        t = threading.Thread(
            target=enrich_row,
            args=(row,),
            kwargs={"rename_only": rename_only, "session": session},
        )
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
        enriched_rows.append(t.return_value)

    return enriched_rows


def enrich_chunk_of_pocket_export_rows(source_file_name, min_index=0, chunk_size=100):
    """enrich inplace by chunks of given size"""

    max_index = min_index + chunk_size
    pocket = TableTransfer(
        source_file_name=source_file_name,
        target_file_name=source_file_name,
    )
    pocket.get_entries_from_csv()

    if min_index > 0:
        min_unchanged_part = pocket.list_of_dicts_entries[0: min_index]
    else:
        min_unchanged_part = []

    if max_index >= len(pocket.list_of_dicts_entries):
        max_unchanged_part = []
    else:
        max_unchanged_part = pocket.list_of_dicts_entries[max_index:]

    changed_part = enrich_group_of_rows(
        pocket.list_of_dicts_entries[min_index:max_index], rename_only=False)
    pocket.list_of_dicts_entries = min_unchanged_part + changed_part + max_unchanged_part
    pocket.upload_entries_to_csv()


def enrich_pocket_export(source_file_name, target_file_name, target_s3_bucket, target_s3_file_name):
    """to be used locally"""

    # 1. rename columns and save to target file
    pocket = TableTransfer(
        source_file_name=os.environ['LOCAL_POCKET_EXPORT_SOURCE_FILE_NAME_CSV'],
        target_file_name=os.environ['LOCAL_POCKET_EXPORT_TARGET_FILE_NAME_CSV'],
    )
    pocket.get_entries_from_csv()
    pocket.list_of_dicts_entries = enrich_group_of_rows(
        pocket.list_of_dicts_entries, rename_only=True)
    pocket.upload_entries_to_csv()

    # 2. enrich by chunks (intentionally using the same file for source and target)
    chunk_size = 500
    min_index_list = [0 + chunk_size * i for i in range(8)]
    for min_index in min_index_list:
        logger.info(f'Start processing {min_index=}')
        enrich_chunk_of_pocket_export_rows(
            source_file_name=os.environ['LOCAL_POCKET_EXPORT_TARGET_FILE_NAME_CSV'],
            min_index=min_index,
            chunk_size=chunk_size,
        )

    # 3. upload to s3 as csv
    pocket = TableTransfer(
        source_file_name=os.environ['LOCAL_POCKET_EXPORT_TARGET_FILE_NAME_CSV'],
        target_s3_bucket=os.environ['S3_BUCKET_PRIVATE_DATA_PROCESSING'],
        target_file_name=os.environ['S3_POCKET_EXPORT_TARGET_FILE_NAME_CSV'],
    )
    pocket.get_entries_from_csv()
    pocket.upload_entries_to_csv()


if __name__ == '__main__':
    # note: initial script, once time usage
    logging.basicConfig(level=logging.INFO)

    # TODO:
    #   enrich_pocket_export()  FINISHED, but parametrize
    #   enrich_pocket_export_old() (locally, additional renaming to be made at first)
    #   upload_pocket_export_to_postgresql() (cloud)
    #   upload_pocket_export_old_to_postgresql() (cloud)
