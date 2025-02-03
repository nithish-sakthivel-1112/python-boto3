import boto3
import dotenv as loadenv



response = boto3.client('s3')

S3_put_object = response.put_object(
    Body = 'test file',
    Bucket = 'my-bucket-sdk2',
    Key = 'text.txt',
    StorageClass = 'STANDARD'
)

print(S3_put_object)