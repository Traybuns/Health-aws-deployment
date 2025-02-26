import boto3
from botocore.exceptions import ClientError

class KubernetesManager:
    def __init__(self, region="eu-north-1"):
        self.client = boto3.client(
            'eks',
            region_name=os.getenv('AWS_REGION', 'eu-north-1')
        )
    
    def list_clusters(self):
        try:
            response = self.client.list_clusters()
            return response['clusters']
        except ClientError as e:
            raise Exception(f"Failed to list EKS clusters: {str(e)}")
