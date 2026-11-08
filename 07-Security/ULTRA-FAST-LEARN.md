# 07: Security & Compliance - Ultra Fast Learning

## KMS (Key Management Service)

### KMS Basics
- **Managed encryption** service
- **Regional** service
- **FIPS 140-3 Level 3** validated HSMs (Level 3 overall since May 2023)
- Audit with CloudTrail
- **$1/month** per customer managed key

### Key Types
- **Symmetric (AES-256)**: Single key, never see key, most common
- **Asymmetric (RSA/ECC)**: Public/private key pair, download public key

### KMS Keys
- **AWS Managed**: Free, auto-rotate yearly, `aws/service-name`
- **Customer Managed**: $1/month, optional auto-rotate (90-2,560 days, default 365) or on-demand, full control
- **AWS Owned**: Free, used by AWS services, no visibility

### KMS Operations
- **Encrypt**: <4 KB data
- **Decrypt**: Decrypt ciphertext
- **GenerateDataKey**: For envelope encryption (>4 KB)
- **Key Policies**: Control access (must exist, default allows root)

### Envelope Encryption
1. KMS generates Data Encryption Key (DEK)
2. Encrypt data with DEK
3. Encrypt DEK with KMS key
4. Store encrypted data + encrypted DEK

## Secrets Manager
- Store **secrets** (passwords, API keys)
- **Auto-rotation** (Lambda function)
- Integration with RDS (auto-rotate DB passwords)
- **$0.40/secret/month + $0.05/10K API calls**

### Secrets Manager vs Parameter Store
| Feature | Secrets Manager | Parameter Store |
|---------|-----------------|-----------------|
| Auto-rotation | Yes | No |
| RDS integration | Yes | No |
| Cost | $0.40/secret | Free (standard) |
| Max size | 64 KB | 4 KB (standard), 8 KB (advanced) |
| Use case | Secrets with rotation | Config, parameters |

## Parameter Store
- Store **configuration** and secrets
- **Free** (standard tier)
- **Hierarchical** structure
- **Integration** with CloudFormation, Lambda
- **SecureString**: Encrypted with KMS

## CloudHSM
- **FIPS 140-2 or 140-3 Level 3** depending on HSM type (KMS is also Level 3 now; the key difference is single-tenancy)
- **Dedicated hardware** (not multi-tenant)
- **You manage keys** (AWS manages hardware)
- **Single-tenant**, deployed in VPC
- **Use case**: Regulations or contracts that require a single-tenant HSM under your exclusive control

## Certificate Manager (ACM)
- Provision, manage, deploy **SSL/TLS certificates**
- **Free** for AWS services
- **Auto-renewal**
- Works with: ALB, NLB, CloudFront, API Gateway
- **Export**: Only exportable public certificates (paid option, since June 2025) and private CA certificates can be exported with their private key; standard public certificates cannot

## WAF (Web Application Firewall)
- Protect against **web exploits** (Layer 7)
- **Rules**: IP addresses, HTTP headers, body, URI strings
- **Rate-based rules**: DDoS protection
- **Deploy on**: ALB, API Gateway, CloudFront, AppSync
- **Web ACL**: Collection of rules

### WAF Rule Types
- **IP Set**: Block/allow IPs
- **Geo Match**: Block countries
- **Size Constraint**: Request size
- **SQL Injection**: Detect SQL injection
- **XSS**: Cross-site scripting
- **Rate-based**: Limit requests (e.g., 2000/5 min)

## Shield
- **DDoS protection**
- **Shield Standard**: Free, automatic, network/transport layer
- **Shield Advanced**: $3K/month, enhanced protection, Shield Response Team (SRT), cost protection

## GuardDuty
- **Threat detection** using ML
- Analyzes: CloudTrail, VPC Flow Logs, DNS logs
- **Findings**: Unusual API calls, compromised instances, reconnaissance
- **30-day free trial**
- Can trigger Lambda/SNS for automated response

## Inspector
- **Automated security assessment**
- **EC2**: Package vulnerabilities + network reachability (SSM Agent, or agentless EBS snapshot scans in hybrid mode)
- **ECR**: Container image scanning
- **Lambda**: Code and dependencies
- Findings with severity, remediation

## Macie
- **Data security** service using ML
- Discover and protect **sensitive data** in S3 (PII, credentials)
- **Findings**: Sensitive data detected
- Integration with EventBridge for automation

## Config
- **Audit and compliance** of AWS resources
- Record **configuration changes** over time
- **Rules**: Evaluate compliance (AWS managed or custom)
- **Remediation**: Auto-fix non-compliant resources (SSM Automation)
- **Not free**: Pay per config item + rule evaluation

## CloudTrail
- **API audit logging**
- **Who, what, when, where** (user, action, time, IP)
- **90 days** in Event History (free)
- **Long-term**: Send to S3 or CloudWatch Logs
- **Management events**: First copy delivered to S3 is free (control plane)
- **Data events**: Paid (data plane, e.g., S3 GetObject)
- **Insights**: Detect unusual activity

### CloudTrail vs CloudWatch vs Config
| Service | Purpose |
|---------|---------|
| CloudTrail | WHO did WHAT (API calls) |
| CloudWatch | Performance metrics, logs |
| Config | Resource configuration changes, compliance |

## Detective
- **Security investigation** using ML
- Analyze and visualize security data
- Root cause analysis
- Uses: VPC Flow Logs, CloudTrail, GuardDuty

## Security Hub
- **Central security dashboard**
- Aggregates findings from GuardDuty, Inspector, Macie, etc.
- **Compliance checks**: CIS, PCI-DSS
- Automated remediation with EventBridge

## Firewall Manager
- **Centrally manage firewall rules** across accounts
- Works with: WAF, Shield Advanced, Security Groups, Network Firewall
- Requires **AWS Organizations**

## Quick Exam Tips
- **KMS**: Regional, $1/month, <4 KB encryption
- **Envelope Encryption**: For >4 KB data
- **CloudHSM**: Level 3, dedicated hardware, single-tenant
- **Secrets Manager**: Auto-rotation, $0.40/secret
- **Parameter Store**: Free config storage
- **ACM**: Free SSL/TLS certificates
- **WAF**: Layer 7 protection, rate-based rules
- **Shield Standard**: Free DDoS protection
- **Shield Advanced**: $3K/month, enhanced protection
- **GuardDuty**: Threat detection using ML
- **Inspector**: Security assessment (EC2, ECR, Lambda)
- **Macie**: Find PII/sensitive data in S3
- **Config**: Compliance auditing, remediation
- **CloudTrail**: API logging, 90 days free
- **Security Hub**: Central security dashboard

