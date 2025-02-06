#This script will help you to create bucket
import boto3
import dotenv as loadenv

bucket_name = 'my-bucket-sdk3'
response = boto3.client('s3')
try:
    S3_create_bucket = response.create_bucket(
    Bucket = bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1',
    }
)
except response.exceptions.BucketAlreadyOwnedByYou:
    print(f"Bucket '{bucket_name}' already exists.")

file_name = 'hi.txt'

try:
    response.put_object(
    Bucket = bucket_name,
    Key = file_name,
)
except Exception as e:
    print(f"Error uploading a file: '{e}'")

