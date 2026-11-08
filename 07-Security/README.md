# Module 07: Security & Compliance

## Overview
Security is the foundation of AWS Solutions Architecture. This module covers encryption, monitoring, compliance, and security services.

## Learning Objectives
- Implement encryption with KMS and CloudHSM
- Secure applications with WAF, Shield, and GuardDuty
- Manage secrets with Secrets Manager and Parameter Store
- Understand AWS compliance and governance services
- Implement security best practices

---

## 1. AWS KMS (Key Management Service)

### What is KMS?
- **Managed service** for creating and controlling encryption keys
- Integrated with most AWS services
- **FIPS 140-3 Level 3** validated HSMs (Level 3 overall since May 2023; before that, Level 2 overall)
- Audit with CloudTrail
- **Regional service**

### KMS Key Types

**Symmetric Keys (AES-256)**
- **Single key** for encrypt and decrypt
- AWS services use symmetric CMKs
- **Never get access to the key itself** (must call KMS API)
- Most common use case

**Asymmetric Keys (RSA & ECC)**
- **Public key** (download) and **Private key** (cannot access)
- Use for encrypt/decrypt or sign/verify
- Public key is downloadable
- Use case: Encryption outside AWS, users can't call KMS API

### KMS Keys

**AWS Managed Keys**
- Free
- Automatic rotation every 1 year
- Format: `aws/service-name` (e.g., `aws/s3`)

**Customer Managed Keys**
- **$1/month**
- Rotation: Optional automatic rotation with a configurable period of 90-2,560 days (default 365), plus on-demand rotation
- Can enable/disable
- Full control over key policy

**AWS Owned Keys**
- Used by AWS on shared basis across accounts
- You don't see or manage
- Free

**CloudHSM Keys (Custom Key Store)**
- Keys stored in CloudHSM cluster
- More expensive

### KMS Key Policies

