# SAA-C03 Exam Coverage Map

Maps each task statement in the [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) to the topics it covers and where this guide teaches them. Last compared with the exam guide on 2026-11-08.

Use it two ways: before studying, to see what each domain expects; after a practice test, to jump from a weak task to the right module.

For a per-service view, see [In-scope services](../reference/IN-SCOPE-SERVICES.md).

## Exam format

| Item | Value |
|------|-------|
| Questions | 65: 50 scored, 15 unscored (not identified) |
| Question types | Multiple choice (1 correct of 4), multiple response (2 or more correct of 5 or more) |
| Scoring | Scaled 100-1,000, pass at 720; no penalty for guessing |
| Time | 130 minutes |

## Domain weights

| Domain | Weight |
|--------|--------|
| 1. Design Secure Architectures | 30% |
| 2. Design Resilient Architectures | 26% |
| 3. Design High-Performing Architectures | 24% |
| 4. Design Cost-Optimized Architectures | 20% |

## Domain 1: Design Secure Architectures (30%)

| Task | Topics | Where |
|------|--------|-------|
| 1.1 Design secure access to AWS resources | IAM users, groups, roles and policies; policy evaluation; least privilege; MFA and root user protection; IAM Identity Center; cross-account roles; Organizations with SCPs and RCPs; Control Tower; Cognito; STS and federation | [02 IAM](../../02-IAM/README.md), [01 Fundamentals](../../01-AWS-Fundamentals/README.md), [07 Security](../../07-Security/README.md) |
| 1.2 Design secure workloads and applications | VPC design with public and private subnets; security groups vs NACLs; VPC endpoints and PrivateLink; WAF, Shield, Firewall Manager, Network Firewall; GuardDuty, Inspector, Macie, Security Hub, Detective; Secrets Manager and Parameter Store; Cognito for app users; Verified Access | [06 Networking](../../06-Networking/README.md), [07 Security](../../07-Security/README.md) |
| 1.3 Determine appropriate data security controls | KMS key types and rotation; CloudHSM; encryption at rest and in transit; ACM; S3 bucket policies, Block Public Access, Object Lock; backups and retention; data classification and compliance (Artifact, Config) | [07 Security](../../07-Security/README.md), [04 Storage](../../04-Storage/README.md), [09 Monitoring](../../09-Monitoring/README.md) |

## Domain 2: Design Resilient Architectures (26%)

| Task | Topics | Where |
|------|--------|-------|
| 2.1 Design scalable and loosely coupled architectures | SQS, SNS, EventBridge, Step Functions, MQ; API Gateway; Lambda and containers (ECS, EKS, Fargate); caching with ElastiCache and CloudFront; stateless design; Auto Scaling; microservices and event-driven patterns | [08 Application Integration](../../08-Application-Integration/README.md), [03 Compute](../../03-Compute/README.md), [12 Architecture Patterns](../../12-Architecture-Patterns/README.md) |
| 2.2 Design highly available and/or fault-tolerant architectures | Multi-AZ and multi-Region designs; ELB health checks; Route 53 routing and failover; RDS Multi-AZ, Aurora replicas and Global Database, DynamoDB global tables; backup and restore, pilot light, warm standby, multi-site; RTO and RPO; AWS Backup; Elastic Disaster Recovery; ARC zonal shift | [12 Architecture Patterns](../../12-Architecture-Patterns/README.md), [05 Database](../../05-Database/README.md), [06 Networking](../../06-Networking/README.md) |

## Domain 3: Design High-Performing Architectures (24%)

| Task | Topics | Where |
|------|--------|-------|
| 3.1 Determine high-performing and/or scalable storage solutions | S3 performance (prefixes, multipart upload, Transfer Acceleration, Express One Zone); EBS volume types; EFS and FSx performance options; instance store | [04 Storage](../../04-Storage/README.md) |
| 3.2 Design high-performing and elastic compute solutions | EC2 instance families and placement groups; Auto Scaling policies; Lambda concurrency and SnapStart; ECS, EKS and Fargate; Batch; EMR | [03 Compute](../../03-Compute/README.md) |
| 3.3 Determine high-performing database solutions | RDS vs Aurora vs DynamoDB; read replicas; RDS Proxy; DynamoDB capacity modes and DAX; ElastiCache; purpose-built databases (Neptune, DocumentDB, Keyspaces, Timestream) | [05 Database](../../05-Database/README.md) |
| 3.4 Determine high-performing and/or scalable network architectures | CloudFront; Global Accelerator; Route 53 latency routing; Direct Connect and VPN; Transit Gateway; VPC peering; VPC Lattice; load balancer types | [06 Networking](../../06-Networking/README.md) |
| 3.5 Determine high-performing data ingestion and transformation solutions | Kinesis Data Streams and Data Firehose; MSK; Glue; Athena; EMR; Lake Formation; Redshift; zero-ETL; DataSync and Transfer Family; Amazon Quick Sight | [11 Analytics](../../11-Analytics/README.md), [10 Migration](../../10-Migration/README.md) |

## Domain 4: Design Cost-Optimized Architectures (20%)

| Task | Topics | Where |
|------|--------|-------|
| 4.1 Design cost-optimized storage solutions | S3 storage classes, lifecycle rules and Intelligent-Tiering; EBS gp3 vs gp2; EFS and FSx storage classes; Storage Gateway; data transfer costs | [04 Storage](../../04-Storage/README.md), [13 Cost Optimization](../../13-Cost-Optimization/README.md) |
| 4.2 Design cost-optimized compute solutions | On-Demand, Reserved Instances, Savings Plans, Spot; right-sizing with Compute Optimizer; Graviton; Lambda and Fargate pricing; Auto Scaling | [13 Cost Optimization](../../13-Cost-Optimization/README.md), [03 Compute](../../03-Compute/README.md) |
| 4.3 Design cost-optimized database solutions | RDS and Aurora reserved instances and Database Savings Plans; Aurora Serverless; Aurora I/O-Optimized; DynamoDB on-demand vs provisioned and reserved capacity; caching to reduce database load | [05 Database](../../05-Database/README.md), [13 Cost Optimization](../../13-Cost-Optimization/README.md) |
| 4.4 Design cost-optimized network architectures | NAT gateway costs and VPC gateway endpoints; data transfer between AZs and Regions; CloudFront to cut origin egress; Direct Connect vs VPN costs; Transit Gateway vs peering | [06 Networking](../../06-Networking/README.md), [13 Cost Optimization](../../13-Cost-Optimization/README.md) |

## Cross-cutting material

| Need | Where |
|------|-------|
| Practice by domain | [Exam simulator](../../simulator/), module `PRACTICE-QUESTIONS.md` files, [exam reviews](../../exam-reviews/README.md) |
| Newer features that questions may use | "Newer Features to Know" sections in modules 03-08 and 12, and the [flashcards](../study-guides/FLASHCARDS.md#newer-features-2023-2026) |
| Official sources | [References](../REFERENCES.md) |
