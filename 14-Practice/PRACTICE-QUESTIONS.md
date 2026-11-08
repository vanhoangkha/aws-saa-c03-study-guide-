# AWS SAA-C03 Practice Questions

> Focused practice questions for weak areas and common exam scenarios

> **DISCLAIMER:** These are **original practice questions** created for educational purposes. They are **NOT actual exam questions** and do not represent questions from the AWS certification exam. All content is based on publicly available AWS documentation.

## Categories
- [Auto Scaling & High Availability](#auto-scaling--high-availability)
- [Storage & Data Management](#storage--data-management)
- [Networking](#networking)
- [Databases](#databases)
- [Serverless & Containers](#serverless--containers)
- [Security](#security)
- [Cost Optimization](#cost-optimization)

---

## Auto Scaling & High Availability

### Question 1
An Auto Scaling group isn't responding to CloudWatch alarms despite the alarm firing. What's the most likely cause?

**Options:**
A. Wrong CloudWatch metric configured
B. The Auto Scaling group is in cooldown period (correct)
C. Minimum size of ASG is 0
D. Desired size of ASG is 0

**Explanation:** With simple scaling policies, the group waits for the cooldown period (default 300 seconds) after a scaling activity before any further simple-scaling activity can start, so a firing alarm has no effect until the cooldown ends. Target tracking and step scaling policies do not wait for cooldowns (they use instance warmup), and AWS recommends them over simple scaling.

---

### Question 2
You need to upgrade one EC2 instance in an ASG without receiving traffic. What should you do?

**Options:**
A. Hibernate the instance
B. Use cooldown timers
C. Put instance in Standby, upgrade, return to InService (correct)
D. Use lifecycle hooks

**Explanation:** Standby detaches from load balancing while retaining in ASG, preventing replacement.

---

## Storage & Data Management

### Question 3
How do you achieve WORM (Write Once Read Many) in S3?

**Options:**
A. Enable versioning
B. Enable S3 Object Lock on the bucket (correct)
C. Use S3 Glacier
D. Configure bucket policy

**Explanation:** Object Lock enforces WORM with retention periods and legal holds. It requires versioning and can be enabled on new or existing buckets.

---

### Question 4
After deleting an S3 object (no versioning), what do you see immediately in a list-objects call?

**Options:**
A. Object still appears
B. Object is deleted (correct)
C. May appear or not depending on consistency
D. Object has a delete marker

**Explanation:** S3 provides strong consistency; object disappears immediately after successful delete.

---

## Networking

### Question 5
What VPC feature provides private connectivity to S3 and DynamoDB without cost?

**Options:**
A. NAT Gateway
B. VPC Peering
C. Gateway Endpoints (correct)
D. Interface Endpoints

**Explanation:** Gateway endpoints for S3/DynamoDB are free and route-table based.

---

### Question 6
Internet-facing ALB requests fail despite healthy targets. What's likely wrong?

**Options:**
A. ALB subnet route table lacks IGW route (correct)
B. Targets in public subnet
C. ALB has no Elastic IP
D. Cross-zone LB disabled

**Explanation:** ALB must be in public subnets with 0.0.0.0/0 → IGW route.

---

## Databases

### Question 7
Your read-heavy app hits 100% CPU on RDS. What helps scale reads? (Choose 3)

**Options:**
A. Add Read Replicas (correct)
B. Enable Storage Auto Scaling
C. Use SQS to throttle
D. Use ElastiCache (correct)
E. Shard across multiple RDS instances (correct)
F. Enable Multi-AZ

**Explanation:** Read replicas, caching, and sharding all reduce read load on primary.

---

### Question 8
Multi-AZ RDS deployment provides:

**Options:**
A. Read scaling
B. Automatic failover for high availability (correct)
C. Cross-region disaster recovery
D. Cost optimization

**Explanation:** A Multi-AZ DB instance deployment keeps a synchronous standby in another AZ for automatic failover; the standby cannot serve reads. (A Multi-AZ DB cluster deployment, available for RDS for MySQL and PostgreSQL, adds two readable standbys.)

---

## Serverless & Containers

### Question 9
Lambda needs to write CloudWatch Logs. Which permissions required? (Choose 3)

**Options:**
A. logs:CreateLogGroup (correct)
B. logs:GetLogEvents
C. logs:CreateLogStream (correct)
D. logs:DescribeLogStreams
E. logs:PutLogEvents (correct)

**Explanation:** The AWSLambdaBasicExecutionRole managed policy grants exactly these three actions. Lambda uses them to create the log group (`/aws/lambda/<function-name>`) and log streams and to write log events.

---

### Question 10
Which ECS networking mode provides task-level security groups?

**Options:**
A. Host
B. Bridge
C. awsvpc (correct)
D. Default

**Explanation:** awsvpc gives each task its own ENI, enabling task-level security groups.

---

## Security

### Question 11
How do you restrict an S3 bucket so that only specific IAM roles can access it, even if other principals in the account have IAM policies that allow S3 access?

**Options:**
A. Bucket policy with an explicit Deny for all principals whose aws:PrincipalArn is not one of the listed roles (correct)
B. Bucket policy that only Allows the listed roles, with no Deny statement
C. IAM identity policies attached to the listed roles that allow S3 access
D. Bucket policy with a Deny statement that uses NotPrincipal to exempt the listed roles

**Explanation:** An explicit Deny overrides any Allow, so a bucket policy that denies every principal except the listed role ARNs (condition on `aws:PrincipalArn`) is what actually restricts access. An Allow-only bucket policy (B) or role policies (C) do not stop other principals whose own IAM policies grant S3 access. AWS recommends the `aws:PrincipalArn` condition instead of `NotPrincipal` with Deny (D), which also denies principals that have a permissions boundary.

---

### Question 12
CloudFront serves private content from S3. How do you grant access to multiple files?

**Options:**
A. S3 pre-signed URLs
B. CloudFront signed URLs
C. CloudFront signed cookies (correct)
D. CloudFront geo restrictions

**Explanation:** Signed cookies grant access to multiple objects without changing URLs.

---

## Cost Optimization

### Question 13
Which services identify underutilized EC2 instances? (Choose 2)

**Options:**
A. CloudWatch (correct)
B. SNS
C. Trusted Advisor (correct)
D. CloudTrail
E. Config

**Explanation:** CloudWatch metrics and Trusted Advisor checks identify low-utilization instances. AWS Compute Optimizer (not listed) is the purpose-built right-sizing service.

---

### Question 14
Most cost-effective connectivity for small vendor team to VPC databases?

**Options:**
A. AWS Client VPN (correct)
B. Direct Connect
C. Site-to-Site VPN to VGW
D. Site-to-Site VPN to Transit Gateway

**Explanation:** Client VPN provides user-level auth, pay-as-you-go pricing, minimal setup.

---

## Architecture Patterns

### Question 15
Serverless media processing pipeline with visual workflow and priority queues?

**Options:**
A. S3 → Lambda → SQS → DynamoDB
B. S3 → Lambda → SWF → DynamoDB
C. S3 → Lambda → process → DynamoDB
D. S3 → Lambda → Step Functions → DynamoDB (correct)

**Explanation:** Step Functions provides visual workflows with native Lambda and DynamoDB integrations, and AWS recommends it over Amazon SWF for new applications. Priorities can be handled with separate state machines or separate queues (SQS has no message priority).

---

*Practice these scenarios until you can explain each answer confidently.*

