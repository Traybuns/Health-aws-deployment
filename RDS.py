import boto3
from botocore.exceptions import ClientError
import os

class RDSManager:
    def __init__(self,):
        self.client = boto3.client(
            'rds',
            region_name=os.getenv('AWS_REGION', 'eu-north-1')
        )
    
    def list_instances(self):
        try:
            response = self.client.describe_db_instances()
            return response['DBInstances']
        except ClientError as e:
            raise Exception(f"Failed to list RDS instances: {str(e)}")
