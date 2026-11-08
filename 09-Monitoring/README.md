# Module 09: Monitoring & Management

## Overview
Monitoring and management services help you track performance, detect issues, and maintain compliance. This module covers CloudWatch, CloudTrail, Config, and Systems Manager.

## Learning Objectives
- Monitor applications with CloudWatch
- Track API calls with CloudTrail
- Ensure compliance with AWS Config
- Manage resources with Systems Manager
- Optimize performance with Trusted Advisor

---

## 1. Amazon CloudWatch

### What is CloudWatch?
- **Monitoring and observability** service
- Collect and track **metrics**
- Collect and monitor **log files**
- Set **alarms** and automate actions
- Visualize with **dashboards**

### CloudWatch Metrics

**AWS Service Metrics (Automatic)**
- EC2: CPU, Network, Disk, Status Checks
- EBS: Read/Write operations
- S3: Bucket metrics
- RDS: Database connections, CPU
- Lambda: Invocations, duration, errors
- **Default monitoring**: 5-minute intervals
- **Detailed monitoring**: 1-minute intervals (extra cost)

**Custom Metrics**
- Push your own metrics using PutMetricData API
- **Standard resolution**: 1-minute intervals
- **High resolution**: 1-second intervals
- Examples: Application metrics, business metrics

**EC2 Memory Metrics**
- **NOT included by default** (only CPU, network, disk)
- Must install **CloudWatch Agent** to send memory metrics

### CloudWatch Alarms

**Alarm States**
- **OK**: Within threshold
- **ALARM**: Breached threshold
- **INSUFFICIENT_DATA**: Not enough data

**Alarm Actions**
- **Auto Scaling**: Scale EC2 instances
- **EC2 Actions**: Stop, terminate, reboot, recover
- **SNS**: Send notifications
- **Lambda**: Invoke a function directly
- **Systems Manager**: Create an OpsItem or incident

**Composite Alarms**
- Combine multiple alarms with AND/OR logic
- Reduce alarm noise

### CloudWatch Logs

**Log Groups**: Collection of log streams (e.g., /aws/lambda/my-function)  
**Log Streams**: Sequence of log events (e.g., instance ID)  
**Log Events**: Individual log entries with timestamp  

**Log Sources**
- **SDK**: Application logs
- **CloudWatch Logs Agent**: EC2, on-premises
- **Elastic Beanstalk**: Application logs
- **ECS**: Container logs
- **Lambda**: Function logs
- **VPC Flow Logs**: Network traffic
- **API Gateway**: API request logs
- **CloudTrail**: API calls (with filter)
- **Route 53**: DNS queries

**Retention**
- **1 day** to **10 years**, or never expire
- Default: Never expire
- Can export to S3

**CloudWatch Logs Insights**
- **Query and analyze** log data
- Purpose-built query language
- Example: Find errors, count events, percentiles

**Metric Filters**
- Create metrics from log data
- Example: Count occurrences of "ERROR"
- Trigger alarms based on log patterns

**Log Subscriptions**
- Real-time log processing
- Destinations:
  - **Kinesis Data Streams**: Real-time processing
  - **Amazon Data Firehose** (formerly Kinesis Data Firehose): S3, Redshift, OpenSearch
  - **Lambda**: Custom processing
  - **Amazon OpenSearch Service**: Search and analytics
- Cross-account subscriptions supported

### CloudWatch Agent
- **Collect logs and metrics** from EC2 and on-premises
- System-level metrics (memory, disk usage, processes)
- **SSM Parameter Store** for centralized config
- **Unified Agent**: Metrics + Logs

### CloudWatch Dashboards
- **Visualize metrics** and logs
- **Global view**: Cross-region, cross-account
- **Automatic dashboards**: Service-specific (EC2, Lambda, etc.)
- Can add graphs, numbers, text widgets
- **Pricing**: 3 dashboards (up to 50 metrics) free, then $3/dashboard/month

