from fastapi import FastAPI, HTTPException
from aws.rds import RDSManager
from aws.kubernetes import KubernetesManager
from aws.ecs import ECSManager
import os

app = FastAPI(title="AWS Management API")


rds = RDSManager()
kubernetes = KubernetesManager()
ecs = ECSManager()

@app.get("/aws/rds/instances")
async def list_rds_instances():
    try:
        return rds.list_instances()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/aws/kubernetes/clusters")
async def list_kubernetes_clusters():
    try:
        return kubernetes.list_clusters()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/aws/ecs/clusters")
async def list_ecs_clusters():
    try:
        return ecs.list_clusters()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/aws/ecs/services/{cluster}")
async def list_ecs_services(cluster: str):
    try:
        return ecs.list_services(cluster)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

#dxgxvgxjHXtXxtGfxzfxvxfx