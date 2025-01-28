import boto3
import dotenv

client = boto3.client('iam')

iam_policy = client.attach_user_policy(
    PolicyArn='arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess',UserName = 'nithish'
)