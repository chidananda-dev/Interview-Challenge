# Azure VNet API with Python

## Features
- Create VNet with multiple subnets in Azure
- Store and retrieve metadata
- JWT authentication

## Setup

1. Clone the repo
2. Install requirements:  
   ```bash
   pip install -r requirements.txt
   ```
3. Fill in the `.env` file with your Azure credentials

## Run the App
```bash
uvicorn app.main:app --reload
```

## Generate JWT Token
```bash
python scripts/generate_token.py
```

Use the output token as:
```
Authorization: Bearer <token>
```

## Sample Request

### POST /vnet

```json
{
  "name": "finance-vnet",
  "location": "eastus",
  "resource_group": "rg-finance",
  "address_space": ["10.10.0.0/16"],
  "subnets": [
    {"name": "subnet-db", "address_prefix": "10.10.1.0/24"},
    {"name": "subnet-app", "address_prefix": "10.10.2.0/24"}
  ]
}
```

### GET /vnets

Lists stored VNets from the local DB.