Default Key Policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "Enable IAM User Permissions",
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::ACCOUNT-ID:root"},
    "Action": "kms:*",
    "Resource": "*"
  }]
}
```

### KMS Operations

**Encryption**:
- `Encrypt`: Encrypt up to 4 KB of data
- `GenerateDataKey`: Generate data key for envelope encryption
- `GenerateDataKeyWithoutPlaintext`: Generate encrypted data key

**Decryption**:
- `Decrypt`: Decrypt ciphertext
- Must have permission in key policy

**Rotation**:
- Automatic: Customer managed keys, configurable period of 90-2,560 days (default 365); AWS managed keys rotate every year
- On-demand: `RotateKeyOnDemand` rotates immediately (maximum 25 on-demand rotations per key, not adjustable)
- Manual: Create new key and update alias

**Limits**:
- **Requests per second** (symmetric cryptographic operations, shared): 10,000 by default
- **20,000** in some Regions and **100,000** in us-east-1, us-west-2 and eu-west-1
- Asymmetric RSA and ECC keys have separate quotas (1,000 per second each)
- Can request quota increase
- Use data key caching to reduce API calls

### Envelope Encryption
- Encrypt data with **Data Key**
- Encrypt Data Key with **Master Key** (KMS)
- Reduces network load (encrypt large files locally)
- `GenerateDataKey` API

---

## 2. AWS CloudHSM

### What is CloudHSM?
- **Hardware Security Module** in AWS Cloud
- **FIPS 140-2 Level 3 or FIPS 140-3 Level 3** validated (depends on HSM type; FIPS-mode clusters)
- **You manage the keys entirely**
- Runs in your VPC
- **Tamper resistant, single-tenant**

### CloudHSM vs KMS

| Feature | KMS | CloudHSM |
|---------|-----|----------|
| **Tenancy** | Multi-tenant | Single-tenant |
| **Key Control** | AWS manages | You manage |
| **FIPS Certification** | FIPS 140-3 Level 3 | FIPS 140-2 or 140-3 Level 3 (by HSM type) |
| **Key Differentiator** | Multi-tenant, AWS-managed | Single-tenant, customer-managed |
| **Key Types** | Symmetric + Asymmetric | Symmetric + Asymmetric |
| **Pricing** | Per API call + key | Per hour (cluster) |
| **Integration** | Native AWS integration | Limited integration |
| **High Availability** | Automatic | Manual (multi-AZ cluster) |

### CloudHSM Use Cases
- **Single-tenant compliance**: Regulated workloads requiring dedicated HSMs
- **Full control** over keys
- **Custom key management**
- SSL/TLS offload
- Oracle TDE (Transparent Data Encryption)

---

## 3. AWS Secrets Manager

### What is Secrets Manager?
- Store, retrieve, rotate **secrets** (passwords, API keys)
- **Automatic rotation** of secrets
- Integration with RDS, Redshift, DocumentDB
- **Encryption** using KMS
- **$0.40 per secret/month** + API calls

### Secrets Manager vs Parameter Store

| Feature | Secrets Manager | Parameter Store |
|---------|----------------|-----------------|
| **Price** | $0.40/secret/month | Free (Standard), $0.05/advanced |
| **Rotation** | Automatic (Lambda) | Manual |
| **Integration** | RDS, Redshift, DocumentDB | Limited |
| **Secret Size** | 64 KB | 4 KB (Standard), 8 KB (Advanced) |
| **Encryption** | Mandatory (KMS) | Optional |
| **Use Case** | Database credentials | Application config |

### Secrets Rotation
- **Automatic rotation**:
  - RDS MySQL/PostgreSQL/Aurora
  - Redshift
  - DocumentDB
- **Lambda function** performs rotation
- Rotation schedule: `rate()` or `cron()` expression, from every 4 hours up to every 999 days

---

## 4. SSM Parameter Store

### What is Parameter Store?
- **Secure storage** for configuration and secrets
- Optional encryption using KMS
- **Serverless, scalable**
- Version tracking
- Integration with CloudFormation

### Parameter Tiers

| Feature | Standard | Advanced |
|---------|----------|----------|
| **Price** | Free | $0.05/parameter/month |
| **Parameters** | 10,000 | 100,000 |
| **Max Size** | 4 KB | 8 KB |
| **Policies** | No | Yes (expiration, notifications) |
| **Throughput** | Standard by default; higher throughput is an optional paid account setting for both tiers | Same as Standard |

### Parameter Policies (Advanced)
- **Expiration**: Delete parameter after date
- **ExpirationNotification**: EventBridge event before expiration
- **NoChangeNotification**: Event if not changed

---

## 5. AWS Certificate Manager (ACM)

### What is ACM?
- Provision, manage, deploy **SSL/TLS certificates**
- **Free** for public certificates
- **Automatic renewal**
- Integration with: ELB, CloudFront, API Gateway
- Standard ACM certificates cannot be installed on EC2; for EC2 or on-premises servers, request an exportable public certificate (paid, available since June 2025) or install a certificate manually

### ACM Features
- **Public Certificates**:
  - Free
  - Auto-renewal
  - Domain validation (email or DNS)
- **Private Certificates**:
  - For internal applications
  - Requires AWS Private Certificate Authority
  - **$400/month** for Private CA
- **Import Certificates**:
  - Third-party certificates
  - Manual renewal

---

## 6. AWS WAF (Web Application Firewall)

### What is WAF?
- Protect web applications from **common exploits**
- Deploy on: **CloudFront, ALB, API Gateway, AppSync**
- Define **Web ACLs** (Access Control Lists)

### WAF Rules
- **IP Set**: Block/allow IPs (up to 10,000)
- **HTTP headers, HTTP body, URI strings**
- **Size constraints** (e.g., > 5 KB)
- **Geo-match**: Block countries
- **Rate-based rules**: DDoS protection (e.g., > 2,000 requests in 5 min)

### Managed Rules
- **AWS Managed Rules**: $1/month per rule group added to a web ACL (plus request charges); Bot Control and Fraud Control (ATP, ACFP) have additional fees
- **AWS Marketplace Rules**: From third parties
- Rule groups for:
  - OWASP Top 10
  - SQL injection
  - Cross-Site Scripting (XSS)
  - Known bad inputs

### WAF Use Cases
- **SQL Injection** prevention
- **Cross-Site Scripting (XSS)** prevention
- **Rate limiting** / DDoS protection
- **Geo-blocking**
- **Block specific user agents**

---

## 7. AWS Shield

### What is AWS Shield?
- **DDoS protection** service

### Shield Standard
- **Free** for all AWS customers
- Protection against common layer 3/4 attacks
- Protects: CloudFront, Route 53, Global Accelerator

### Shield Advanced
- **$3,000/month per organization**
- Enhanced DDoS protection
- **24/7 Shield Response Team (SRT)** (formerly DDoS Response Team; requires Business or Enterprise Support)
- **Cost protection**: Reimbursement for scaling charges during DDoS
- Protects: EC2, ELB, CloudFront, Global Accelerator, Route 53
- Advanced attack analytics and reporting

---

## 8. AWS Firewall Manager

### What is Firewall Manager?
- **Centrally manage security rules** across accounts
- Requires **AWS Organizations**
- Manage:
  - WAF rules
  - Shield Advanced
  - Security Groups
  - Network Firewall
  - Route 53 Resolver DNS Firewall

### Firewall Manager Benefits
- Apply security policies across entire organization
- Automatic remediation of non-compliant resources
- Centralized management

---

## 9. Amazon GuardDuty

### What is GuardDuty?
- **Intelligent threat detection**
- Machine learning to detect anomalies
- **30-day free trial**
- Input data:
  - CloudTrail Events Logs
  - VPC Flow Logs
  - DNS Logs
  - Optional: Kubernetes Audit Logs, RDS Login Events

### GuardDuty Findings
- **Cryptocurrency mining**
- **Unusual API calls**
- **Unauthorized deployments**
- **Compromised instances**
- **Reconnaissance** by attackers

### GuardDuty Integration
- **EventBridge**: Automate remediation
- **SNS**: Notifications
- **Lambda**: Custom actions
- **Detective**: Deep investigation

---

## 10. Amazon Inspector

### What is Inspector?
- **Automated security assessment**
- For **EC2 instances, container images, Lambda functions**
- Checks for:
  - **Vulnerabilities** (CVE)
  - **Network exposure**
  - **Best practice deviations**

### Inspector Features
- Continuous scanning when instances run
- **Risk scores** with findings
- Integration with **Systems Manager**
- Reports sent to **Security Hub**

### Inspector vs GuardDuty
- **Inspector**: Vulnerabilities, configuration issues
- **GuardDuty**: Malicious activity, threats

---

## 11. Amazon Macie

### What is Macie?
- **Data security** and **privacy** service
- Discover and protect **sensitive data in S3**
- Uses machine learning and pattern matching
- Identifies:
  - **PII** (Personally Identifiable Information)
  - **Financial data**
  - **Credentials**

### Macie Use Cases
- GDPR compliance
- PCI-DSS compliance
- Data loss prevention
- S3 bucket security audit

---

## 12. AWS Security Hub

### What is Security Hub?
- **Centralized security management**
- Aggregates findings from:
  - GuardDuty
  - Inspector
  - Macie
  - IAM Access Analyzer
  - Systems Manager
  - Firewall Manager
  - Partner solutions
- **Security standards**: CIS, PCI-DSS, AWS best practices
- **Automated remediation** with EventBridge + Lambda
- Status (November 2026): the posture-management part (security standards and controls) is now named **AWS Security Hub CSPM**; the multi-account lead account is called the **administrator account**

---

## 13. Amazon Detective

### What is Detective?
- **Analyze and investigate** security issues
- Automatically collects log data:
  - VPC Flow Logs
  - CloudTrail
  - GuardDuty findings
- **Machine learning** and **visualizations**
- Root cause analysis
- Works with GuardDuty

---

## 14. AWS Audit Manager

### What is Audit Manager?
- **Continuous auditing** for compliance
- Automated evidence collection
- **Pre-built frameworks**: HIPAA, GDPR, PCI-DSS, SOC 2
- Generate audit-ready reports

---

## 15. AWS Config

### What is AWS Config?
- Record **configuration changes** over time
- **Compliance auditing**
- **Configuration history** and **change tracking**
- Does NOT prevent changes (use Config Rules + remediation)

### AWS Config Rules
- Evaluate resource compliance
- **AWS Managed Rules** or **Custom Rules** (Lambda)
- Can trigger **auto-remediation** (SSM Automation Documents)

### Config vs CloudTrail
- **Config**: What resources look like, configuration changes
- **CloudTrail**: Who made what API call

---

## 16. AWS Systems Manager

### Session Manager
- **Secure shell access** to EC2 and on-premises servers
- **No SSH keys, bastion hosts, or ports open**
- Session logs to S3 or CloudWatch Logs
- IAM permissions for access control

### Patch Manager
- Automate patching EC2 instances and on-premises servers
- Patch on a schedule
- Compliance scanning

### Parameter Store
- (Covered earlier)

### Systems Manager Automation
- Automate common maintenance tasks
- Simplify complex tasks
- Integration with Config for remediation

---

## 17. AWS Trusted Advisor

### What is Trusted Advisor?
- **Best practice recommendations**
- Six categories:
  1. **Cost Optimization**
  2. **Performance**
  3. **Security**
  4. **Fault Tolerance**
  5. **Service Limits**
  6. **Operational Excellence**

### Trusted Advisor Checks
**Basic/Developer Support**:
- 7 core checks (S3 bucket permissions, Security Groups, IAM use, MFA on root, EBS snapshots, RDS snapshots, Service Limits)

**Business/Enterprise Support**:
- All checks
- CloudWatch integration
- Programmatic access via API

---

## Security Best Practices

### Data Protection
- Encrypt data at rest (KMS, CloudHSM)
- Encrypt data in transit (TLS/SSL)
- Use VPC endpoints for AWS services
- Enable S3 versioning and MFA Delete
- Use S3 Object Lock for compliance

### Identity and Access Management
- Use IAM roles instead of access keys
- Enable MFA for privileged users
- Implement least privilege
- Use IAM Access Analyzer
- Rotate credentials regularly

### Infrastructure Protection
- Use security groups as firewalls
- Use NACLs for subnet-level protection
- Implement WAF for web applications
- Enable AWS Shield for DDoS protection
- Use private subnets for backend resources

### Detection
- Enable CloudTrail in all regions
- Enable GuardDuty for threat detection
- Use Config for compliance monitoring
- Centralize logs in CloudWatch
- Enable VPC Flow Logs

### Incident Response
- Automate responses with EventBridge + Lambda
- Use Security Hub for centralized findings
- Implement backup and recovery strategies
- Document incident response procedures

---

## Practice Questions

1. **Which service provides single-tenant dedicated HSMs where you manage the keys entirely?**
   - A. KMS
   - B. CloudHSM
   - C. Secrets Manager
   - D. Certificate Manager
   
   **Answer**: B
   
   *(Note: Since May 2023, KMS HSMs are also FIPS 140-2/140-3 Level 3 validated. FIPS level is no longer the differentiator — single-tenancy and full key control are.)*

2. **Which AWS service automatically rotates database credentials?**
   - A. KMS
   - B. Parameter Store
   - C. Secrets Manager
   - D. IAM
   
   **Answer**: C

3. **Which service detects unauthorized deployments and cryptocurrency mining?**
   - A. Inspector
   - B. GuardDuty
   - C. Macie
   - D. Detective
   
   **Answer**: B

4. **What is the difference between Shield Standard and Shield Advanced?**
   - A. Standard is free, Advanced costs $3,000/month
   - B. Standard for CloudFront only, Advanced for all services
   - C. Standard for layer 3/4, Advanced for layer 7
   - D. No difference
   
   **Answer**: A

---

## Hands-On Labs

### Lab 1: KMS Encryption
1. Create customer managed KMS key
2. Encrypt S3 bucket with KMS
3. Upload files
4. Enable automatic key rotation
5. View CloudTrail logs for KMS operations

### Lab 2: Secrets Manager
1. Create secret for RDS database password
2. Configure automatic rotation
3. Reference secret in application
4. Test rotation

### Lab 3: GuardDuty
1. Enable GuardDuty
2. Generate sample findings
3. Create EventBridge rule for findings
4. Send notifications to SNS

### Lab 4: WAF
1. Create Web ACL
2. Add rate-based rule
3. Add geo-blocking rule
4. Attach to ALB
5. Test rules

---

## Key Takeaways

 KMS manages encryption keys (FIPS 140-3 Level 3), CloudHSM for single-tenant dedicated HSMs with full key control  
 Secrets Manager for automatic rotation of database credentials  
 Parameter Store for application configuration (cheaper than Secrets Manager)  
 WAF protects against SQL injection, XSS, rate limiting  
 Shield Standard (free) for layer 3/4, Shield Advanced ($3,000/month) for enhanced protection  
 GuardDuty for threat detection, Inspector for vulnerabilities  
 Macie for discovering sensitive data in S3  
 Security Hub centralizes security findings across services  
 Always encrypt sensitive data at rest and in transit  
 Use CloudTrail for API logging, Config for resource configuration tracking  

---

## Additional Resources

- [Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- [AWS KMS Documentation](https://docs.aws.amazon.com/kms/)
- [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/)
- [GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/)

## References

Pages this module was fact-checked against (November 2026):

- [AWS KMS request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html)
- [AWS KMS resource quotas (on-demand rotation)](https://docs.aws.amazon.com/kms/latest/developerguide/resource-limits.html)
- [AWS KMS key stores (FIPS 140-3 Level 3 HSMs)](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html)
- [What is AWS CloudHSM?](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html)
- [Secrets Manager rotation schedules](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_schedule.html)
- [ACM public certificates (198-day validity, renewal 45 days before expiry)](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html)
- [Shield Response Team (SRT) support](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html)
- [GuardDuty retired finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html)
- [GuardDuty IAM finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html)
- [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/)
- [Default SSE-C setting for new S3 buckets FAQ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-s3-c-encryption-setting-faq.html)
- [Site-to-Site VPN tunnel options (Large Bandwidth Tunnels)](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html)
- [Direct Connect MAC Security](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html)

For the full source list, see [docs/REFERENCES.md](../docs/REFERENCES.md).

---

**Previous Module**: [Module 06: Networking & Content Delivery](../06-Networking/README.md)  
**Next Module**: [Module 08: Application Integration](../08-Application-Integration/README.md)