### CloudWatch Events (now EventBridge)
- See Module 08: EventBridge
- Schedule cron jobs
- React to AWS service events

---

## 2. AWS CloudTrail

### What is CloudTrail?
- **Governance, compliance, audit** service
- **Record API calls** made in AWS account
- **Who, what, when, where**
- Enabled by default (90-day history)

### CloudTrail Events

**Management Events**
- Operations on AWS resources
- Examples: Creating EC2, modifying security groups, attaching IAM policy
- **Read Events**: Read operations (List, Describe, Get)
- **Write Events**: Modify operations (Create, Delete, Update)
- **Enabled by default**

**Data Events**
- Resource operations within a resource
- Examples: S3 object-level operations, Lambda invocations
- **High volume** (disabled by default)
- Can log: S3 object operations, Lambda executions

**Insights Events**
- Detect **unusual activity**
- Uses machine learning
- Examples: Burst of IAM actions, spike in resource provisioning
- **Paid feature**

### CloudTrail Features

**Trails**
- Configure which events to log
- Deliver to **S3 bucket** (encrypted)
- Optional: Send to **CloudWatch Logs**
- **Multi-region** or **single-region**
- **Organization trail**: All accounts in AWS Organizations

**Log File Integrity Validation**
- Ensure logs not modified
- Uses digital signatures

**CloudTrail Lake**
- Status (November 2026): closed to new customers since 31 May 2026; existing customers can keep using it. For new setups, query trail logs in S3 with Athena or use CloudWatch.
- **Query CloudTrail logs** with SQL
- Retain events for up to **10 years** (3,653 days) with one-year extendable retention pricing, or up to 7 years with seven-year retention pricing
- Aggregate logs from multiple accounts/regions

### CloudTrail vs CloudWatch

| Feature | CloudTrail | CloudWatch |
|---------|-----------|------------|
| **Purpose** | API call auditing | Monitoring performance |
| **Data** | WHO did WHAT, WHEN | Metrics, logs, events |
| **Use Case** | Security, compliance | Performance, troubleshooting |
| **Example** | Who terminated EC2? | Is CPU high? |

---

## 3. AWS Config

### What is AWS Config?
- **Record and evaluate** resource configurations
- **Compliance auditing**
- **Configuration history** and change tracking
- **Continuous monitoring**

### AWS Config Features

**Configuration Recorder**
- Records resource configurations over time
- Stores in S3
- Can send to SNS for notifications

**Configuration Items**
- Point-in-time snapshot of resource
- Includes: Metadata, attributes, relationships, configuration

**Configuration History**
- View resource configuration over time
- Timeline of changes

**Configuration Snapshots**
- Collection of all configuration items
- Delivered to S3

### Config Rules

**AWS Managed Rules** (800+)
- Pre-built rules for common best practices
- Examples:
  - `encrypted-volumes`: Check if EBS volumes are encrypted
  - `s3-bucket-public-read-prohibited`: Check if S3 buckets are public
  - `iam-password-policy`: Check IAM password policy

**Custom Rules**
- Lambda functions to evaluate compliance
- Triggered by configuration changes or periodic

**Remediation**
- **Automatic remediation** using SSM Automation Documents
- Example: If EBS not encrypted → Delete volume (risky!)
- Can configure retry attempts

### Config Aggregator
- Aggregate Config data from **multiple accounts and regions**
- Central view of compliance

### Config vs CloudTrail

| Feature | Config | CloudTrail |
|---------|--------|-----------|
| **Focus** | Resource configuration | API calls |
| **Question** | What does it look like? | Who made the change? |
| **Data** | Configuration state | API call details |
| **Example** | Is SG port 22 open? | Who opened port 22? |

---

## 4. AWS Systems Manager (SSM)

### What is Systems Manager?
- **Operational hub** for AWS resources
- Manage **EC2 and on-premises** servers
- Patching, configuration, automation
- **Hybrid service** (AWS + on-premises)

### SSM Key Features

