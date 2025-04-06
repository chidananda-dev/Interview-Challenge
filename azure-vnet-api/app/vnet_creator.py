from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

def create_vnet_with_subnets(data):
    credential = DefaultAzureCredential()
    network_client = NetworkManagementClient(credential, "<SUBSCRIPTION_ID>")

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
