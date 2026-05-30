import boto3

ec2 = boto3.client('S3')

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance['State']['DEV'])
