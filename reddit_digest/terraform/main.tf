#!/bin/env -S terraform plan


terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}


provider "yandex" {
  token = var.yc_token
  cloud_id = var.yc_cloud_id
  folder_id = var.yc_folder_id
}


resource "yandex_storage_bucket" "bucket" {
  access_key = var.s3_access_key
  secret_key = var.s3_secret_key
  bucket = var.s3_bucket
  max_size = 53687091200  # 50GB
}


# todo: doesn't work properly, created support ticket
resource "yandex_lockbox_secret" "reddit_digest" {
  name = "reddit_digest"
}


# todo: doesn't work properly, created support ticket
resource "yandex_lockbox_secret_version_hashed" "version_0" {
  secret_id = yandex_lockbox_secret.reddit_digest.id
  key_1 = "ACCESS_KEY_ID"
  text_value_1 = var.s3_access_key
  key_2 = "SECRET_ACCESS_KEY"
  text_value_2 = var.s3_secret_key
  description = "sensitive information for "
}


resource "null_resource" "reddit_digest_zip" {
  provisioner "local-exec" {
    command = "zip reddit_digest ../requirements.txt ../helpers.py ../reddit_request.py ../main.py"
  }
}


#  todo: doesn't work properly, created support ticket
resource "yandex_function" "reddit_digest_ingest_raw" {
  name               = "reddit_digest_ingest_raw"
  description        = "requests some subreddits on reddit, saves response to s3"
  user_hash          = "v0"
  runtime            = "python313"
  entrypoint         = "main.handler"
  memory             = "128"
  execution_timeout  = "10"
  service_account_id = var.service_account_id
  tags               = ["reddit_digest"]
  environment = {
    LOCKBOX_SECRET_ID = yandex_lockbox_secret.reddit_digest.id
    S3_BUCKET = var.s3_bucket
    S3_ENDPOINT_URL = var.s3_endpoint_url
    REGION_NAME = var.region_name
    SUBREDDIT_LIST = var.subreddit_list
  }
  depends_on = [null_resource.reddit_digest_zip]
  content {
    zip_filename = "reddit_digest.zip"
  }
}


#  todo: doesn't work properly, created support ticket
resource "yandex_function_trigger" "reddit_digest_ingest_raw_trigger" {
  name        = "reddit_digest_ingest_raw_trigger"
  description = "starts reddit_digest_ingest_raw"
  timer {
    cron_expression = "0 10 * * *"
  }
  function {
    id = yandex_function.reddit_digest_ingest_raw.id
  }
}
