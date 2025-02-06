import boto3


ec2_create_resources= boto3.client('ec2', 'us-east-1')

#create EC2 Instance 

response = ec2_create_resources.run_instances(
    ImageId='ami-0e1bed4f06a3b463d',
    InstanceType='t2.micro',
    MaxCount=1, #Max no of instances to launch
    MinCount=1, #Min no of instances to launch 
    #SubnetId = 'Replace with you Subnet id ',  #Not required it is optional
   
)

print(response)