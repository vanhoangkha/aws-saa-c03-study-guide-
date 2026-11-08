# Module 01: AWS Fundamentals

## Overview

This module covers the foundational concepts of Amazon Web Services (AWS) that are essential for the AWS Certified Solutions Architect - Associate (SAA-C03) exam. Understanding these fundamentals is critical for designing and deploying applications on AWS.

**Exam Weight**: Not weighted separately. The SAA-C03 exam guide weights only its four domains (Secure 30%, Resilient 26%, High-Performing 24%, Cost-Optimized 20%); these fundamentals underpin all of them.

---

## Learning Objectives

By the end of this module, you will be able to:

- Explain AWS Global Infrastructure (Regions, Availability Zones, Edge Locations)
- Navigate the AWS Management Console and use AWS CLI
- Understand the AWS Well-Architected Framework's 6 pillars
- Identify AWS Shared Responsibility Model
- Describe AWS account management and billing basics
- Explain AWS service categories and when to use them

---

## Table of Contents

1. [AWS Global Infrastructure](#1-aws-global-infrastructure)
2. [AWS Management Tools](#2-aws-management-tools)
3. [AWS Well-Architected Framework](#3-aws-well-architected-framework)
4. [Shared Responsibility Model](#4-shared-responsibility-model)
5. [AWS Account Management](#5-aws-account-management)
6. [AWS Service Categories](#6-aws-service-categories)
7. [Exam Tips](#exam-tips)
8. [Practice Questions](#practice-questions)

---

## 1. AWS Global Infrastructure

### 1.1 Regions

**What is a Region?**
- A geographical area containing multiple Availability Zones
- Completely independent and isolated from other regions
- 39 Regions globally (as of late 2026; AWS adds Regions regularly)

**Key Characteristics:**
- Each region has a unique code (e.g., `us-east-1`, `eu-west-1`)
- Data doesn't leave a region unless you explicitly configure it
- Pricing varies by region
- Not all services are available in all regions

**How to Choose a Region:**
```
Consider these factors:
1. Compliance - Data sovereignty requirements
2. Proximity - Latency to end users
3. Available Services - Not all services in all regions
4. Pricing - Costs vary by region
```

**Exam Tip**: Choose the region closest to your users to minimize latency.

### 1.2 Availability Zones (AZs)

**What is an Availability Zone?**
- One or more discrete data centers within a region
- Each AZ has independent power, cooling, and networking
- Connected to other AZs via low-latency links
- Each Region has at least 3 AZs (some have more)

**Key Characteristics:**
- AZs are named: `us-east-1a`, `us-east-1b`, `us-east-1c`, etc.
- Isolated from failures in other AZs
- Enables high availability and fault tolerance
- 124 AZs globally (as of late 2026)

**Multi-AZ Deployment Pattern:**
```
Region: us-east-1
├── AZ: us-east-1a
│   ├── Application Server 1
│   └── Database Primary
├── AZ: us-east-1b
│   ├── Application Server 2
│   └── Database Standby
└── AZ: us-east-1c
    └── Application Server 3
```

**Exam Tip**: Always deploy across multiple AZs for high availability.

### 1.3 Edge Locations

**What is an Edge Location?**
- Endpoints for AWS services like CloudFront and Route 53
- Used to cache content closer to end users
- CloudFront has 750+ points of presence (PoPs) plus 15 Regional edge caches (far more than Regions)
- Part of the AWS Global Network

**Use Cases:**
- Content Delivery Network (CloudFront)
- DNS service (Route 53)
- AWS WAF and Shield
- Lambda@Edge

**Exam Tip**: Edge Locations ≠ Regions. They're for caching and low-latency access.

### 1.4 Local Zones

**What is a Local Zone?**
- Extension of an AWS region closer to large population centers
- Provides single-digit millisecond latency to end users
- Useful for latency-sensitive applications

**Example:** Los Angeles Local Zone extends `us-west-2` region

### 1.5 Wavelength Zones

**What is a Wavelength Zone?**
- AWS infrastructure embedded within telecom providers' 5G networks
- Enables ultra-low latency for mobile and edge devices
- Use cases: AR/VR, real-time gaming, autonomous vehicles

---

## 2. AWS Management Tools

### 2.1 AWS Management Console

**Web-Based Interface:**
- Visual, point-and-click interface
- Accessible at: https://console.aws.amazon.com
- Best for: Learning, exploration, one-time tasks

**Key Features:**
- Service search and favorites
- Recently visited services
- Resource groups
- Cost and usage dashboards

### 2.2 AWS Command Line Interface (CLI)

**Command-Line Tool:**
```bash
# Install AWS CLI version 2 with the official installer for your OS
# (see the AWS CLI User Guide: "Installing or updating to the latest version")

# Configure credentials
aws configure

# Example: List S3 buckets
aws s3 ls

# Example: Launch EC2 instance
aws ec2 run-instances --image-id ami-12345678 --instance-type t2.micro
```

**Use Cases:**
- Automation and scripting
- Batch operations
- Integration with CI/CD pipelines

### 2.3 AWS SDKs (Software Development Kits)

> Note: "AWS Tools and SDKs" are listed as out of scope in the SAA-C03 exam guide.

**Programming Languages Supported:**
- Python (Boto3)
- JavaScript/Node.js
- Java
- .NET
- Ruby
- PHP
- Go

**Example (Python):**
```python
import boto3

# Create S3 client
s3 = boto3.client('s3')

# List buckets
response = s3.list_buckets()
```

### 2.4 AWS CloudFormation

**Infrastructure as Code (IaC):**
- Define infrastructure in JSON or YAML templates
- Version control your infrastructure
- Repeatable deployments
- Automatic rollback on errors

**Example Template:**
```yaml
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: my-unique-bucket-name
```

### 2.5 AWS CloudShell

> Note: AWS CloudShell is listed as out of scope in the SAA-C03 exam guide.

**Browser-Based Shell:**
- Pre-configured with AWS CLI and tools
- No installation required
- 1 GB of storage per region
- Automatically authenticated with your console credentials

---

## 3. AWS Well-Architected Framework

### 3.1 Overview

The AWS Well-Architected Framework helps you understand best practices for designing and operating reliable, secure, efficient, and cost-effective systems in the cloud.

**6 Pillars: CROPSS (Mnemonic: "CROPS + Security")**

### 3.2 Operational Excellence

**Design Principles:**
- Organize teams around business outcomes
- Implement observability for actionable insights
- Safely automate where possible (operations as code)
- Make frequent, small, reversible changes
- Refine operations procedures frequently
- Anticipate failure
- Learn from all operational events and metrics
- Use managed services

**Key Services:**
- AWS CloudFormation
- AWS Config
- AWS CloudTrail
- Amazon CloudWatch

**Questions to Ask:**
- How do you determine your operational priorities?
- How do you design your workload for operational excellence?

### 3.3 Security

**Design Principles:**
- Implement strong identity foundation
- Enable traceability
- Apply security at all layers
- Automate security best practices
- Protect data in transit and at rest
- Keep people away from data
- Prepare for security events

**Key Services:**
- AWS IAM
- AWS KMS
- AWS WAF
- AWS Shield
- Amazon GuardDuty

**Questions to Ask:**
- How do you securely operate your workload?
- How do you manage identities and permissions?

### 3.4 Reliability

**Design Principles:**
- Automatically recover from failure
- Test recovery procedures
- Scale horizontally
- Stop guessing capacity
- Manage change through automation

**Key Services:**
- Amazon Route 53
- Elastic Load Balancing
- Auto Scaling
- Amazon RDS Multi-AZ

**Questions to Ask:**
- How do you design your workload to adapt to changes in demand?
- How do you implement your workload to withstand component failures?

### 3.5 Performance Efficiency

**Design Principles:**
- Democratize advanced technologies
- Go global in minutes
- Use serverless architectures
- Experiment more often
- Consider mechanical sympathy

**Key Services:**
- AWS Lambda
- Amazon CloudFront
- Amazon ElastiCache
- Amazon RDS Read Replicas

**Questions to Ask:**
- How do you select appropriate resource types and sizes?
- How do you monitor your resources to ensure performance?

### 3.6 Cost Optimization

**Design Principles:**
- Implement cloud financial management
- Adopt a consumption model
- Measure overall efficiency
- Stop spending on undifferentiated heavy lifting
- Analyze and attribute expenditure

**Key Services:**
- AWS Cost Explorer
- AWS Budgets
- Reserved Instances
- Savings Plans
- AWS Trusted Advisor

**Questions to Ask:**
- How do you govern usage?
- How do you monitor usage and cost?

### 3.7 Sustainability

**Design Principles:**
- Understand your impact
- Establish sustainability goals
- Maximize utilization
- Anticipate and adopt new, more efficient offerings
- Use managed services
- Reduce downstream impact

**Key Services:**
- EC2 Auto Scaling
- Serverless services
- AWS Graviton processors

**Exam Tip**: Know the 6 pillars by heart. Use mnemonic: **"CROPSS"** or **"SCROPP"**

---

## 4. Shared Responsibility Model

### 4.1 Concept

**"Security OF the cloud vs. Security IN the cloud"**

```
┌─────────────────────────────────────────────┐
│          CUSTOMER RESPONSIBILITY            │
│         "Security IN the Cloud"             │
├─────────────────────────────────────────────┤
│ • Customer Data                             │
│ • Platform, Applications, IAM               │
│ • Operating System, Network, Firewall       │
│ • Client-Side Encryption & Authentication   │
│ • Server-Side Encryption (File System/Data)│
│ • Network Traffic Protection                │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│            AWS RESPONSIBILITY               │
│         "Security OF the Cloud"             │
├─────────────────────────────────────────────┤
│ • Hardware / AWS Global Infrastructure      │
│ • Regions, AZs, Edge Locations             │
│ • Compute, Storage, Database, Networking    │
│ • Software (Hypervisor, Host OS)           │
│ • Physical Security of Data Centers         │
└─────────────────────────────────────────────┘
```

### 4.2 Examples by Service Type

**IaaS (EC2):**
- **AWS**: Physical hardware, hypervisor
- **Customer**: OS patches, security groups, data encryption

**PaaS (RDS):**
- **AWS**: OS patches, database patching, backups
- **Customer**: Database credentials, network access, data encryption

**Abstracted services (S3, DynamoDB):**
- **AWS**: Infrastructure, software, physical security
- **Customer**: Data classification, bucket policies, encryption

**Exam Tip**: If you can configure it, you're responsible for it.

---

## 5. AWS Account Management

### 5.1 AWS Account Basics

**Root User:**
- Created when AWS account is created
- Has complete access to all resources
- **NEVER use for everyday tasks**
- Enable MFA immediately (AWS now enforces MFA for the root user of all account types)

**Best Practices:**
- Use federation through IAM Identity Center (temporary credentials) for daily human access, not long-term IAM users
- Enable MFA on root account
- Use strong password
- Don't share root credentials
- Delete root access keys

### 5.2 AWS Organizations

**What is AWS Organizations?**
- **Centrally manage multiple AWS accounts**
- Consolidated billing across all accounts
- Hierarchical account structure with Organizational Units (OUs)
- Automate account creation
- Apply policies across accounts

**Key Benefits:**
- **Consolidated Billing**: Single payment method, volume discounts
- **Centralized Management**: Control access and security policies
- **Service Control Policies (SCPs)**: Set permission guardrails
- **Account Automation**: Programmatic account creation
- **Cost Allocation**: Tag-based cost tracking across accounts

#### AWS Organizations Structure

```
Root (Organization)
│
├── Management Account (Master Account)
│   └── Pays all charges, full admin access
│
├── Production OU
│   ├── Prod-App Account
│   ├── Prod-DB Account
│   └── Prod-Network Account
│
├── Development OU
│   ├── Dev Account 1
│   ├── Dev Account 2
│   └── Test Account
│
├── Security OU
│   ├── Security Audit Account
│   └── Log Archive Account
│
└── Sandbox OU
    ├── Sandbox 1
    └── Sandbox 2
```

**Organizational Unit (OU) Best Practices:**
- Group accounts by function (Production, Development, Security)
- Nest OUs up to 5 levels deep
- Apply different policies to different OUs
- Use meaningful names for easy management

#### Service Control Policies (SCPs)

**What are SCPs?**
- JSON policies that define **maximum permissions** for accounts
- Act as **guardrails** (don't grant permissions, only limit them)
- Applied at: Organization Root, OU, or individual Account level
- Inherited down the OU hierarchy

**Important SCP Rules:**
- SCPs **DO NOT** affect the Management Account
- SCPs **DO NOT** grant permissions (only restrict)
- SCPs **DO NOT** affect service-linked roles
- Yes: SCPs apply to all IAM users and roles in member accounts, including the member account root user
- Yes: Effective permissions = IAM permissions AND SCP permissions (an action must be allowed by the SCPs at every level: root, each OU, and the account)

**SCP Example 1: Deny All Actions Outside us-east-1**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAllOutsideUSEast1",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
```

**SCP Example 2: Require Encryption for EBS Volumes**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyUnencryptedEBS",
      "Effect": "Deny",
      "Action": [
        "ec2:CreateVolume",
        "ec2:RunInstances"
      ],
      "Resource": "*",
      "Condition": {
        "Bool": {
          "ec2:Encrypted": "false"
        }
      }
    }
  ]
}
```

**SCP Example 3: Prevent Users from Leaving Organization**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "organizations:LeaveOrganization",
      "Resource": "*"
    }
  ]
}
```

**Common SCP Use Cases:**
- Restrict services to specific regions (data sovereignty)
- Enforce encryption requirements
- Prevent deletion of CloudTrail logs
- Restrict instance types to approved list
- Deny public S3 buckets
- Prevent leaving the organization

**SCP Evaluation Logic:**
```
User attempts action
    ↓
Is there an explicit Deny in SCP? → YES → DENY
    ↓ NO
Allowed by SCPs at every level? → YES → Check IAM Policy
    ↓ NO                                      ↓
 DENY (implicit)                    Is there Allow in IAM? → YES → ALLOW
                                            ↓ NO
                                         DENY
```

**Exam Tip**: Remember: SCPs affect ALL users and roles in member accounts, but NOT the management account.

#### AWS Control Tower

**What is AWS Control Tower?**
- **Easy way to set up and govern multi-account AWS environments**
- Built on top of AWS Organizations
- Automated account provisioning
- Pre-configured controls (formerly called guardrails): SCPs/RCPs, AWS Config rules, CloudFormation hooks
- Dashboard for compliance monitoring

**Key Features:**
- **Landing Zone**: Well-architected multi-account baseline
- **Controls (guardrails)**: Preventive (SCPs, RCPs, declarative policies), detective (AWS Config rules), and proactive (CloudFormation hooks)
- **Account Factory**: Automated account provisioning
- **Dashboard**: Centralized visibility and compliance

**Control Tower Controls (guidance levels):**

**Mandatory controls** (always enabled, cannot be deactivated):
- Disallow deletion of log archive
- Disallow changes to the Log Archive S3 bucket policy, encryption, logging and lifecycle configuration
- Enable AWS Config in all available Regions; disallow configuration changes to AWS Config

**Strongly recommended controls** (optional):
- Detect whether MFA for the root user is enabled
- Detect whether encryption is enabled for EBS volumes attached to EC2 instances
- Detect whether public read/write access to S3 buckets is allowed
- Detect whether unrestricted SSH from the internet is allowed

**Elective controls** (optional):
- Disallow internet access for a customer-managed VPC
- Disallow delete actions on S3 buckets without MFA
- Detect whether MFA is enabled for IAM users

**Control Tower vs Organizations:**
| Feature | Organizations | Control Tower |
|---------|---------------|---------------|
| Setup Complexity | Manual | Automated |
| Controls (guardrails) | Manual SCPs/RCPs | Pre-built + custom |
| Account Provisioning | Manual | Account Factory |
| Compliance Dashboard | No | Yes |
| Use Case | Full control | Quick setup with best practices |

**When to Use:**
- **Control Tower**: Quick setup, governance out-of-the-box, less AWS experience
- **Organizations**: Maximum flexibility, custom policies, experienced teams

#### AWS Resource Access Manager (RAM)

**What is AWS RAM?**
- **Share AWS resources across accounts** without duplicating them
- Share within your Organization or with specific accounts
- No additional charge for using RAM
- Centralized resource management

**Shareable Resources:**
- **VPC Subnets**: Share subnets with other accounts (common use case)
- **Transit Gateway**: Share transit gateway attachments
- **Route 53 Resolver**: Share DNS query resolution rules
- **License Manager**: Share software licenses
- **Aurora DB Clusters**: Share Aurora DB clusters
- **Resource Groups**: Share resource groups
- **Capacity Reservations**: Share EC2 capacity reservations
- **Dedicated Hosts**: Share dedicated hosts
- **Prefix Lists**: Share managed prefix lists

**Common Use Case: VPC Subnet Sharing**
```
Account A (Networking Account)
└── VPC (10.0.0.0/16)
    ├── Private Subnet 1 (shared via RAM)
    └── Private Subnet 2 (shared via RAM)
        ↓
        RAM Resource Share
        ↓
Account B (Application Account)
└── EC2 instances launch in Account A's subnets
    (but owned by Account B)
```

**Benefits of Subnet Sharing:**
- Centralized network management
- Reduced number of VPCs
- Simplified network architecture
- Lower operational overhead
- Efficient use of IP addresses

**RAM Sharing Process:**
1. Resource owner creates a resource share
2. Specify which resources to share
3. Specify which accounts/OUs can access
4. Recipients accept the invitation (only when sharing outside your organization, or if sharing with AWS Organizations is not enabled)
5. Recipients can use resources (but not modify/delete)

**Exam Tip**: RAM is commonly tested with VPC subnet sharing scenarios for centralized networking.

#### Consolidated Billing

**How Consolidated Billing Works:**
- Single payment method for all accounts in Organization
- Management account pays all charges
- Member accounts cannot change billing settings
- Combined usage for volume discounts

**Volume Discount Benefits** (example from the AWS Billing docs, illustrative rates):
```
Account 1: Transfers 8 TB of data
Account 2: Transfers 4 TB of data
Combined: 12 TB → first 10 TB billed at the tier-1 rate,
          the remaining 2 TB at the cheaper tier-2 rate
(Billed separately, each account would pay the tier-1 rate for all of its usage)
```

**Cost Allocation Tags:**
- Tag resources across accounts
- Track costs by project, department, environment
- Generate detailed cost reports
- Examples: `Project:WebApp`, `Environment:Production`, `CostCenter:Engineering`

### 5.3 Billing and Cost Management

**Key Services:**
- **AWS Budgets**: Set custom budgets and alerts
- **Cost Explorer**: Visualize and analyze costs
- **Cost and Usage Report**: Detailed cost data
- **AWS Cost Anomaly Detection**: ML-powered cost anomaly alerts

**Free Tier:**
- New accounts (created on or after 15 July 2025): USD $100 in credits at sign-up, plus up to $100 more earned through activities
- Free account plan lasts up to 6 months or until credits are used; upgrade to a paid plan for production
- Always free services (30+ services with monthly free limits, e.g. Lambda, DynamoDB)
- Accounts created before 15 July 2025 keep the older 12-month free tier offers

---

## 6. AWS Service Categories

### 6.1 Compute

- **EC2**: Virtual servers
- **Lambda**: Serverless functions
- **ECS/EKS**: Containers
- **Elastic Beanstalk**: PaaS

### 6.2 Storage

- **S3**: Object storage
- **EBS**: Block storage for EC2
- **EFS**: File storage
- **Glacier**: Archive storage

### 6.3 Database

- **RDS**: Managed relational databases
- **DynamoDB**: NoSQL database
- **Aurora**: High-performance relational
- **Redshift**: Data warehouse

### 6.4 Networking

- **VPC**: Virtual network
- **Route 53**: DNS service
- **CloudFront**: CDN
- **Direct Connect**: Dedicated connection

### 6.5 Security & Identity

- **IAM**: Identity and access management
- **KMS**: Key management
- **WAF**: Web application firewall
- **GuardDuty**: Threat detection

### 6.6 Management & Monitoring

- **CloudWatch**: Monitoring and logging
- **CloudTrail**: API auditing
- **Config**: Resource inventory and compliance
- **Systems Manager**: Operations hub

---

## Exam Tips

### Must Know for Exam

1. **Regions and AZs:**
   - At least 3 AZs per Region
   - Deploy across multiple AZs for HA
   - Choose region based on: compliance, latency, cost, services

2. **Well-Architected Framework:**
   - Know all 6 pillars: CROPSS
   - Understand design principles
   - Know key services for each pillar

3. **Shared Responsibility:**
   - AWS = Security OF the cloud
   - Customer = Security IN the cloud
   - Varies by service type (IaaS vs PaaS vs SaaS)

4. **Management Tools:**
   - Console = GUI
   - CLI = Automation
   - SDK = Programming
   - CloudFormation = Infrastructure as Code

### Common Exam Scenarios

**Scenario 1**: *"A company needs to ensure their application remains available even if an entire data center fails."*
- **Answer**: Deploy across multiple Availability Zones

**Scenario 2**: *"Who is responsible for patching the operating system on an EC2 instance?"*
- **Answer**: Customer (it's IaaS - you manage the OS)

**Scenario 3**: *"A company wants to reduce latency for users in Europe accessing content from us-east-1."*
- **Answer**: Use CloudFront (Edge Locations)

### Exam Keywords Mapping

| Keyword | Think This |
|---------|------------|
| "High Availability" | Multi-AZ deployment |
| "Disaster Recovery" | Multi-Region |
| "Low Latency" | Edge Locations, CloudFront |
| "Compliance" | Choose specific Region |
| "Infrastructure as Code" | CloudFormation |
| "Security OF cloud" | AWS responsibility |
| "Security IN cloud" | Customer responsibility |

---

## Practice Questions

### Question 1
**Which of the following is an AWS responsibility under the Shared Responsibility Model?**

A) Patching the operating system on EC2 instances  
B) Encrypting data stored in S3 buckets  
C) Physical security of data centers  
D) Configuring security groups

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation**: Physical security of data centers is AWS's responsibility ("Security OF the cloud"). Options A, B, and D are customer responsibilities ("Security IN the cloud").
</details>

### Question 2
**A company wants to deploy a web application that must remain available even if an entire AWS data center becomes unavailable. What should they do?**

A) Deploy the application in multiple Regions  
B) Deploy the application across multiple Availability Zones  
C) Deploy the application using multiple Edge Locations  
D) Use AWS CloudFormation for deployment

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation**: Deploying across multiple Availability Zones within a region ensures the application remains available even if one AZ (data center) fails. Multi-Region (A) would be for disaster recovery across regions. Edge Locations (C) are for content delivery. CloudFormation (D) is for infrastructure as code.
</details>

### Question 3
**Which pillar of the AWS Well-Architected Framework focuses on the ability to recover from failures and dynamically acquire resources to meet demand?**

A) Operational Excellence  
B) Security  
C) Reliability  
D) Performance Efficiency

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation**: Reliability pillar focuses on the ability to recover from failures and dynamically acquire computing resources to meet demand.
</details>

### Question 4
**What is the minimum number of Availability Zones in an AWS Region?**

A) 1  
B) 2  
C) 3  
D) 4

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation**: AWS states that each Region consists of at least three isolated, physically separate Availability Zones; some Regions have more.
</details>

### Question 5
**A solutions architect needs to ensure that users in Asia experience low latency when accessing static web content hosted in us-east-1. What should they use?**

A) Deploy the application in ap-southeast-1 region  
B) Use Amazon CloudFront  
C) Create a VPC in Asia  
D) Use Route 53 geoproximity routing

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation**: CloudFront uses Edge Locations globally to cache content closer to users, reducing latency. This is more cost-effective than deploying in multiple regions (A) for static content.
</details>

---

## Additional Resources

### AWS Official Documentation
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html)

### Hands-On Labs
1. **Explore AWS Regions and AZs**: Navigate the console and identify available regions
2. **Set Up AWS CLI**: Configure CLI on your local machine
3. **Create CloudFormation Stack**: Deploy a simple S3 bucket using IaC
4. **Enable MFA**: Enable multi-factor authentication on your AWS account

### Next Steps
- Complete this module
- **Next**: [Module 02: Identity and Access Management (IAM)](../02-IAM/README.md)
- **Related**: [Quick Reference](../docs/reference/QUICK-REFERENCE.md) for service comparisons

---

**Module Progress**: Foundation Complete  
**Estimated Study Time**: 4-6 hours  
**Difficulty**: 1/3 Beginner

---

[Back to Main README](../README.md) | [Next Module: IAM ](../02-IAM/README.md)

## References

Pages verified for the fact-check of this module (November 2026):
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) (Region and AZ counts, minimum of three AZs per Region)
- [Amazon CloudFront features](https://aws.amazon.com/cloudfront/features/) (points of presence and Regional edge caches)
- [AWS Local Zones: available Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html)
- [Installing or updating the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [AWS CloudShell concepts](https://docs.aws.amazon.com/cloudshell/latest/userguide/working-with-aws-cloudshell.html) (1 GB persistent storage per Region)
- [Well-Architected: Operational Excellence design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html)
- [Performance Efficiency Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)
- [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [AWS Organizations FAQs](https://aws.amazon.com/organizations/faqs/) (OU nesting depth)
- [AWS Control Tower: how controls work](https://docs.aws.amazon.com/controltower/latest/userguide/how-controls-work.html), [Mandatory controls](https://docs.aws.amazon.com/controltower/latest/controlreference/mandatory-controls.html), [Strongly recommended detective controls](https://docs.aws.amazon.com/controltower/latest/controlreference/strongly-recommended-detective-controls.html), [Elective preventive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/elective-preventive-controls.html)
- [AWS RAM: sharing your resources](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html)
- [Consolidated billing: volume discounts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/useconsolidatedbilling-effective.html)
- [AWS Free Tier](https://aws.amazon.com/free/) and [Free Tier start and expiry (re:Post Knowledge Center)](https://repost.aws/knowledge-center/aws-free-tier-account-start-expire)
- [AWS Support plan pricing](https://aws.amazon.com/premiumsupport/pricing/) and [Developer, Business, and Enterprise On-Ramp end of support](https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html)
- [Multi-factor authentication in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) (root user MFA enforcement)
- [QuickSight evolves to Amazon Quick Suite (AWS Business Intelligence Blog)](https://aws.amazon.com/blogs/business-intelligence/reimagine-business-intelligence-amazon-quicksight-evolves-to-amazon-quick-suite)
