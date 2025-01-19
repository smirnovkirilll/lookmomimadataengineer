tf-init:
	terraform init -backend-config="state_and_vars/backend.conf"
tf-plan:
	terraform plan -var-file="state_and_vars/secret.tfvars"
tf-apply:
	terraform apply -var-file="state_and_vars/secret.tfvars"
