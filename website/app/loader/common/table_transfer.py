#!/bin/env python
# note: 3 source and target types required: csv <--> json <--> postgresql <--> csv
#   entries can be stored locally, s3, postgresql
#   lets implement generic transfer to move entries in any direction

import json
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
    csv_file_content_to_dict,
    write_object_to_local_file,
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
            source_file_name=None,
            target_s3_bucket=None,
            target_file_name=None,
            source_pg_schema=None,
            source_pg_table=None,
            target_pg_schema=None,
            target_pg_table=None,
    ):
        self.columns = None
        self.list_of_dicts_entries = None
        self.source_s3_bucket = source_s3_bucket
        self.source_file_name = source_file_name
        self.target_s3_bucket = target_s3_bucket
        self.target_file_name = target_file_name
        self.source_pg_schema = source_pg_schema
        self.source_pg_table = source_pg_table
        self.target_pg_schema = target_pg_schema
        self.target_pg_table = target_pg_table
        self.postgresql_connection = get_postgresql_connection()
        self.s3_client = get_s3_client()

    def _check_entries(self):
        """all upload methods should work only if entries has already been prepared"""
        if not self.list_of_dicts_entries:
            raise Exception('Get entries at first, cant proceed')

    def get_entries_from_csv(self, bucket=None, file_name=None):
        """gets entries from s3 or from local file system if no bucket provided"""

        if bucket:
            self.source_s3_bucket = bucket

        if file_name:
            self.source_file_name = file_name
        if not self.source_file_name:
            raise Exception(f'No source_file_name provided, cant proceed')

        if self.source_s3_bucket:
            temp_file = download_object_from_s3(self.source_s3_bucket, self.source_file_name)
            content = read_temp_file(temp_file)
        else:
            content = read_local_file(self.source_file_name)

        self.list_of_dicts_entries = csv_file_content_to_dict(content)
        logger.info(f'Got entries as dicts from CSV: {self.list_of_dicts_entries=}')

    @property
    def list_of_dicts_entries_b(self):
        """list_of_dicts_entries as bytes"""
        self._check_entries()
        return json.dumps(self.list_of_dicts_entries, indent=2).encode('utf-8')

    def get_entries_from_json(self, bucket=None, file_name=None):
        """gets entries from s3 or from local file system if no bucket provided"""
        # TODO
        pass

    def get_entries_from_pg(self):
        # TODO
        pass

    def upload_entries_to_csv(self):
        # TODO
        """warning: TransformType.TRUNCATE_INSERT only"""
        self._check_entries()

    def upload_entries_to_json(self, bucket=None, file_name=None):
        """warning: TransformType.TRUNCATE_INSERT only"""
        self._check_entries()

        if bucket:
            self.target_s3_bucket = bucket

        if file_name:
            self.target_file_name = file_name
        if not self.target_file_name:
            raise Exception(f'No target_file_name provided, cant proceed')

        if self.target_s3_bucket:
            upload_object_to_s3(self.target_s3_bucket, self.target_file_name, self.list_of_dicts_entries_b)
            logger.info(f'Uploaded entries as json to s3: {self.target_s3_bucket=}, {self.target_file_name=}')
        else:
            write_object_to_local_file(self.target_file_name, self.list_of_dicts_entries_b)
            logger.info(f'Saved entries as json locally: {self.target_file_name=}')

    def upload_entries_to_pg(self, transform_type: TransformType):
        """insert/upsert/truncate+insert"""
        # TODO

        self._check_entries()
        if not self.postgresql_connection:
            raise Exception('No postgresql_connection provided, cant proceed')


if __name__ == '__main__':
    # note: debug only
    logging.basicConfig(level=logging.INFO)
    curated_list = TableTransfer(
        # 1. local-to-local
        # source_file_name=os.environ['LOCAL_SOURCE_FILE_NAME_CSV'],
        # target_file_name=os.environ['LOCAL_TARGET_FILE_NAME_JSON'],

        # 2. local-to-s3
        source_file_name=os.environ['LOCAL_SOURCE_FILE_NAME_CSV'],
        target_s3_bucket=os.environ['S3_BUCKET_LOOKMOM'],
        target_file_name=os.environ['S3_TARGET_FILE_NAME_JSON'],

        # 3. s3-to-s3
        # source_s3_bucket=os.environ['S3_BUCKET_LOOKMOM'],
        # source_file_name=os.environ['S3_SOURCE_FILE_NAME_CSV'],
        # target_s3_bucket=os.environ['S3_BUCKET_LOOKMOM'],
        # target_file_name=os.environ['S3_TARGET_FILE_NAME_JSON'],
    )
    curated_list.get_entries_from_csv()
    curated_list.upload_entries_to_json()
