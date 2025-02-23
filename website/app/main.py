#!/bin/env python
import os
from loader.private.raw.reddit import request_and_save_response


def handler(event, context):

    subreddit_list = os.environ['SUBREDDIT_LIST'].split(',')
    subreddit_list = [subreddit.strip() for subreddit in subreddit_list]

    uploaded_list = []
    failed_list = []
    exception_list = []
    for subreddit in subreddit_list:
        try:
            request_and_save_response(subreddit=subreddit)
            uploaded_list.append(subreddit)
        except Exception as exc:
            failed_list.append(subreddit)
            exception_list.append(exc)

    if failed_list:
        return {
            'statusCode': 404,
            'body': f'could not Uploaded files for subreddits={failed_list}, exceptions={exception_list}',
        }
    else:
        return {
            'statusCode': 200,
            'body': f'Uploaded files for subreddits={uploaded_list}',
        }
