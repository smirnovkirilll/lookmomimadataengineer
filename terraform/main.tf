# https://developer.hashicorp.com/terraform/tutorials/configuration-language/sensitive-variables


variable "revision" {
  default = 2
}


terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
  backend "s3" {
    skip_region_validation      = true
    skip_credentials_validation = true
    skip_requesting_account_id  = true  # option needed for Terraform version >= 1.6.1
    skip_s3_checksum            = true  # option needed for Terraform version >= 1.6.1
  }
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


resource "terraform_data" "reddit_digest_zip" {
  triggers_replace = {
    revision = var.revision
  }
  provisioner "local-exec" {
    command = "cd ../website/app/reddit_digest; zip -FSr reddit_digest {requirements.txt,__init__.py,helpers.py,reddit_request.py,main.py}; mv reddit_digest.zip ../../../terraform/state_and_vars"
  }
}


resource "yandex_function" "reddit_digest_ingest_raw" {
  name               = "reddit-digest-ingest-raw"
  description        = "requests some subreddits on reddit, saves response to s3"
  user_hash          = var.revision
  runtime            = "python312"
  entrypoint         = "main.handler"
  memory             = "256"
  execution_timeout  = "30"
  service_account_id = var.service_account_id
  tags               = ["reddit_digest"]
  environment = {
    LOCKBOX_SECRET_ID = yandex_lockbox_secret.reddit_digest.id
    S3_BUCKET = var.s3_bucket
    S3_ENDPOINT_URL = var.s3_endpoint_url
    REGION_NAME = var.region_name
    SUBREDDIT_LIST = var.subreddit_list
  }
  depends_on = [terraform_data.reddit_digest_zip]
  content {
    zip_filename = "state_and_vars/reddit_digest.zip"
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


output revision {value = var.revision}
output yandex_storage_bucket_id {value = yandex_storage_bucket.bucket.id}
output yandex_lockbox_secret_id {value = yandex_lockbox_secret.reddit_digest.id}
output reddit_digest_ingest_raw_id {value = yandex_function.reddit_digest_ingest_raw.id}
output yandex_function_trigger_id {value = yandex_function_trigger.reddit_digest_ingest_raw_trigger.id}
