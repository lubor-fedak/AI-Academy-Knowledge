# Lab 04: Mentor Notes

## Key Concepts

1. **Container best practices:** Multi-stage, non-root, health checks
2. **Secret management:** Never in code, use Key Vault
3. **Infrastructure as Code:** Reproducible deployments
4. **Observability:** Logs, metrics, traces from day one

## Common Struggles

### "Docker build fails"
**Causes:** Missing dependencies, wrong base image, path issues
**Intervention:** Check build output. Start with simpler Dockerfile.

### "Can't push to ACR"
**Causes:** Not logged in, wrong registry name, permissions
**Intervention:** `az acr login --name <name>`, check RBAC

### "Container starts but crashes"
**Causes:** Missing env vars, port mismatch, dependency issues
**Intervention:** Check logs: `az containerapp logs show`

### "API key not working"
**Causes:** Secret not mounted, wrong name, permissions
**Intervention:** Verify secret exists, check env var name

## Security Reminders

- NEVER commit .env files
- NEVER hardcode secrets
- ALWAYS use managed identities where possible
- ALWAYS use HTTPS in production

## Debrief Topics

1. **Why containers?** Consistency, isolation, scalability
2. **Why Container Apps vs. AKS?** Simpler, managed, serverless-ish
3. **CI/CD importance:** Manual deployment doesn't scale
4. **Cost management:** Pay per use, set budgets

## What Good Looks Like

- Clean Dockerfile with comments
- Documented deployment process
- Working health endpoint
- No secrets in code
- Monitoring configured
