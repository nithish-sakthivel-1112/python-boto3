import boto3
import dotenv

client = boto3.client('iam')

iam = client.create_user(
    UserName = 'nithish'
)




