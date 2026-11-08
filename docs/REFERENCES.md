# SAA-C03 References

Official and community sources for the AWS Certified Solutions Architect – Associate (SAA-C03) exam, grouped by how you use them. Official AWS sources come first; when anything in this guide disagrees with them, the official source wins.

Every link was checked on 2026-11-08. To check them again, run `python3 scripts/check_external_links.py docs/REFERENCES.md`.

## Contents

- [Exam](#exam)
- [Official exam preparation](#official-exam-preparation)
- [AWS Well-Architected](#aws-well-architected)
- [Decision guides](#decision-guides)
- [Whitepapers and guides](#whitepapers-and-guides)
- [Documentation and FAQs by module](#documentation-and-faqs-by-module)
- [Architecture examples](#architecture-examples)
- [Pricing, quotas and Regions](#pricing-quotas-and-regions)
- [Hands-on practice](#hands-on-practice)
- [Staying current](#staying-current)
- [Community study guides](#community-study-guides)
- [Third-party courses and practice tests](#third-party-courses-and-practice-tests)

## Exam

| Source | Use it for |
|--------|------------|
| [Exam page](https://aws.amazon.com/certification/certified-solutions-architect-associate/) | Format, price, languages, scheduling, and the four-step preparation plan |
| [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) | Domains and weights, task statements, in-scope and out-of-scope services. Read this first and come back to it at the end |
| [In-scope services in this guide](reference/IN-SCOPE-SERVICES.md) | The exam guide's service list with a one-line summary and scenario cue for each service |
| [All AWS exam guides](https://docs.aws.amazon.com/aws-certification/latest/examguides/aws-certification-exam-guides.html) | Comparing SAA-C03 with Cloud Practitioner, SAP-C03 and the specialty exams |
| [Certification policies](https://aws.amazon.com/certification/policies/) | ID requirements, online proctoring rules, retakes, accommodations |
| [Certification FAQ](https://aws.amazon.com/certification/faqs/) | Scoring, results, discounts |
| [Recertification](https://aws.amazon.com/certification/recertification/) | Keeping the certification active after three years |
| [Certification Program Agreement](https://aws.amazon.com/certification/certification-agreement/) | What you may and may not share about exam content |

## Official exam preparation

| Source | Use it for |
|--------|------------|
| [AWS Skill Builder](https://skillbuilder.aws/) | The Official Practice Question Set (free), the Exam Prep course, the Official Practice Exam and Builder Labs. Search for "Solutions Architect – Associate" |
| [AWS Training](https://aws.amazon.com/training/) | Classroom and digital courses, free exam-readiness webinars |
| [Immersive learning](https://aws.amazon.com/training/digital/immersive-learning/) | AWS Cloud Quest, AWS SimuLearn, AWS Jam and AWS Escape Room |

## AWS Well-Architected

SAA-C03 tests whether you can design against the Well-Architected Framework, so the pillar papers are the closest thing to an official textbook.

| Source | Most relevant exam domain |
|--------|---------------------------|
| [Framework overview](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) | All |
| [Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) | 1. Secure architectures |
| [Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) | 2. Resilient architectures |
| [Performance Efficiency Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) | 3. High-performing architectures |
| [Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) | 4. Cost-optimized architectures |
| [Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) | All |
| [Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) | All |
| [Serverless Applications Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) | 2, 3 |
| [Well-Architected home](https://aws.amazon.com/architecture/well-architected/) and [Well-Architected Tool](https://aws.amazon.com/well-architected-tool/) | Lenses, labs, and reviewing your own workloads |

## Decision guides

Each guide compares the services in one category and explains when to choose which. Most exam questions are this kind of choice. Index: [AWS Decision Guides](https://docs.aws.amazon.com/decision-guides/).

| Guide | Module |
|-------|--------|
| [Choosing an AWS compute service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-aws-compute-service.html) | 03 |
| [Choosing an AWS container service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-aws-container-service.html) | 03 |
| [Choosing an AWS serverless service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-aws-serverless-service.html) | 03, 08 |
| [Fargate or Lambda](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/fargate-or-lambda.html) | 03 |
| [Lightsail, Elastic Beanstalk or EC2](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/lightsail-elastic-beanstalk-ec2.html) | 03 |
| [EC2 purchasing options](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/ec2-purchasing-options-aws-how-to-choose.html) | 03, 13 |
| [Choosing an AWS storage service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-aws-storage-service.html) | 04 |
| [Choosing an AWS database service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/databases-on-aws-how-to-choose.html) | 05 |
| [Choosing a networking and content delivery service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-networking-and-content-delivery-service.html) | 06 |
| [Choosing AWS security services](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-aws-security-services.html) | 07 |
| [Choosing identity services](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/identity-on-aws-how-to-choose.html) | 02 |
| [WAF or Shield](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/waf-or-shield.html) | 07 |
| [Choosing application integration services](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/application-integration-on-aws-how-to-choose.html) | 08 |
| [SNS, SQS or EventBridge](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/sns-or-sqs-or-eventbridge.html) | 08 |
| [Choosing monitoring services](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/monitoring-on-aws-how-to-choose.html) | 09 |
| [CloudTrail or CloudWatch](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/cloudtrail-or-cloudwatch.html) | 09 |
| [Choosing cloud governance services](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/cloud-governance-on-aws-how-to-choose.html) | 02, 09 |
| [Choosing migration services](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/migration-on-aws-how-to-choose.html) | 10 |
| [Choosing an AWS analytics service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/analytics-on-aws-how-to-choose.html) | 11 |
| [Choosing machine learning services](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/ml-guide.html) | 11 |
| [Modern application strategy](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/modern-apps-strategy-on-aws-how-to-choose.html) | 12 |
| [Choosing cost management services](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/cost-management-on-aws-how-to-choose.html) | 13 |

## Whitepapers and guides

| Paper | Module |
|-------|--------|
| [Overview of Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html) | 01 |
| [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) | 01, 12 |
| [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) | 01, 07 |
| [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) | 02, 07 |
| [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) | 02 |
| [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) | 02 |
| [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) | 02 |
| [Spot Instance best practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html) | 03, 13 |
| [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) | 04 |
| [S3 lifecycle transitions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html) | 04 |
| [RDS Multi-AZ deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) | 05 |
| [Building a Scalable and Secure Multi-VPC Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) | 06 |
| [Amazon VPC Connectivity Options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html) | 06 |
| [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) | 06 |
| [VPC security best practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html) | 06, 07 |
| [How Elastic Load Balancing works](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html) | 03, 06 |
| [AWS Best Practices for DDoS Resiliency](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/) | 07 |
| [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/) | 07 |
| [Security in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html) | 03, 07 |
| [ElastiCache caching strategies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html) | 05 |
| [Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html) | 08, 12 |
| [AWS Migration Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-migration-whitepaper/welcome.html) | 10 |
| [Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) | 12 |
| [AWS Multi-Region Fundamentals](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/) | 12 |
| [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) | 10, 12 |
| [How AWS Pricing Works](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/) | 13 |
| [All AWS whitepapers](https://aws.amazon.com/whitepapers/) | |

## Documentation and FAQs by module

Service FAQs are short, current and close to the level of detail the exam asks for. Read the FAQ first and the user guide when a FAQ answer is not enough.

| Module | Documentation | FAQs |
|--------|---------------|------|
| 01 Fundamentals | [Global infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) | [All FAQs](https://aws.amazon.com/faqs/) |
| 02 IAM | [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/) | [IAM](https://aws.amazon.com/iam/faqs/), [Organizations](https://aws.amazon.com/organizations/faqs/), [IAM Identity Center](https://aws.amazon.com/iam/identity-center/faqs/), [Control Tower](https://aws.amazon.com/controltower/faqs/), [Cognito](https://aws.amazon.com/cognito/faqs/), [Directory Service](https://aws.amazon.com/directoryservice/faqs/) |
| 03 Compute | [EC2](https://docs.aws.amazon.com/ec2/), [EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html), [Lambda](https://docs.aws.amazon.com/lambda/), [ECS](https://docs.aws.amazon.com/ecs/), [EKS](https://docs.aws.amazon.com/eks/), [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/) | [EC2](https://aws.amazon.com/ec2/faqs/), [Lambda](https://aws.amazon.com/lambda/faqs/), [ECS](https://aws.amazon.com/ecs/faqs/), [EKS](https://aws.amazon.com/eks/faqs/), [Fargate](https://aws.amazon.com/fargate/faqs/), [Batch](https://aws.amazon.com/batch/faqs/), [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/faqs/), [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/faqs/), [Outposts](https://aws.amazon.com/outposts/rack/faqs/) |
| 04 Storage | [S3](https://docs.aws.amazon.com/s3/), [EBS](https://docs.aws.amazon.com/ebs/), [EFS](https://docs.aws.amazon.com/efs/), [FSx](https://docs.aws.amazon.com/fsx/), [Storage Gateway](https://docs.aws.amazon.com/storagegateway/) | [S3](https://aws.amazon.com/s3/faqs/), [EBS](https://aws.amazon.com/ebs/faqs/), [EFS](https://aws.amazon.com/efs/faq/), [FSx for Windows](https://aws.amazon.com/fsx/windows/faqs/), [FSx for Lustre](https://aws.amazon.com/fsx/lustre/faqs/), [FSx for NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/faqs/), [Storage Gateway](https://aws.amazon.com/storagegateway/faqs/), [AWS Backup](https://aws.amazon.com/backup/faqs/) |
| 05 Database | [RDS](https://docs.aws.amazon.com/rds/), [Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html), [DynamoDB](https://docs.aws.amazon.com/dynamodb/), [ElastiCache](https://docs.aws.amazon.com/elasticache/), [Redshift](https://docs.aws.amazon.com/redshift/) | [RDS](https://aws.amazon.com/rds/faqs/), [Aurora](https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq.html), [DynamoDB](https://aws.amazon.com/dynamodb/faqs/), [ElastiCache](https://aws.amazon.com/elasticache/faqs/), [DocumentDB](https://aws.amazon.com/documentdb/faqs/), [Neptune](https://aws.amazon.com/neptune/faqs/) |
| 06 Networking | [VPC](https://docs.aws.amazon.com/vpc/), [Route 53](https://docs.aws.amazon.com/route53/), [CloudFront](https://docs.aws.amazon.com/cloudfront/), [Direct Connect](https://docs.aws.amazon.com/directconnect/) | [VPC](https://aws.amazon.com/vpc/faqs/), [Transit Gateway](https://aws.amazon.com/transit-gateway/faqs/), [PrivateLink](https://aws.amazon.com/privatelink/faqs/), [Site-to-Site VPN](https://aws.amazon.com/vpn/faqs/), [Direct Connect](https://aws.amazon.com/directconnect/faqs/), [Route 53](https://aws.amazon.com/route53/faqs/), [CloudFront](https://aws.amazon.com/cloudfront/faqs/), [Global Accelerator](https://aws.amazon.com/global-accelerator/faqs/) |
| 07 Security | [KMS](https://docs.aws.amazon.com/kms/), [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/), [WAF and Shield](https://docs.aws.amazon.com/waf/), [GuardDuty](https://docs.aws.amazon.com/guardduty/), [Security documentation](https://docs.aws.amazon.com/security/) | [KMS](https://aws.amazon.com/kms/faqs/), [Secrets Manager](https://aws.amazon.com/secrets-manager/faqs/), [Certificate Manager](https://aws.amazon.com/certificate-manager/faqs/), [WAF](https://aws.amazon.com/waf/faqs/), [Shield](https://aws.amazon.com/shield/faqs/), [Firewall Manager](https://aws.amazon.com/firewall-manager/faqs/), [Network Firewall](https://aws.amazon.com/network-firewall/faqs/), [GuardDuty](https://aws.amazon.com/guardduty/faqs/), [Inspector](https://aws.amazon.com/inspector/faqs/), [Macie](https://aws.amazon.com/macie/faq/), [Security Hub](https://aws.amazon.com/security-hub/faqs/) |
| 08 Application Integration | [SQS](https://docs.aws.amazon.com/sqs/), [SNS](https://docs.aws.amazon.com/sns/), [EventBridge](https://docs.aws.amazon.com/eventbridge/), [Step Functions](https://docs.aws.amazon.com/step-functions/) | [SQS](https://aws.amazon.com/sqs/faqs/), [SNS](https://aws.amazon.com/sns/faqs/), [EventBridge](https://aws.amazon.com/eventbridge/faqs/), [Step Functions](https://aws.amazon.com/step-functions/faqs/), [Amazon MQ](https://aws.amazon.com/amazon-mq/faqs/), [AppSync](https://aws.amazon.com/appsync/faqs/), [API Gateway](https://aws.amazon.com/api-gateway/faqs/) |
| 09 Monitoring | [CloudWatch](https://docs.aws.amazon.com/cloudwatch/), [CloudTrail](https://docs.aws.amazon.com/cloudtrail/), [Config](https://docs.aws.amazon.com/config/), [Systems Manager](https://docs.aws.amazon.com/systems-manager/) | [CloudWatch](https://aws.amazon.com/cloudwatch/faqs/), [CloudTrail](https://aws.amazon.com/cloudtrail/faqs/), [Config](https://aws.amazon.com/config/faqs/), [Systems Manager](https://aws.amazon.com/systems-manager/faq/), [CloudFormation](https://aws.amazon.com/cloudformation/faqs/), [Trusted Advisor](https://aws.amazon.com/premiumsupport/faqs/) |
| 10 Migration | [DMS](https://docs.aws.amazon.com/dms/), [DataSync](https://docs.aws.amazon.com/datasync/), [Application Migration Service](https://docs.aws.amazon.com/mgn/), [Transfer Family](https://docs.aws.amazon.com/transfer/), [Snowball](https://docs.aws.amazon.com/snowball/) | [DMS](https://aws.amazon.com/dms/faqs/), [DataSync](https://aws.amazon.com/datasync/faqs/), [Application Migration Service](https://aws.amazon.com/application-migration-service/faqs/), [Transfer Family](https://aws.amazon.com/aws-transfer-family/faqs/), [Snowball](https://aws.amazon.com/snowball/faqs/) |
| 11 Analytics | [Athena](https://docs.aws.amazon.com/athena/), [Glue](https://docs.aws.amazon.com/glue/), [Kinesis](https://docs.aws.amazon.com/kinesis/), [EMR](https://docs.aws.amazon.com/emr/), [Quick Suite (QuickSight)](https://docs.aws.amazon.com/quick/) | [Athena](https://aws.amazon.com/athena/faqs/), [Glue](https://aws.amazon.com/glue/faqs/), [Lake Formation](https://aws.amazon.com/lake-formation/faqs/), [Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/faqs/), [Data Firehose](https://aws.amazon.com/firehose/faqs/), [Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/faqs/), [EMR](https://aws.amazon.com/emr/faqs/), [Redshift](https://aws.amazon.com/redshift/faqs/), [OpenSearch Service](https://aws.amazon.com/opensearch-service/faqs/), [QuickSight](https://aws.amazon.com/quick/quicksight/faqs/) |
| 12 Architecture Patterns | [Architecture Center](https://aws.amazon.com/architecture/) | [Caching](https://aws.amazon.com/caching/) |
| 13 Cost Optimization | [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) | [Savings Plans](https://aws.amazon.com/savingsplans/faqs/), [Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/faqs/), [Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/faqs/) |

## Architecture examples

| Source | Use it for |
|--------|------------|
| [AWS Architecture Center](https://aws.amazon.com/architecture/) | Reference architectures and best practices by industry and technology |
| [Reference architecture diagrams](https://docs.aws.amazon.com/reference-architecture-diagrams/) | One-page diagrams that show how services fit together |
| [AWS Solutions Library](https://aws.amazon.com/solutions/) | Deployable solutions with their architecture explained |
| [This Is My Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/) | Short videos of real customer designs |
| [Amazon Builders' Library](https://builder.aws.com/learn/topics/builders-library) | How Amazon builds resilient systems: timeouts, retries, backoff, static stability |
| [AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance/) | Migration and modernization patterns |

## Pricing, quotas and Regions

| Source | Use it for |
|--------|------------|
| [AWS Pricing](https://aws.amazon.com/pricing/) | Pricing models and per-service pricing pages |
| [AWS Pricing Calculator](https://calculator.aws/) | Estimating and comparing designs |
| [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) | Default limits per service |
| [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) | Viewing and raising limits |
| [Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) | Which services exist in which Region |

## Hands-on practice

| Source | Use it for |
|--------|------------|
| [AWS Free Tier](https://aws.amazon.com/free/) | A practice account. Set a budget alert before you start |
| [Hands-on tutorials](https://aws.amazon.com/getting-started/hands-on/) | Short guided builds |
| [AWS Workshops](https://builder.aws.com/build/workshops) | Longer self-paced labs by topic |
| [AWS re:Post](https://repost.aws/) and [Knowledge Center](https://repost.aws/knowledge-center) | Answers to specific "how do I" and troubleshooting questions |

## Staying current

The exam is updated when services change. Check these before your exam date.

| Source | Use it for |
|--------|------------|
| [What's New with AWS](https://aws.amazon.com/new/) | Launches and changes to limits and features |
| [AWS News Blog](https://aws.amazon.com/blogs/aws/) | Longer write-ups of major launches |
| [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/) | Design patterns and reference architectures in practice |
| [AWS Security Blog](https://aws.amazon.com/blogs/security/) | Security service changes and best practices |
| [AWS Events on YouTube](https://www.youtube.com/@AWSEventsChannel) | re:Invent and Summit sessions, for example the yearly architecture and networking deep dives |
| [Exam guide revisions](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) | Changes to the in-scope service list |

## Community study guides

Unofficial material. Use it alongside the sources above, not instead of them.

| Source | Notes |
|--------|-------|
| [ChathurangaVKD/AWS-Certified-Solutions-Architect-Associate-SAA-C03](https://github.com/ChathurangaVKD/AWS-Certified-Solutions-Architect-Associate-SAA-C03) | The MIT-licensed guide this repository is based on |
| [rdurelli/AWS-SAA-C03-Study-Guide](https://github.com/rdurelli/AWS-SAA-C03-Study-Guide) | Long-form notes per service; included here as the [`external/`](../external/) submodule |
| [keenanromain/AWS-SAA-C02-Study-Guide](https://github.com/keenanromain/AWS-SAA-C02-Study-Guide) | Notes for the previous exam version; most service content still applies |

## Third-party courses and practice tests

Widely used by SAA-C03 candidates. They are not affiliated with AWS or with this repository, some are paid, and they can lag behind AWS changes. Check anything that conflicts with the official sources above.

| Source | Format | Cost |
|--------|--------|------|
| [freeCodeCamp SAA-C03 course (Andrew Brown)](https://www.youtube.com/watch?v=c3Cn4xYfxJY) | Full video course | Free |
| [Tutorials Dojo AWS cheat sheets](https://tutorialsdojo.com/aws-cheat-sheets/) | Per-service summaries and comparisons | Free |
| [Ultimate AWS Certified Solutions Architect Associate (Stephane Maarek)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/) | Video course with slides | Paid |
| [Adrian Cantrill courses](https://learn.cantrill.io/) | In-depth video course with demos | Paid |
| [ExamPro SAA-C03](https://www.exampro.co/saa-c03) | Video course and practice exams | Free and paid tiers |