#### Session Manager
- **Secure shell access** to EC2
- **No SSH keys, bastion hosts, or open ports**
- Session logs sent to S3 or CloudWatch
- IAM permissions for access control
- **Audit trail** of all sessions

#### Patch Manager
- **Automate patching** for OS and applications
- **Patch baselines**: Which patches to install
- **Maintenance windows**: When to patch
- **Patch groups**: Group instances for patching
- Compliance reporting

#### Run Command
- **Execute commands** on managed instances
- No SSH required
- **Rate control** and **error control**
- Command history in CloudTrail
- Examples: Install software, run scripts, collect logs

#### State Manager
- **Maintain desired state** of instances
- **Associations**: Link configuration to instances
- Example: Ensure antivirus is installed and running

#### Parameter Store
- **Secure storage** for configuration and secrets
- (Covered in Module 07: Security)
- **Hierarchical storage**: `/app/db/password`
- Integration with CloudFormation, Lambda, etc.
- **Standard**: Free, 4 KB, 10,000 params (per account per Region)
- **Advanced**: $0.05/param/month, 8 KB, 100,000 params (per account per Region), parameter policies

#### Inventory
- **Collect metadata** from managed instances
- OS, applications, network config
- Query and visualize with Inventory dashboard

#### Automation
- **Automate common tasks**
- **Runbooks** (Automation Documents)
- Examples: Create AMI, patch instances, restart services
- Integration with Config for auto-remediation

#### Fleet Manager
- **Centralized view** of managed instances
- File system browser
- Performance counters
- Windows registry editor

### AWS OpsWorks (retired)
- Ran managed Chef and Puppet for configuration management (OpsWorks Stacks, OpsWorks for Chef Automate, OpsWorks for Puppet Enterprise)
- **End of life**: AWS has retired OpsWorks and removed it from the documentation. Older practice questions may still name it as the answer for "existing Chef or Puppet recipes"
- Current replacement for configuration management: **Systems Manager** (State Manager, Run Command, Automation). State Manager can apply existing Chef recipes with the `AWS-ApplyChefRecipes` document

---

## 5. AWS Trusted Advisor

### What is Trusted Advisor?
- **Best practice recommendations**
- Real-time guidance
- **Six categories**:
  1. **Cost Optimization**: Reduce costs
  2. **Performance**: Improve performance
  3. **Security**: Close security gaps
  4. **Fault Tolerance**: Increase availability
  5. **Service Limits**: Check service quotas
  6. **Operational Excellence**: Operate at scale

### Support Plans

Status (November 2026): Developer Support and Business Support closed to new subscriptions on 2 Dec 2025 and are discontinued on 1 Jan 2027. The current plans are Basic, Business Support+, Enterprise Support and Unified Operations.

**Basic Support** (and Developer Support until it is discontinued)
- **Core checks** (free): 6 security checks plus the service limit checks
  - S3 bucket permissions
  - Security groups - specific ports unrestricted
  - IAM use
  - MFA on root account
  - EBS public snapshots
  - RDS public snapshots
  - Service limits (all checks in this category)

**Business Support+ / Enterprise Support / Unified Operations** (and Business Support until it is discontinued)
- **Full set of checks** (all categories)
- **CloudWatch integration**
- **Programmatic access** via AWS Support API
- **Weekly email notifications**

### Trusted Advisor Notifications
- Set up Amazon EventBridge rules for status changes
- Automate actions based on recommendations

---

## 6. AWS Health (AWS Health Dashboard)

In 2022 AWS merged the Service Health Dashboard and the Personal Health Dashboard into one AWS Health Dashboard. Older questions may still use the old names.

### What is AWS Health?
- **Personalized view** of AWS service health
- Alerts for events affecting your resources
- **Proactive notifications**
- **Remediation guidance**

### AWS Health Features

**AWS Health Dashboard - service health** (formerly Service Health Dashboard)
- Overall status of AWS services (public)
- Historical information

