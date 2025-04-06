# Azure VNet API with Python

## Features
- Create VNet with multiple subnets in Azure
- Store and retrieve metadata
- JWT authentication

## Run Locally
```bash
uvicorn app.main:app --reload
```

## API
- `POST /vnet` – Create VNet (Authenticated)
- `GET /vnets` – List VNets (Authenticated)

## Auth
Use JWT token: `"Authorization: Bearer <token>"`

## Configuration
Set environment variables for Azure credentials:
- AZURE_CLIENT_ID
- AZURE_TENANT_ID
- AZURE_CLIENT_SECRET
