# SAA-C03 In-Scope Services

Every service and feature on the official [in-scope services list](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html) of the exam guide, in the guide's order, with what it does, the scenario cue that usually points to it, and where this guide covers it. AWS says the list is non-exhaustive and subject to change; it was last compared with the exam guide on 2026-11-08.

Services marked **Status** have changed availability. The exam can still mention them, but prefer the current replacement when you design something new.

## Contents

- [Analytics](#analytics)
- [Application Integration](#application-integration)
- [AWS Cost Management](#aws-cost-management)
- [Compute](#compute)
- [Containers](#containers)
- [Database](#database)
- [Developer Tools](#developer-tools)
- [Front-End Web and Mobile](#front-end-web-and-mobile)
- [Machine Learning](#machine-learning)
- [Management and Governance](#management-and-governance)
- [Media Services](#media-services)
- [Migration and Transfer](#migration-and-transfer)
- [Networking and Content Delivery](#networking-and-content-delivery)
- [Security, Identity, and Compliance](#security-identity-and-compliance)
- [Serverless](#serverless)
- [Storage](#storage)

## Analytics

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| Amazon Athena | Serverless SQL queries on data in S3, billed per data scanned | Ad hoc SQL on S3 logs, no servers, pay per query | [11](../../11-Analytics/README.md) |
| AWS Data Exchange | Find, subscribe to and use third-party data sets | Buy or license external data and load it into S3 or Redshift | [11](../../11-Analytics/README.md) |
| AWS Data Pipeline | Scheduled data movement and processing between AWS services. **Status:** closed to new customers since July 2025; AWS recommends Glue, Step Functions or Amazon MWAA | Legacy scheduled ETL | [11](../../11-Analytics/README.md) |
| Amazon EMR | Managed Hadoop, Spark, Hive and Presto clusters, also on EKS or serverless | Big data processing with open-source frameworks | [11](../../11-Analytics/README.md) |
| AWS Glue | Serverless ETL, crawlers and the Data Catalog | Discover schemas, catalog S3 data, serverless ETL | [11](../../11-Analytics/README.md) |
| Amazon Kinesis | Data Streams (real-time stream with replay), Data Firehose (managed delivery to S3, Redshift, OpenSearch and others) | Real-time ingestion; "near real time, no code delivery to S3" means Firehose | [11](../../11-Analytics/README.md) |
| AWS Lake Formation | Builds and governs data lakes on S3 with fine-grained (table, column, row) permissions | Central permissions for a data lake used by Athena, Redshift and EMR | [11](../../11-Analytics/README.md) |
| Amazon MSK | Managed Apache Kafka, provisioned or serverless | Existing Kafka applications, Kafka APIs required | [11](../../11-Analytics/README.md) |
| Amazon OpenSearch Service | Managed OpenSearch for search, log analytics and dashboards | Full-text search, log analytics with OpenSearch Dashboards | [11](../../11-Analytics/README.md) |
| Amazon Quick | AI-assisted analytics; its BI feature, Amazon Quick Sight, was formerly Amazon QuickSight | Serverless BI dashboards for many users, pay per user or session | [11](../../11-Analytics/README.md) |
| Amazon Redshift | Columnar data warehouse, provisioned or serverless; Spectrum queries S3 | Complex SQL analytics and BI on large structured data | [11](../../11-Analytics/README.md), [05](../../05-Database/README.md) |

## Application Integration

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| Amazon AppFlow | Managed data transfer between SaaS apps (Salesforce, SAP, Zendesk and others) and AWS | Move SaaS data to S3 or Redshift on a schedule without code | [08](../../08-Application-Integration/README.md) |
| Amazon EventBridge | Serverless event bus, rules, scheduler and pipes; SaaS partner events | Event-driven routing between AWS services, SaaS and your apps; cron-style schedules | [08](../../08-Application-Integration/README.md) |
| Amazon MQ | Managed ActiveMQ and RabbitMQ | Migrating apps that use JMS, AMQP, MQTT or STOMP without code changes | [08](../../08-Application-Integration/README.md) |
| Amazon SNS | Pub/sub push to many subscribers (SQS, Lambda, HTTP, email, SMS) | Fan-out one message to many consumers | [08](../../08-Application-Integration/README.md) |
| Amazon SQS | Managed message queues, standard or FIFO | Decouple tiers, buffer load, retry with dead-letter queues | [08](../../08-Application-Integration/README.md) |
| AWS Step Functions | Serverless workflow orchestration with state machines | Multi-step workflows with retries, branching, human approval | [08](../../08-Application-Integration/README.md) |

## AWS Cost Management

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| AWS Budgets | Cost, usage and reservation budgets with alerts and actions | Alert or act when spend crosses a threshold | [13](../../13-Cost-Optimization/README.md) |
| AWS Cost and Usage Report | Most detailed billing data delivered to S3 (now also through Data Exports) | Line-item analysis with Athena or Quick Sight | [13](../../13-Cost-Optimization/README.md) |
| AWS Cost Explorer | Visualize and forecast cost and usage; RI and Savings Plans recommendations | See cost trends by service, tag or account | [13](../../13-Cost-Optimization/README.md) |
| Savings Plans | Commit to a $/hour spend for 1 or 3 years: Compute, EC2 Instance, Database, SageMaker AI | Steady usage across instance families, Fargate or Lambda | [13](../../13-Cost-Optimization/README.md) |

## Compute

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| AWS Batch | Managed batch job scheduling on EC2, Spot or Fargate | Large numbers of batch jobs, longer than Lambda's 15 minutes | [03](../../03-Compute/README.md) |
| Amazon EC2 | Virtual servers with many instance families and purchase options | Full OS control, long-running workloads | [03](../../03-Compute/README.md) |
| Amazon EC2 Auto Scaling | Adjusts the number of EC2 instances in a group | Scale out and in with demand, replace unhealthy instances | [03](../../03-Compute/README.md) |
| AWS Elastic Beanstalk | Deploys and manages web apps on EC2 for you | Developers upload code, AWS handles capacity and deployment | [03](../../03-Compute/README.md) |
| AWS Outposts | AWS infrastructure installed in your data center | Low latency or data residency on premises with AWS APIs | [03](../../03-Compute/README.md) |
| AWS Serverless Application Repository | Catalog of reusable serverless applications built with SAM | Share or deploy prebuilt serverless apps | [03](../../03-Compute/README.md) |
| VMware Cloud on AWS | VMware SDDC running on dedicated AWS hardware | Move vSphere workloads without converting them | [10](../../10-Migration/README.md) |
| AWS Wavelength | AWS compute and storage inside 5G carrier networks | Single-digit millisecond latency for mobile devices | [01](../../01-AWS-Fundamentals/README.md) |

## Containers

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| Amazon ECR | Managed container image registry with image scanning, lifecycle policies and cross-Region replication | Store and scan Docker images for ECS, EKS or Lambda | [03](../../03-Compute/README.md) |
| Amazon ECS | AWS-native container orchestration on EC2 or Fargate | Run containers without Kubernetes | [03](../../03-Compute/README.md) |
| Amazon ECS Anywhere | ECS control plane for containers on your own servers | Manage on-premises containers with ECS | [03](../../03-Compute/README.md) |
| Amazon EKS | Managed Kubernetes control plane | Kubernetes workloads, portability, existing Kubernetes tooling | [03](../../03-Compute/README.md) |
| Amazon EKS Anywhere | Run and manage Kubernetes clusters on your own infrastructure | Kubernetes on premises with EKS tooling | [03](../../03-Compute/README.md) |
| Amazon EKS Distro | The Kubernetes distribution used by EKS, which you install and run yourself | Same Kubernetes version as EKS, self-managed | [03](../../03-Compute/README.md) |

## Database

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| Amazon Aurora | MySQL- and PostgreSQL-compatible relational database, six copies across three AZs, up to 15 replicas | High performance relational, fast failover, Global Database | [05](../../05-Database/README.md) |
| Amazon Aurora Serverless | Aurora that scales capacity automatically (v2 in ACUs) | Unpredictable or intermittent relational workloads | [05](../../05-Database/README.md) |
| Amazon DocumentDB | MongoDB-compatible document database | Migrate MongoDB workloads, JSON documents | [05](../../05-Database/README.md) |
| Amazon DynamoDB | Serverless key-value and document database with single-digit millisecond latency | Massive scale key-value access, sessions, global tables | [05](../../05-Database/README.md) |
| Amazon ElastiCache | Managed Valkey, Redis OSS and Memcached | In-memory caching, session store, leaderboards | [05](../../05-Database/README.md) |
| Amazon Keyspaces | Serverless Apache Cassandra-compatible database | Migrate Cassandra workloads, CQL | [05](../../05-Database/README.md) |
| Amazon Neptune | Graph database (property graph and RDF) | Social networks, fraud detection, recommendation graphs | [05](../../05-Database/README.md) |
| Amazon RDS | Managed MySQL, PostgreSQL, MariaDB, Oracle, SQL Server and Db2 | Lift-and-shift relational databases, Multi-AZ, read replicas | [05](../../05-Database/README.md) |
| Amazon Redshift | Data warehouse (see Analytics) | OLAP and reporting, not OLTP | [05](../../05-Database/README.md) |

## Developer Tools

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| AWS X-Ray | Distributed tracing and service maps | Find latency or errors across microservices and Lambda | [09](../../09-Monitoring/README.md) |

## Front-End Web and Mobile

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| AWS Amplify | Build, host and deploy full-stack web and mobile apps | Hosting with CI/CD for single-page apps, quick backends | [08](../../08-Application-Integration/README.md) |
| Amazon API Gateway | Managed REST, HTTP and WebSocket APIs with throttling, caching and authorizers | Front door for Lambda or HTTP backends | [08](../../08-Application-Integration/README.md) |
| AWS Device Farm | Test web and mobile apps on real devices and browsers | Test an app across many phones and browsers | [08](../../08-Application-Integration/README.md) |

## Machine Learning

The exam tests which managed AI service fits a task, not how to build models.

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| Amazon Comprehend | Natural language processing: entities, sentiment, key phrases, PII detection | Analyze sentiment of reviews or find PII in text | [11](../../11-Analytics/README.md) |
| Amazon Lex | Conversational chatbots with speech and text | Build a chatbot or voice bot | [11](../../11-Analytics/README.md) |
| Amazon Polly | Text to speech | Turn articles into audio | [11](../../11-Analytics/README.md) |
| Amazon Rekognition | Image and video analysis: objects, faces, text, content moderation | Detect faces or unsafe content in images | [11](../../11-Analytics/README.md) |
| Amazon SageMaker AI | Build, train and deploy your own ML models | Custom model training and hosting | [11](../../11-Analytics/README.md) |
| Amazon Textract | Extract text, forms and tables from scanned documents | Read data from invoices or forms | [11](../../11-Analytics/README.md) |
| Amazon Transcribe | Speech to text | Transcribe call recordings | [11](../../11-Analytics/README.md) |
| Amazon Translate | Neural machine translation | Translate content into other languages | [11](../../11-Analytics/README.md) |

## Management and Governance

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| AWS Auto Scaling | Scaling plans across EC2, ECS, DynamoDB and Aurora | One place to scale several resource types | [03](../../03-Compute/README.md) |
| AWS CLI | Command-line access to AWS APIs | Scripting and automation | [01](../../01-AWS-Fundamentals/README.md) |
| AWS CloudFormation | Infrastructure as code with templates and stacks; StackSets across accounts and Regions | Repeatable environments, deploy the same stack to many accounts | [09](../../09-Monitoring/README.md) |
| AWS CloudTrail | Records API calls for auditing | Who did what and when | [09](../../09-Monitoring/README.md) |
| Amazon CloudWatch | Metrics, logs, alarms, dashboards | Monitor resources and trigger actions | [09](../../09-Monitoring/README.md) |
| AWS Compute Optimizer | Right-sizing recommendations for EC2, Auto Scaling, EBS, Lambda, ECS on Fargate and RDS | Find over- or under-provisioned resources | [13](../../13-Cost-Optimization/README.md) |
| AWS Config | Records resource configuration and evaluates compliance rules | Track configuration changes, detect non-compliant resources | [09](../../09-Monitoring/README.md) |
| AWS Control Tower | Sets up and governs a multi-account landing zone with controls | New multi-account environment with guardrails | [01](../../01-AWS-Fundamentals/README.md) |
| AWS Health Dashboard | Service health and events that affect your account | Get notified of AWS events affecting your resources | [09](../../09-Monitoring/README.md) |
| AWS License Manager | Track and enforce software license usage | Control BYOL licenses (Windows, Oracle, SQL Server) | [01](../../01-AWS-Fundamentals/README.md) |
| Amazon Managed Grafana | Managed Grafana dashboards over many data sources | Grafana dashboards without running servers | [09](../../09-Monitoring/README.md) |
| Amazon Managed Service for Prometheus | Prometheus-compatible metrics storage and querying | Container and Kubernetes metrics with PromQL | [09](../../09-Monitoring/README.md) |
| AWS Management Console | Web interface for AWS | Manual administration | [01](../../01-AWS-Fundamentals/README.md) |
| AWS Organizations | Group accounts, consolidated billing, SCPs and RCPs | Central governance and billing across accounts | [02](../../02-IAM/README.md) |
| AWS Proton | Templates for self-service infrastructure and deployments. **Status:** end of support on 7 October 2026; closed to new customers since 7 October 2025 | Platform team templates for developers | [09](../../09-Monitoring/README.md) |
| AWS Service Catalog | Approved catalog of CloudFormation products for self-service | Let users launch only approved, compliant stacks | [01](../../01-AWS-Fundamentals/README.md) |
| AWS Systems Manager | Operations hub: Session Manager, Patch Manager, Run Command, Parameter Store | Patch fleets, shell access without SSH or bastions, store configuration | [09](../../09-Monitoring/README.md) |
| AWS Well-Architected Tool | Review workloads against the Well-Architected Framework | Assess a workload and track improvements | [12](../../12-Architecture-Patterns/README.md) |

## Media Services

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| Amazon Kinesis Video Streams | Ingest, store and process video streams from devices | Camera feeds for playback or analysis with Rekognition | [11](../../11-Analytics/README.md) |

## Migration and Transfer

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| AWS Application Discovery Service | Collects on-premises server inventory and dependencies. **Status:** closed to new customers; AWS Transform is the recommended replacement | Plan a migration from server data | [10](../../10-Migration/README.md) |
| AWS Application Migration Service | Block-level replication for lift-and-shift rehosting to EC2 | Rehost servers with minimal downtime | [10](../../10-Migration/README.md) |
| AWS DataSync | Online data transfer between on premises, other clouds and AWS storage | Scheduled or one-time copy of NFS, SMB, HDFS or object data | [10](../../10-Migration/README.md) |
| AWS DMS | Database migration with ongoing replication (CDC); Schema Conversion for engine changes | Migrate a database with minimal downtime | [10](../../10-Migration/README.md) |
| AWS Snow Family | Physical devices for offline transfer and edge computing. **Status:** no Snow device is offered to new customers (Snowball Edge closed, Snowcone discontinued); AWS points new customers to DataSync or AWS Data Transfer Terminal, and to Outposts for edge compute | Very large data sets with limited bandwidth | [10](../../10-Migration/README.md) |
| AWS Transfer Family | Managed SFTP, FTPS, FTP and AS2 into S3 or EFS | Partners must keep using SFTP | [10](../../10-Migration/README.md) |

## Networking and Content Delivery

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| AWS Client VPN | Managed OpenVPN-based remote access for users | Remote employees need secure access to a VPC | [06](../../06-Networking/README.md) |
| Amazon CloudFront | CDN with edge caching, OAC for S3, signed URLs and cookies | Cache static and dynamic content close to users | [06](../../06-Networking/README.md) |
| AWS Direct Connect | Dedicated private connection from on premises to AWS | Consistent bandwidth and latency, private connectivity | [06](../../06-Networking/README.md) |
| Elastic Load Balancing | ALB (layer 7), NLB (layer 4), GWLB (appliances) | Distribute traffic across targets and AZs | [03](../../03-Compute/README.md) |
| AWS Global Accelerator | Anycast static IPs routing over the AWS network | Static IPs, fast Regional failover, non-HTTP traffic | [06](../../06-Networking/README.md) |
| AWS PrivateLink | Private access to services through interface endpoints | Expose a service to other VPCs without peering | [06](../../06-Networking/README.md) |
| Amazon Route 53 | DNS, health checks and routing policies | Failover, latency, weighted and geolocation routing | [06](../../06-Networking/README.md) |
| AWS Site-to-Site VPN | IPsec tunnels over the internet | Quick, encrypted hybrid connectivity or Direct Connect backup | [06](../../06-Networking/README.md) |
| AWS Transit Gateway | Regional hub connecting VPCs and on-premises networks | Many VPCs with transitive routing | [06](../../06-Networking/README.md) |
| Amazon VPC | Isolated network with subnets, route tables, security groups and NACLs | Network design and isolation | [06](../../06-Networking/README.md) |

## Security, Identity, and Compliance

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| AWS Artifact | On-demand compliance reports and agreements | Auditor needs SOC or PCI reports, sign a BAA | [07](../../07-Security/README.md) |
| AWS Certificate Manager | Free public TLS certificates with automatic renewal | HTTPS on ALB, CloudFront or API Gateway | [07](../../07-Security/README.md) |
| AWS CloudHSM | Single-tenant hardware security modules you control | FIPS 140-3 Level 3 HSM, full key control | [07](../../07-Security/README.md) |
| Amazon Cognito | User pools (sign-up and sign-in) and identity pools (temporary AWS credentials) | Authentication for web and mobile app users | [02](../../02-IAM/README.md) |
| Amazon Detective | Investigates root cause of security findings with graph analysis | Investigate a GuardDuty finding | [07](../../07-Security/README.md) |
| AWS Directory Service | Managed Microsoft AD, AD Connector, Simple AD | Use Active Directory with AWS workloads | [07](../../07-Security/README.md) |
| AWS Firewall Manager | Central management of WAF, Shield Advanced, security groups and Network Firewall across accounts | Enforce firewall rules organization-wide | [07](../../07-Security/README.md) |
| Amazon GuardDuty | Threat detection from CloudTrail, VPC Flow Logs, DNS logs and more | Detect compromised instances or credentials | [07](../../07-Security/README.md) |
| AWS IAM Identity Center | Workforce single sign-on to accounts and apps | Employees sign in once to many accounts | [02](../../02-IAM/README.md) |
| Amazon Inspector | Automated vulnerability scanning of EC2, ECR images and Lambda | Find CVEs in instances and container images | [07](../../07-Security/README.md) |
| AWS KMS | Managed encryption keys integrated with AWS services | Encrypt data at rest with managed or customer managed keys | [07](../../07-Security/README.md) |
| Amazon Macie | Discovers sensitive data such as PII in S3 | Find PII in S3 buckets | [07](../../07-Security/README.md) |
| AWS Network Firewall | Managed stateful firewall and IPS for VPCs | Inspect and filter VPC traffic, domain filtering | [07](../../07-Security/README.md) |
| AWS Resource Access Manager | Share resources such as subnets and Transit Gateways across accounts | Share a VPC subnet with other accounts | [01](../../01-AWS-Fundamentals/README.md) |
| AWS Secrets Manager | Store and automatically rotate secrets | Rotate database passwords automatically | [07](../../07-Security/README.md) |
| AWS Security Hub | Aggregates security findings and runs best-practice checks | Single view of security posture across accounts | [07](../../07-Security/README.md) |
| AWS Shield | DDoS protection: Standard (free) and Advanced (paid, response team, cost protection) | Protect against DDoS | [07](../../07-Security/README.md) |
| AWS WAF | Layer 7 web application firewall for CloudFront, ALB, API Gateway and others | Block SQL injection, XSS, rate-limit IPs | [07](../../07-Security/README.md) |
| IAM | Users, groups, roles and policies | Least-privilege access control | [02](../../02-IAM/README.md) |

## Serverless

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| AWS Fargate | Serverless compute for ECS and EKS containers | Containers without managing servers | [03](../../03-Compute/README.md) |
| AWS Lambda | Event-driven functions, up to 15 minutes per invocation | Short event-driven tasks, pay per request | [03](../../03-Compute/README.md) |

## Storage

| Service | What it does | Scenario cue | Module |
|---------|--------------|--------------|--------|
| AWS Backup | Central, policy-based backups across services and accounts | One backup policy for EBS, RDS, DynamoDB, EFS and more | [04](../../04-Storage/README.md) |
| Amazon EBS | Block storage for EC2 in one AZ | Boot volumes, databases on EC2 | [04](../../04-Storage/README.md) |
| Amazon EFS | Elastic NFS file system across AZs for Linux | Shared file storage for many Linux instances | [04](../../04-Storage/README.md) |
| Amazon FSx | Managed Windows File Server, Lustre, NetApp ONTAP and OpenZFS | Windows SMB shares, HPC with Lustre, NetApp features | [04](../../04-Storage/README.md) |
| Amazon S3 | Object storage with eleven nines of durability and many storage classes | Static content, data lakes, backups | [04](../../04-Storage/README.md) |
| Amazon S3 Glacier | Archive storage classes: Instant Retrieval, Flexible Retrieval, Deep Archive | Long-term archives at lowest cost | [04](../../04-Storage/README.md) |
| AWS Storage Gateway | Hybrid access to cloud storage: S3 File Gateway, Volume Gateway, Tape Gateway (FSx File Gateway is closed to new customers) | On-premises apps use cloud storage through NFS, SMB or iSCSI | [04](../../04-Storage/README.md) |
