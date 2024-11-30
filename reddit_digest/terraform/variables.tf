variable "yc_token" {
  description = "token for yandex cloud"
  type        = string
  sensitive   = true
}
variable "yc_cloud_id" {
  description = "yandex cloud id"
  type        = string
  sensitive   = true
}
variable "yc_folder_id" {
  description = "yandex cloud folder id"
  type        = string
  sensitive   = true
}
variable "region_name" {
  description = "region name"
  type        = string
  sensitive   = false
}
variable "s3_endpoint_url" {
  description = "s3 endpoint url"
  type        = string
  sensitive   = false
}
variable "s3_access_key" {
  description = "s3 access key id"
  type        = string
  sensitive   = true
}
variable "s3_secret_key" {
  description = "s3 secret access key"
  type        = string
  sensitive   = true
}
variable "s3_bucket" {
  description = "s3 bucket name"
  type        = string
  sensitive   = false
}
variable "service_account_id" {
  description = "service account id of robot to execute serverless functions"
  type        = string
  sensitive   = true
}
variable "subreddit_list" {
  description = "list of subreddits to be requested"
  type        = string
  sensitive   = false
}
