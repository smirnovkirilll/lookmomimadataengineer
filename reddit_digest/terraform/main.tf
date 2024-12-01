#!/bin/env -S terraform plan
# https://developer.hashicorp.com/terraform/tutorials/configuration-language/sensitive-variables
# terraform init
# terraform plan -var-file="secret.tfvars"
# terraform apply -var-file="secret.tfvars"


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


resource "yandex_lockbox_secret" "reddit_digest" {
  name = "reddit_digest"
  description = "sensitive information for reddit-digest application"
}


resource "yandex_lockbox_secret_version_hashed" "version_0" {
  secret_id = yandex_lockbox_secret.reddit_digest.id
  key_1 = "ACCESS_KEY_ID"
  text_value_1 = var.s3_access_key
  key_2 = "SECRET_ACCESS_KEY"
  text_value_2 = var.s3_secret_key
}


resource "random_uuid" "new_on_every_run" {}


resource "null_resource" "reddit_digest_zip" {
  triggers = {
    uuid = random_uuid.new_on_every_run.id
  }
  provisioner "local-exec" {
    command = "mkdir app; cp ../{requirements.txt,__init__.py,helpers.py,reddit_request.py,main.py} app; zip -r reddit_digest app; rm -rf app;"
  }
}


# todo: does not work properly yet
resource "yandex_function" "reddit_digest_ingest_raw" {
  name               = "reddit-digest-ingest-raw"
  description        = "requests some subreddits on reddit, saves response to s3"
  user_hash          = random_uuid.new_on_every_run.id
  runtime            = "python312"
  entrypoint         = "app.main.handler"
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


resource "yandex_function_trigger" "reddit_digest_ingest_raw_trigger" {
  name        = "reddit-digest-ingest-raw-trigger"
  description = "starts function reddit-digest-ingest-raw"
  timer {
    # crontab-guru says it's incorrect, but YC wants this format
    cron_expression = "0 10 * * ? *"
  }
  function {
    id = yandex_function.reddit_digest_ingest_raw.id
    service_account_id = var.service_account_id
  }
}


output yandex_storage_bucket_id {value = yandex_storage_bucket.bucket.id}
output yandex_lockbox_secret_id {value = yandex_lockbox_secret.reddit_digest.id}
output reddit_digest_ingest_raw_id {value = yandex_function.reddit_digest_ingest_raw.id}
output reddit_digest_ingest_raw_user_hash {value = random_uuid.new_on_every_run.id}
output yandex_function_trigger_id {value = yandex_function_trigger.reddit_digest_ingest_raw_trigger.id}