**AWS Health Dashboard - your account health** (formerly Personal Health Dashboard)
- Personalized view for YOUR resources
- Alerts for:
  - Scheduled maintenance
  - Service degradation
  - Account-specific issues

**EventBridge Integration**
- Automate responses to health events
- Example: If EC2 scheduled for maintenance → Create snapshot

---

## 7. Amazon EventBridge (Monitoring Integration)

### EventBridge for Monitoring
- React to CloudWatch alarms
- React to AWS Health events
- React to Trusted Advisor checks
- Trigger automated remediation

Example: CloudWatch Alarm → EventBridge → Lambda → Fix issue

---

## Monitoring Best Practices

### Application Monitoring
 **CloudWatch Metrics**: Track performance  
 **CloudWatch Logs**: Centralize logs  
 **CloudWatch Alarms**: Alert on issues  
 **X-Ray**: Distributed tracing (not covered in depth)  

### Security Monitoring
 **CloudTrail**: All API calls  
 **Config**: Resource compliance  
 **GuardDuty**: Threat detection  
 **Security Hub**: Centralized findings  

### Operational Monitoring
 **Systems Manager**: Patch and configure  
 **Trusted Advisor**: Best practice checks  
 **AWS Health**: Service health events  

---

## Practice Questions

**Q1.** Which service records API calls made in your AWS account?
- A. CloudWatch
- B. CloudTrail
- C. AWS Config
- D. X-Ray

**Answer**: B

**Q2.** How can you collect memory metrics from EC2 instances?
- A. Enable detailed monitoring
- B. Install CloudWatch Agent
- C. Use CloudTrail
- D. Memory metrics are automatic

**Answer**: B

**Q3.** Which service helps you check if EBS volumes are encrypted?
- A. CloudWatch
- B. CloudTrail
- C. AWS Config
- D. Inspector

**Answer**: C

**Q4.** What is the retention period for CloudTrail events in Event History?
- A. 30 days
- B. 60 days
- C. 90 days
- D. 180 days

**Answer**: C

---

## Key Takeaways

 CloudWatch monitors metrics and logs, CloudTrail logs API calls  
 CloudWatch Agent required for EC2 memory/disk metrics  
 Config tracks resource configuration and compliance  
 Systems Manager for operational tasks (patching, automation, secure access)  
 Session Manager eliminates need for bastion hosts and SSH keys  
 Trusted Advisor provides best practice recommendations  
 CloudTrail records WHO did WHAT, Config shows WHAT it looks like  
 Use CloudWatch Logs Insights for log analysis  
 EventBridge integrates monitoring with automation  
 Always enable CloudTrail in all regions for security  

---

**Previous Module**: [Module 08: Application Integration](../08-Application-Integration/README.md)  
**Next Module**: [Module 10: Migration & Transfer](../10-Migration/README.md)


## References

Pages verified for this module (see [docs/REFERENCES.md](../docs/REFERENCES.md) for the full list):

- [CloudWatch metrics concepts (resolution, retention)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)
- [Invoke a Lambda function from a CloudWatch alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarms-and-actions-Lambda.html)
- [CloudWatch dashboard refresh interval](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/change_dashboard_refresh_interval.html)
- [CloudWatch Logs subscription filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html)
- [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/)
- [CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)
- [CloudTrail Lake pricing options and retention](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html)
- [List of AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)
- [AWS-DisableS3BucketPublicReadWrite runbook](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-disables3bucketpublicreadwrite.html)
- [Systems Manager pricing (Parameter Store tiers)](https://aws.amazon.com/systems-manager/pricing/)
- [Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html)
- [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html)
- [X-Ray concepts (retention, sampling)](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html)
- [Trusted Advisor check categories](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor.html)
- [AWS Support plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html)
- [AWS Premium Support FAQs (Trusted Advisor checks by plan)](https://aws.amazon.com/premiumsupport/faqs/)
- [Amazon S3 default encryption FAQ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html)
