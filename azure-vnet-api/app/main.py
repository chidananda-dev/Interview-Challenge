from fastapi import FastAPI, Depends
from app.auth import get_current_user
from app.vnet_creator import create_vnet_with_subnets
from app.storage import store_vnet_data, get_all_vnets
from app.models import VNetRequest

app = FastAPI()

@app.post("/vnet")
def create_vnet(data: VNetRequest, user: str = Depends(get_current_user)):
    result = create_vnet_with_subnets(data)
    store_vnet_data(result)
    return {"message": "VNet created", "details": result}

@app.get("/vnets")
def list_vnets(user: str = Depends(get_current_user)):
    return get_all_vnets()
