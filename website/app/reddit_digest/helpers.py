#!/bin/env python
# note: the implementation is partially borrowed from official documents and training courses https://yandex.cloud

import boto3
import logging
import os
import yandexcloud
from io import BytesIO
from yandex.cloud.lockbox.v1.payload_service_pb2 import GetPayloadRequest
from yandex.cloud.lockbox.v1.payload_service_pb2_grpc import PayloadServiceStub


logger = logging.getLogger('logging cloud actions')
logger.setLevel(logging.INFO)
boto_session = None
storage_client = None
docapi_table = None
ymq_queue = None


def _get_environ_aws_secrets():
    """for development and local usage"""

    secret_id = None
    access_key = os.environ['ACCESS_KEY_ID']
    secret_key = os.environ['SECRET_ACCESS_KEY']

    return secret_id, access_key, secret_key


def _get_lockbox_aws_secrets():

    secret_id = os.environ['LOCKBOX_SECRET_ID']
    access_key = None
    secret_key = None

    # initialize lockbox and read secret value
    yc_sdk = yandexcloud.SDK()
    channel = yc_sdk._channels.channel('lockbox-payload')
    lockbox = PayloadServiceStub(channel)
    response = lockbox.Get(GetPayloadRequest(secret_id=secret_id))

    # extract values from secret
    for entry in response.entries:
        if entry.key == 'ACCESS_KEY_ID':
            access_key = entry.text_value
        elif entry.key == 'SECRET_ACCESS_KEY':
            secret_key = entry.text_value
    if access_key is None or secret_key is None:
        raise Exception('secrets required')

    return secret_id, access_key, secret_key


def get_aws_secrets():

    if os.environ.get('LOCKBOX_SECRET_ID'):
        return _get_lockbox_aws_secrets()
    else:
        return _get_environ_aws_secrets()


def get_boto_session():

    global boto_session
    if boto_session is not None:
        return boto_session

    secret_id, access_key, secret_key = get_aws_secrets()

    boto_session = boto3.session.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    logger.info(f'Built boto-session for secret_id={secret_id}')

    return boto_session


def get_ymq_queue():

    global ymq_queue
    if ymq_queue is not None:
        return ymq_queue

    ymq_queue_url = os.environ['YMQ_QUEUE_URL']
    endpoint_url = os.environ['YMQ_ENDPOINT_URL']
    region_name = os.environ['REGION_NAME']

    ymq_queue = get_boto_session().resource(
        service_name='sqs',
        endpoint_url=endpoint_url,
        region_name=region_name,
    ).queue(ymq_queue_url)
    logger.info(f'Got sqs={ymq_queue_url}')

    return ymq_queue


def get_docapi_table(table_name: str):

    global docapi_table
    if docapi_table is not None:
        return docapi_table

    endpoint_url = os.environ['DOCAPI_ENDPOINT_URL']
    region_name = os.environ['REGION_NAME']

    docapi_table = get_boto_session().resource(
        service_name='dynamodb',
        endpoint_url=endpoint_url,
        region_name=region_name,
    ).Table(table_name)
    logger.info(f'Got YDB-table={table_name}')

    return docapi_table


def get_storage_client():

    global storage_client
    if storage_client is not None:
        return storage_client

    endpoint_url = os.environ['S3_ENDPOINT_URL']
    region_name = os.environ['REGION_NAME']

    storage_client = get_boto_session().client(
        service_name='s3',
        endpoint_url=endpoint_url,
        region_name=region_name,
    )
    logger.info(f'Got S3-client')

    return storage_client


def upload_object_to_s3(bucket: str, file_name: str, data_obj: bytes):

    temp_file = BytesIO()
    temp_file.write(data_obj)
    temp_file.seek(0)

    client = get_storage_client()
    logger.info(f'Starting upload to S3 file_name={file_name}')
    client.upload_fileobj(temp_file, bucket, file_name)
