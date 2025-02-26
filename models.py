Base.metadata.create_all(bind=engine)

@app.post("/signup/")
def signup(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    return {"message": "User created successfully"}

@app.post("/login/")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token}

@app.post("/aws/deploy_rds/")
def deploy_database(instance_name: str, user: dict = Depends(get_current_user)):
    return deploy_rds(instance_name)

@app.get("/aws/list_rds/")
def list_databases(user: dict = Depends(get_current_user)):
    return list_rds_instances()

@app.delete("/aws/delete_rds/")
def delete_database(instance_name: str, user: dict = Depends(get_current_user)):
    return delete_rds(instance_name)

@app.post("/aws/deploy_k8s/")
def deploy_kubernetes_cluster(cluster_name: str, user: dict = Depends(get_current_user)):
    return deploy_kubernetes(cluster_name)

@app.get("/aws/list_k8s/")
def list_kubernetes_clusters(user: dict = Depends(get_current_user)):
    return list_k8s_clusters()

@app.delete("/aws/delete_k8s/")
def delete_kubernetes_cluster(cluster_name: str, user: dict = Depends(get_current_user)):
    return delete_kubernetes_cluster(cluster_name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)