# Deploy CI/CD using Terraform in a GCP Project

Following resources needs to be created.

1. Google Cloud Repository
2. Google Cloud Build
3. Google Cloud Run

Additional steps:
a. Create new GCP Project or select exising project
b. Create Service account(SA) and assign the IAM roles to SA with Editor, Security Admin, Service Usage Consumer, Source Repository Administrator IAM Permissions.
c. Download key as terraform.json or someother file name of your choice
d. Export GOOGLE_CLOUD_KEYFILE_JSON=terraform-admin.json or your desired file name

```
 git clone  https://github.com/rajranganathan/gcp-demo-app.git
 cd  gcp-demo-app/terraform
``` 
4. terraform init
5. terraform plan
6. terraform apply

### Following steps to push the code into CSR
1. cd to root
``` 
cd..
```

2.  set remote
```shell script
git remote add google https://source.developers.google.com/p/[PROJECT_ID]/r/[REPO_NAME]
```

3. Push the code 
```shell script
git push --all google
```


#### If you want to maintain Terraform state in Google Cloud Storage 
1. export GCP_PROJECT={YOUR_PROJECT_ID}
2. export TF_STATE=${GCP_PROJECT}-state
3. gsutil mb -p ${GCP_PROJECT} gs://${TF_STATE}
4. cat > backend.tf << EOF
terraform {
 backend "gcs" {
   bucket  = "${TF_STATE}"
   prefix  = "terraform/state"
 }
}
EOF
4. gsutil versioning set on gs://${TF_STATE}
