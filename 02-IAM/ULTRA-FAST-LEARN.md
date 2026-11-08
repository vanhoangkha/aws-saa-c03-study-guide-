# 02: IAM - Ultra Fast Learning

## IAM Basics
- **Free service**, global (not regional)
- **Authentication**: WHO (users, roles)
- **Authorization**: WHAT (policies)
- **No default access**: Implicit DENY by default

## IAM Entities

### Users
- Permanent named operator (person or app)
- Max **5,000 users** per account
- Can belong to **max 10 groups**
- Access: Console password + Access Keys (CLI/SDK)

### Groups
- Collection of users
- **CANNOT nest groups**
- Attach policies to groups
- Users inherit group policies

### Roles
- **Temporary credentials** for services/users
- No long-term credentials (no password/access keys)
- **AssumeRole** to use
- Use cases: EC2 accessing S3, cross-account access

## IAM Policies

### Policy Structure (JSON)
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow/Deny",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::bucket/*",
    "Condition": {}
  }]
}
```

### Policy Types
1. **AWS Managed**: Created/maintained by AWS, can't edit
2. **Customer Managed**: You create, full control, reusable
3. **Inline**: Direct to user/group/role, 1:1 relationship, deleted with entity

### Policy Evaluation
- **Explicit DENY** always wins
- **Default**: Implicit deny
- Order: Explicit Deny > Explicit Allow > Implicit Deny

## Security Best Practices
- Enable **MFA** on root account
- **Never use root** for daily tasks
- Use **federation** (IAM Identity Center) with temporary credentials for human users; never share credentials
- Use **groups** to assign permissions
- **Least privilege** principle
- **Rotate credentials** regularly
- Use **roles** for EC2 instances (not access keys)
- Enable **CloudTrail** for audit logging

## MFA Options
- **Virtual MFA**: Google Authenticator, Authy
- **Passkey / FIDO2 security key** (formerly "U2F"): YubiKey, synced passkeys; phishing-resistant, AWS-recommended
- **Hardware TOTP token**: Thales
- **Hardware TOTP token for GovCloud**: Hypersecu
- Up to 8 MFA devices per user; SMS MFA no longer supported

## Identity Federation
- **SAML 2.0**: Corporate login (AD, ADFS)
- **Web Identity**: Google, Facebook, Amazon
- **Cognito**: Mobile/web apps, social/enterprise identity
- **IAM Identity Center** (formerly AWS SSO): Centralized access to multiple accounts

## IAM Credentials Report
- Lists all users and credential status
- **Account-level** report
- Use for **compliance auditing**

## IAM Access Advisor
- Shows service permissions granted and when they were last accessed
- Available for IAM users, groups, roles and policies (and Organizations entities)
- Use for **least privilege** implementation

## Quick Exam Tips
- **Root user**: Lock it, enable MFA, don't use
- **Roles > Access Keys**: Always use roles for EC2
- **Policy size limit**: inline total per entity 2,048 characters (user), 5,120 (group), 10,240 (role); each managed policy 6,144 characters
- **Managed policies attached**: 10 per user (up to 20), 10 per group, 20 per role (up to 25)
- **Password policy**: Enforce complexity, rotation
- **Access Keys**: Max 2 per user
- **Cross-account**: Use roles, or resource-based policies on services that support them (for example S3, SNS, SQS, KMS, Lambda)
- **Permission boundary**: Max permissions user can have
- **SCP > IAM Policy**: SCPs restrict even admin access

