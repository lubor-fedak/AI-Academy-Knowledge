# Day 8: Works on My Machine

## FDE Track - Week 2, Day 8

---

## The Situation

### "Ship It!"

```
Development is done. The system works perfectly on your laptop.

Now you need to deploy it to Azure for GlobalBank to access.

You try to containerize it. Build fails.
You fix the build. Container starts but can't reach the API.
You fix the networking. Now it times out on large documents.
You fix the timeout. Now secrets are exposed in logs.

It's 6 PM. The deployment was supposed to be done by 3 PM.
GlobalBank's IT team is waiting to do security review.

"It works on my machine" doesn't work anymore.
```

---

## Your Challenge

Deploy your AI application to Azure Container Apps properly.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Containerized** | Builds and runs in Docker |
| **Deployed** | Accessible via HTTPS URL |
| **Configured** | Environment-specific settings |
| **Secure** | No secrets in code or logs |
| **Observable** | Logs and metrics visible |

### Deliverables

1. **Dockerfile** (production-ready)
   - Multi-stage build
   - Non-root user
   - Health check

2. **Deployment Config**
   - Azure Container Apps YAML or Bicep
   - Environment variables configured
   - Secrets from Key Vault

3. **Deployment Runbook** (1 page)
   - Step-by-step deployment guide
   - Rollback procedure
   - Troubleshooting common issues

---

## Micro-Context (5 minutes)

> "Works on my machine" is the enemy of production. Key principles:
> - **Everything in code** - No manual configuration steps
> - **Environment variables** - No hardcoded config
> - **Secrets in vault** - Never in code, never in logs
> - **Health checks** - Know if it's actually running
> - **Graceful shutdown** - Handle termination signals
>
> Hint: If you can't deploy it in one command, you're not done.

---

## Deployment Checklist

### Container Basics
- [ ] Multi-stage Dockerfile (build + runtime)
- [ ] Non-root user in container
- [ ] Health check endpoint (/health)
- [ ] Graceful shutdown handling (SIGTERM)
- [ ] .dockerignore excludes unnecessary files

### Configuration
- [ ] All config from environment variables
- [ ] No secrets in code or Dockerfile
- [ ] Secrets from Azure Key Vault
- [ ] Different configs for dev/staging/prod
- [ ] Timeouts configured appropriately

### Networking
- [ ] HTTPS only (no HTTP)
- [ ] CORS configured correctly
- [ ] Ingress rules defined
- [ ] Internal vs external endpoints clear

### Observability
- [ ] Structured logging (JSON format)
- [ ] No secrets/PII in logs
- [ ] Application Insights connected
- [ ] Key metrics exposed
- [ ] Error tracking configured

---

## Common Deployment Failures

| Failure | Symptom | Cause | Fix |
|---------|---------|-------|-----|
| Build fails in CI | Works locally | Local cache, missing deps | Clean build, pin versions |
| Can't reach API | Connection refused | Wrong endpoint URL | Environment variables |
| Timeout on large docs | 504 Gateway Timeout | Default timeout too short | Configure timeouts |
| Secrets in logs | Credentials visible | Logging full requests | Sanitize log output |
| Container restarts | CrashLoopBackOff | No health check | Add /health endpoint |
| High memory usage | OOMKilled | No memory limit | Set resource limits |

---

## Dockerfile Template

```dockerfile
# Build stage
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim

# Security: non-root user
RUN useradd --create-home --shell /bin/bash app
USER app

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --chown=app:app . .

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Hints

<details>
<summary>Hint 1: Azure Container Apps basics (Click after 10 min)</summary>

Quick deploy to Container Apps:
```bash
# Build and push to ACR
az acr build --registry myacr --image myapp:v1 .

# Create Container App
az containerapp create \
  --name myapp \
  --resource-group myrg \
  --image myacr.azurecr.io/myapp:v1 \
  --target-port 8000 \
  --ingress external
```
</details>

<details>
<summary>Hint 2: Secrets from Key Vault (Click after 25 min)</summary>

Never put secrets in environment variables directly. Reference Key Vault:
```yaml
secrets:
  - name: openai-key
    keyVaultUrl: https://myvault.vault.azure.net/secrets/openai-key
```
</details>

<details>
<summary>Hint 3: Debugging container issues (Click after 40 min)</summary>

Container won't start? Check in order:
1. `az containerapp logs show` - Application logs
2. `az containerapp revision list` - Revision status
3. Test locally: `docker run -p 8000:8000 myapp`
4. Check resource limits - might be OOM
</details>

---

## Self-Study Assignment (90 min)

1. **Create production Dockerfile** (30 min)
2. **Deploy to Azure Container Apps** (45 min)
3. **Write deployment runbook** (15 min)

### Stretch Goals
- Set up GitHub Actions for CI/CD
- Implement blue-green deployment
- Add auto-scaling rules
