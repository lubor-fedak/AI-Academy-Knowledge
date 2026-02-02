# OWASP LLM Top 10 Security Checklist

## LLM01: Prompt Injection

- [ ] Input validation implemented
- [ ] System prompt hardening applied
- [ ] Indirect injection vectors assessed
- [ ] User inputs separated from instructions

## LLM02: Insecure Output Handling

- [ ] Output sanitization implemented
- [ ] PII/secrets filtering active
- [ ] XSS prevention for web display
- [ ] Command injection prevention

## LLM03: Training Data Poisoning

- [ ] Data sources validated
- [ ] Fine-tuning data reviewed
- [ ] Update process secured

## LLM04: Model Denial of Service

- [ ] Rate limiting implemented
- [ ] Input length limits set
- [ ] Resource quotas configured
- [ ] Timeout handling

## LLM05: Supply Chain Vulnerabilities

- [ ] Dependencies reviewed
- [ ] Model provenance verified
- [ ] Plugin security assessed

## LLM06: Sensitive Information Disclosure

- [ ] System prompt protected
- [ ] Training data not exposed
- [ ] Logs sanitized
- [ ] Error messages safe

## LLM07: Insecure Plugin Design

- [ ] Plugin permissions minimal
- [ ] Input validation for plugins
- [ ] Authentication required

## LLM08: Excessive Agency

- [ ] Actions require confirmation
- [ ] Scope limitations enforced
- [ ] Human-in-the-loop for critical actions

## LLM09: Overreliance

- [ ] Confidence indicators shown
- [ ] Source attribution provided
- [ ] "I don't know" responses enabled

## LLM10: Model Theft

- [ ] API access controlled
- [ ] Rate limiting prevents bulk extraction
- [ ] Logging detects abuse patterns
