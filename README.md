# SecureNova – AI Identity Security Capstone

## Project Overview

The **AI Identity Security Capstone** focuses on designing, implementing, testing, and securing AI identity systems. It addresses security risks associated with AI agents, OAuth clients, API keys, MCP server identities, and LLM-powered applications.

This project demonstrates AI identity threat modelling, Auth0-based identity management, red-team attack simulations, blue-team security controls, and governance through security policies and compliance mapping.

## Project Objectives

- Identify and analyse security threats affecting AI identities.
- Implement secure authentication and authorization using Auth0.
- Simulate AI identity attacks and evaluate their impact.
- Develop defensive controls for credential protection and threat detection.
- Establish AI identity security policies and compliance mappings.
- Prioritize security risks and recommend mitigation strategies.



## Project Modules

### Project 1 – Threat Model the AI Identity System

- Identify AI identity attack surfaces.
- Perform STRIDE threat modelling.
- Create attack trees and assess security risks.
- Map attack paths to MITRE ATLAS techniques.
- Prepare a risk-ranked threat register.

### Project 2 – Build and Secure the Auth0 Application

- Configure Auth0 applications and APIs.
- Implement OAuth 2.0 and PKCE authentication.
- Configure custom API scopes and permissions.
- Implement MFA and attack protection.
- Configure short-lived credentials and identity claims.

### Project 3 – Red Team: AI Identity Attacks

- Simulate indirect prompt injection.
- Demonstrate agent identity spoofing.
- Test system prompt extraction techniques.
- Simulate RAG poisoning and MCP abuse.
- Calculate CVSS 3.1 scores and document attack results.

### Project 4 – Blue Team: Guardrails, Hardening and Detection

- Implement input and output security guardrails.
- Redact exposed JWT credentials.
- Generate and verify cryptographic agent identities using Ed25519.
- Configure token lifetime and refresh token rotation.
- Implement anomaly detection and compare security results before and after defensive controls.

### Project 5 – Policy, Compliance and Summary

- Develop an AI Identity Security Policy.
- Prepare an Incident Response Playbook.
- Map security controls to the NIST AI Risk Management Framework.
- Map relevant attacks and controls to the OWASP LLM Top 10.
- Identify remaining compliance gaps.
- Create a GitHub security portfolio.
- Develop a Risk Priority Matrix.
- Provide five prioritized security recommendations with effort estimates and business rationale.

## Technologies and Tools

- **Identity Management:** Auth0
- **Security Standards:** OAuth 2.0, PKCE, JWT, STRIDE
- **AI Security:** OWASP LLM Top 10, MITRE ATLAS
- **Programming:** Python
- **Cryptography:** Ed25519
- **Security Assessment:** CVSS 3.1
- **Version Control:** Git and GitHub
- **Documentation:** Microsoft Word and Excel

## Key Deliverables

1. AI Identity Threat Model and Risk Register.
2. Auth0 IAM Implementation and Authentication Evidence.
3. Red-Team Attack Simulation Results.
4. Blue-Team Security Controls and Detection Evidence.
5. AI Identity Security Policy and Incident Response Playbook.
6. NIST AI RMF and OWASP LLM Compliance Mapping.
7. Risk Priority Matrix and Top Five Security Recommendations.

## Security Outcomes

The capstone demonstrates how AI identity risks can be identified, tested, mitigated, monitored, and governed through a structured security approach.

It emphasizes least-privilege access, credential protection, secure authentication, prompt injection defence, cryptographic identity verification, and continuous security monitoring.

## Author

**Harshith Dindukurthi.**

AI Identity Security Capstone Project

---

*This repository contains project documentation, implementation artifacts, security testing evidence, and compliance deliverables developed as part of the AI Identity Security Capstone.*
