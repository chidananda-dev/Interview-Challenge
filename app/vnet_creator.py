from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
import os

def create_vnet_with_subnets(data):
    credential = DefaultAzureCredential()
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    network_client = NetworkManagementClient(credential, subscription_id)

    vnet_result = network_client.virtual_networks.begin_create_or_update(
        data.resource_group,
        data.name,
        {
            "location": data.location,
            "address_space": {"address_prefixes": data.address_space},
            "subnets": [{"name": s.name, "address_prefix": s.address_prefix} for s in data.subnets]
        }
    ).result()

    return {
        "vnet": vnet_result.name,
        "location": vnet_result.location,
        "subnets": [s.name for s in vnet_result.subnets]
    }
