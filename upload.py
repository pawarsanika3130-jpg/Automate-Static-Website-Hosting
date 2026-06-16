import boto3

s3 = boto3.client('s3')

bucket_name = "mycap-project-5-bucket"

s3.upload_file(
    "index.html",
    bucket_name,
    "index.html",
    ExtraArgs={
        "ContentType": "text/html"
    }
)

print("File Uploaded Successfully")