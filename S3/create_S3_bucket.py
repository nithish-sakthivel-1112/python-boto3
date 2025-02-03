#This script will help you to create bucket
import boto3
import dotenv as loadenv

response = boto3.client('s3')

S3_create_bucket = response.create_bucket(
    Bucket = 'my-bucket-sdk2',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1',
    },
)

