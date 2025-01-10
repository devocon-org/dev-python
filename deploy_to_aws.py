import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def deploy_instance(region, instance_type, ami_id):
    ec2 = boto3.resource('ec2', region_name=region)

    try:
        print(f"Deploying EC2 instance of type {instance_type} using AMI {ami_id} in {region}")
        instance = ec2.create_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1
        )
        print(f"EC2 instance {instance[0].id} deployed successfully.")
        return instance[0].id
    except (NoCredentialsError, PartialCredentialsError) as e:
        print("AWS credentials are not set properly.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    deploy_instance(region="us-west-2", instance_type="t2.micro", ami_id="ami-12345678")
