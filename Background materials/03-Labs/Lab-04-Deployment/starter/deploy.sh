#!/bin/bash
# AI Academy Lab 04 - Deployment Script

set -e

# Configuration
RESOURCE_GROUP="rg-ai-academy-lab04"
LOCATION="westeurope"
ACR_NAME="aiacademyacr$(openssl rand -hex 4)"
APP_NAME="ai-app-lab04"

echo "=== AI Academy Lab 04 Deployment ==="

# TODO: Add deployment steps
# 1. Create resource group
# 2. Create ACR
# 3. Build and push image
# 4. Create Container Apps environment
# 5. Deploy application
# 6. Configure secrets
# 7. Verify deployment

echo "Deployment complete!"
