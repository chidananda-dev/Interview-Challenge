from pydantic import BaseModel
from typing import List

class Subnet(BaseModel):
    name: str
    address_prefix: str

class VNetRequest(BaseModel):
    name: str
    location: str
    resource_group: str
    address_space: List[str]
    subnets: List[Subnet]
