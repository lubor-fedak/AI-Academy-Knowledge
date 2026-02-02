# Lab 04: Deploy AI Application to Azure

## Overview

Building an AI application is only half the battle - you need to deploy it so users can actually use it. In this lab, you'll containerize your AI application and deploy it to Azure Container Apps.

## Learning Objectives

By the end of this lab, you will be able to:
- Containerize a Python AI application with Docker
- Configure Azure Container Apps for AI workloads
- Manage secrets securely with Azure Key Vault
- Set up health checks and monitoring
- Implement basic CI/CD pipeline

## Prerequisites

- Completed Labs 01-03
- Azure CLI installed and authenticated
- Docker Desktop installed
- Basic Docker knowledge

## Time Estimate

**Total: 90 minutes**
- Containerization: 30 minutes
- Azure setup: 25 minutes
- Deployment: 20 minutes
- Verification: 15 minutes

## Target Roles

- **Primary:** AI-SE, FDE
- **Secondary:** AI-PM (for understanding)

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   GitHub    │────▶│   Azure     │────▶│  Container  │
│   Actions   │     │   ACR       │     │    Apps     │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                    ┌──────────────────────────┤
                    │                          │
              ┌─────▼─────┐              ┌─────▼─────┐
              │ Key Vault │              │ App       │
              │ (Secrets) │              │ Insights  │
              └───────────┘              └───────────┘
```

## Success Criteria

- [ ] Docker image builds successfully
- [ ] Image pushed to Azure Container Registry
- [ ] Container Apps deployment works
- [ ] Health endpoint responds correctly
- [ ] Secrets not exposed in code or logs
- [ ] Application Insights shows telemetry
- [ ] API responds to requests

## Deliverables

1. **Dockerfile** - production-ready, multi-stage
2. **Deployment config** - Azure CLI commands or Bicep/ARM
3. **Health check endpoint** - `/health` returns status
4. **Deployment runbook** - step-by-step instructions
5. **Verification checklist** - prove it works
