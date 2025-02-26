import boto3
from botocore.exceptions import ClientError

class ECSManager:
    def __init__(self):
        self.client = boto3.client(
            'ecs',
            region_name=os.getenv('AWS_REGION', 'us-east-1')
        )
    
    def list_clusters(self):
        try:
            response = self.client.list_clusters()
            return response['clusterArns']
        except ClientError as e:
            raise Exception(f"Failed to list ECS clusters: {str(e)}")
    
    def list_services(self, cluster):
        try:
            response = self.client.list_services(cluster=cluster)
            return response['serviceArns']
        except ClientError as e:
            raise Exception(f"Failed to list ECS services: {str(e)}")
