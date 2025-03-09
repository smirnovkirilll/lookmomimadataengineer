#!/bin/env python
# note: 3 source and target types required: csv <--> json <--> postgresql <--> csv
#   entries can be stored locally, s3, postgresql
#   lets implement generic transfer to move entries in any direction
import os
import logging
import typing as tp
from enum import Enum
from loader.common.helpers import (
    get_postgresql_connection,
    get_s3_client,
    download_object_from_s3,
    read_local_file,
    read_temp_file,
    upload_object_to_s3,
    execute_postgresql_query,
)


logger = logging.getLogger('logging table_transfer')
logger.setLevel(logging.INFO)


class TransformType(Enum):
    INSERT = 'insert'
    UPSERT = 'upsert'
    TRUNCATE_INSERT = 'truncate_insert'


class TableTransfer:
    """Represents data as table and helps to transfer data from one system to another"""
    def __init__(
            self,
            source_s3_bucket=None,
            source_s3_file_name=None,
            target_s3_bucket=None,
            target_s3_file_name=None,
            source_pg_schema=None,
            source_pg_table=None,
            target_pg_schema=None,
            target_pg_table=None,
    ):
        self.columns = None
        self.flat_entries = None
        self.list_of_dicts_entries = None
        self.source_s3_bucket = source_s3_bucket
        self.source_s3_file_name = source_s3_file_name
        self.target_s3_bucket = target_s3_bucket
        self.target_s3_file_name = target_s3_file_name
        self.source_pg_schema = source_pg_schema
        self.source_pg_table = source_pg_table
        self.target_pg_schema = target_pg_schema
        self.target_pg_table = target_pg_table
        self.postgresql_connection = get_postgresql_connection()
        self.s3_client = get_s3_client()

    def get_entries_from_csv(self, bucket=None, file_name=None):
        """gets entries from s3 or from local file system if no bucket provided"""

        if bucket:
            self.source_s3_bucket = bucket

        if file_name:
            self.source_s3_file_name = file_name
        if not self.source_s3_file_name:
            raise Exception(f'No source_s3_file_name provided, cant proceed')

        if self.source_s3_bucket:
            temp_file = download_object_from_s3(self.source_s3_bucket, self.source_s3_file_name)
            content = read_temp_file(temp_file)
        else:
            content = read_local_file(self.source_s3_file_name)

        content = content.split('\n')
        columns = content[0]
        entries = content[1:]
        self.columns = [column.strip().strip('\"').strip() for column in columns.split(',')]
        logger.info(f'Got columns from CSV: columns={self.columns}')

        self.flat_entries = [
            [value.strip().strip('\"').strip() for value in entry.split(',')]
                for entry in entries if entry
        ]
        logger.info(f'Got flat entries from CSV: flat_entries={self.flat_entries}')

        self.list_of_dicts_entries = []
        for entry in self.flat_entries:
            self.list_of_dicts_entries.append(dict(zip(self.columns, entry)))
        logger.info(f'Got entries as dicts from CSV: list_of_dicts_entries={self.list_of_dicts_entries}')

    def get_entries_from_json(self, bucket=None, file_name=None):
        """gets entries from s3 or from local file system if no bucket provided"""
        # TODO: in progress
        pass

    def get_entries_from_pg(self):
        pass

    def _check_entries(self):
        if not self.list_of_dicts_entries:
            raise Exception('Get entries at first, cant proceed')

    def upload_entries_to_csv(self):
        """warning: TransformType.TRUNCATE_INSERT only"""
        self._check_entries()

    def upload_entries_to_json(self):
        """warning: TransformType.TRUNCATE_INSERT only"""
        self._check_entries()

    def upload_entries_to_pg(self, transform_type: TransformType):
        """insert/upsert/truncate+insert"""

        self._check_entries()
        if not self.postgresql_connection:
            raise Exception('No postgresql_connection provided, cant proceed')


if __name__ == '__main__':
    # note: debug only
    logging.basicConfig(level=logging.INFO)
    curated_list = TableTransfer(
        # source_s3_file_name=os.environ['LOCAL_FILE_NAME_CSV_TEST'],
        source_s3_file_name=os.environ['S3_FILE_NAME_CSV_TEST'],
        source_s3_bucket=os.environ['S3_BUCKET_CSV_TEST'],
    )
    curated_list.get_entries_from_csv()
