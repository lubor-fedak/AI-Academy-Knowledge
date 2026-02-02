# Lab 04: Instructions

## Phase 1: Containerization (30 min)

### Step 1.1: Create Dockerfile

Create a production-ready Dockerfile:

```dockerfile
# Build stage
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim

WORKDIR /app

# Create non-root user
RUN useradd --create-home appuser
USER appuser

# Copy dependencies from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy application code
COPY --chown=appuser:appuser . .

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Key points:**
- Multi-stage build reduces image size
- Non-root user for security
- Health check for orchestrator
- No secrets in image

### Step 1.2: Create .dockerignore

```
.env
.git
__pycache__
*.pyc
.pytest_cache
.venv
venv
*.md
tests/
```

### Step 1.3: Add Health Endpoint

```python
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }
```

### Step 1.4: Test Locally

```bash
# Build image
docker build -t ai-app:local .

# Run container
docker run -p 8000:8000 --env-file .env ai-app:local

# Test health
curl http://localhost:8000/health
```

---

## Phase 2: Azure Setup (25 min)

### Step 2.1: Login and Set Variables

```bash
# Login to Azure
az login

# Set variables
RESOURCE_GROUP="rg-ai-academy-lab04"
LOCATION="westeurope"
ACR_NAME="aiacademyacr$(openssl rand -hex 4)"
APP_NAME="ai-app-lab04"
```

### Step 2.2: Create Resource Group

```bash
az group create \
    --name $RESOURCE_GROUP \
    --location $LOCATION
```

### Step 2.3: Create Container Registry

```bash
az acr create \
    --resource-group $RESOURCE_GROUP \
    --name $ACR_NAME \
    --sku Basic \
    --admin-enabled true
```

### Step 2.4: Create Key Vault

```bash
KEY_VAULT_NAME="kv-ai-academy-$(openssl rand -hex 4)"

az keyvault create \
    --name $KEY_VAULT_NAME \
    --resource-group $RESOURCE_GROUP \
    --location $LOCATION

# Store API key
az keyvault secret set \
    --vault-name $KEY_VAULT_NAME \
    --name "GEMINI-API-KEY" \
    --value "your-api-key-here"
```

### Step 2.5: Create Container Apps Environment

```bash
az containerapp env create \
    --name "ai-academy-env" \
    --resource-group $RESOURCE_GROUP \
    --location $LOCATION
```

---

## Phase 3: Deployment (20 min)

### Step 3.1: Push Image to ACR

```bash
# Login to ACR
az acr login --name $ACR_NAME

# Tag image
docker tag ai-app:local $ACR_NAME.azurecr.io/ai-app:v1

# Push image
docker push $ACR_NAME.azurecr.io/ai-app:v1
```

### Step 3.2: Deploy to Container Apps

```bash
# Get ACR credentials
ACR_PASSWORD=$(az acr credential show --name $ACR_NAME --query "passwords[0].value" -o tsv)

# Deploy
az containerapp create \
    --name $APP_NAME \
    --resource-group $RESOURCE_GROUP \
    --environment "ai-academy-env" \
    --image "$ACR_NAME.azurecr.io/ai-app:v1" \
    --registry-server "$ACR_NAME.azurecr.io" \
    --registry-username $ACR_NAME \
    --registry-password $ACR_PASSWORD \
    --target-port 8000 \
    --ingress external \
    --min-replicas 1 \
    --max-replicas 3 \
    --cpu 0.5 \
    --memory 1.0Gi \
    --env-vars "LOG_LEVEL=INFO"
```

### Step 3.3: Configure Secrets

```bash
# Add secret from Key Vault
az containerapp secret set \
    --name $APP_NAME \
    --resource-group $RESOURCE_GROUP \
    --secrets "gemini-api-key=keyvaultref:$KEY_VAULT_NAME/GEMINI-API-KEY,identityref:/subscriptions/.../managedIdentities/..."
```

---

## Phase 4: Verification (15 min)

### Step 4.1: Get Application URL

```bash
APP_URL=$(az containerapp show \
    --name $APP_NAME \
    --resource-group $RESOURCE_GROUP \
    --query "properties.configuration.ingress.fqdn" -o tsv)

echo "Application URL: https://$APP_URL"
```

### Step 4.2: Test Endpoints

```bash
# Health check
curl https://$APP_URL/health

# Test API (adjust based on your endpoints)
curl -X POST https://$APP_URL/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "Hello!"}'
```

### Step 4.3: Check Logs

```bash
az containerapp logs show \
    --name $APP_NAME \
    --resource-group $RESOURCE_GROUP \
    --follow
```

### Step 4.4: Verification Checklist

- [ ] Health endpoint returns 200
- [ ] Chat endpoint works
- [ ] No secrets in logs
- [ ] Application Insights shows requests
- [ ] Scaling works (load test optional)

---

## Extension Challenges

1. **CI/CD Pipeline:** Create GitHub Actions workflow
2. **Custom domain:** Add your own domain with SSL
3. **Auto-scaling:** Configure scale rules based on HTTP traffic
4. **Blue-green deployment:** Zero-downtime updates
5. **Monitoring alerts:** Set up alerts for errors/latency

---

## Cleanup

```bash
# Delete resource group (removes everything)
az group delete --name $RESOURCE_GROUP --yes --no-wait
```

---

## Submission

Upload to SharePoint `/07-Submissions/Labs/Lab-04/`:
- `Dockerfile`
- `deploy.sh` (or `deploy.ps1`)
- `runbook.md` (deployment steps)
- `verification.md` (proof it works - screenshots, curl outputs)
- `REFLECTION.md`
