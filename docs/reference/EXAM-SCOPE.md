# SAA-C03 Exam Scope

Which AWS services the exam can ask about, taken from the official [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) (version 1.1, published 29 October 2026), and where this guide covers each one.

AWS says both lists are non-exhaustive and subject to change. Check the exam guide's [Revisions](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-revisions.html) page before your exam: guide updates are published about one month before they reach the exam.

## Exam facts

| | |
|---|---|
| Questions | 65: 50 scored and 15 unscored. Unscored questions are not identified |
| Question types | Multiple choice (one correct of four) and multiple response (two or more correct of five or more) |
| Duration | 130 minutes |
| Scoring | Scaled 100-1,000, pass at 720. Compensatory: you need to pass the exam as a whole, not each domain. No penalty for guessing |
| Cost | 150 USD; 50% off your next AWS exam once you hold an active AWS certification |
| Validity | 3 years |
| Delivery | Pearson VUE test centre or online proctored |

Sources: [exam page](https://aws.amazon.com/certification/certified-solutions-architect-associate/), [exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).

## Domains

| Domain | Weight | Exam guide |
|--------|--------|------------|
| 1. Design Secure Architectures | 30% | [Task statements](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain1.html) |
| 2. Design Resilient Architectures | 26% | [Task statements](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain2.html) |
| 3. Design High-Performing Architectures | 24% | [Task statements](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html) |
| 4. Design Cost-Optimized Architectures | 20% | [Task statements](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain4.html) |

Since version 1.1, Amazon Elastic Transcoder is no longer in scope. The exam uses short service names (for example Amazon SNS); the in-exam Help lists the full names.

## In-scope services

The Modules column lists the modules that mention each service most. Services marked *light* are mentioned only a few times in this guide; see [Lightly covered services](#lightly-covered-services) below.

### Analytics

| Service | Modules | Note |
|---------|---------|------|
| Amazon Athena | [11](../../11-Analytics/README.md), [13](../../13-Cost-Optimization/README.md), [09](../../09-Monitoring/README.md) |  |
| AWS Data Exchange | [11](../../11-Analytics/README.md), [14](../../14-Practice/README.md) |  |
| AWS Data Pipeline | [11](../../11-Analytics/README.md), [12](../../12-Architecture-Patterns/README.md) | Closed to new customers and in maintenance mode. AWS recommends Step Functions, Glue or Amazon MWAA for new workloads. |
| Amazon EMR | [11](../../11-Analytics/README.md), [01](../../01-AWS-Fundamentals/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| AWS Glue | [11](../../11-Analytics/README.md), [05](../../05-Database/README.md), [08](../../08-Application-Integration/README.md) |  |
| Amazon Kinesis | [11](../../11-Analytics/README.md), [08](../../08-Application-Integration/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| AWS Lake Formation | [11](../../11-Analytics/README.md), [14](../../14-Practice/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| Amazon Managed Streaming for Apache Kafka (Amazon MSK) | [11](../../11-Analytics/README.md), [08](../../08-Application-Integration/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| Amazon OpenSearch Service | [11](../../11-Analytics/README.md), [14](../../14-Practice/README.md) |  |
| Amazon Quick | [11](../../11-Analytics/README.md), [13](../../13-Cost-Optimization/README.md), [12](../../12-Architecture-Patterns/README.md) | Formerly Amazon QuickSight; now part of Amazon Quick Suite. |
| Amazon Redshift | [11](../../11-Analytics/README.md), [05](../../05-Database/README.md), [08](../../08-Application-Integration/README.md) |  |

### Application Integration

| Service | Modules | Note |
|---------|---------|------|
| Amazon AppFlow | [08](../../08-Application-Integration/README.md), [14](../../14-Practice/README.md) |  |
| Amazon EventBridge | [08](../../08-Application-Integration/README.md), [07](../../07-Security/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| Amazon MQ | [08](../../08-Application-Integration/README.md) |  |
| Amazon SNS | [08](../../08-Application-Integration/README.md), [12](../../12-Architecture-Patterns/README.md), [09](../../09-Monitoring/README.md) |  |
| Amazon SQS | [08](../../08-Application-Integration/README.md), [12](../../12-Architecture-Patterns/README.md), [03](../../03-Compute/README.md) |  |
| AWS Step Functions | [08](../../08-Application-Integration/README.md), [12](../../12-Architecture-Patterns/README.md), [03](../../03-Compute/README.md) |  |

### AWS Cost Management

| Service | Modules | Note |
|---------|---------|------|
| AWS Budgets | [13](../../13-Cost-Optimization/README.md), [01](../../01-AWS-Fundamentals/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| AWS Cost and Usage Report | [13](../../13-Cost-Optimization/README.md), [01](../../01-AWS-Fundamentals/README.md), [11](../../11-Analytics/README.md) |  |
| AWS Cost Explorer | [13](../../13-Cost-Optimization/README.md), [01](../../01-AWS-Fundamentals/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| Savings Plans | [13](../../13-Cost-Optimization/README.md), [03](../../03-Compute/README.md), [14](../../14-Practice/README.md) |  |

### Compute

| Service | Modules | Note |
|---------|---------|------|
| AWS Batch | [03](../../03-Compute/README.md), [11](../../11-Analytics/README.md), [13](../../13-Cost-Optimization/README.md) |  |
| Amazon EC2 | [03](../../03-Compute/README.md), [13](../../13-Cost-Optimization/README.md), [02](../../02-IAM/README.md) |  |
| Amazon EC2 Auto Scaling | [03](../../03-Compute/README.md), [12](../../12-Architecture-Patterns/README.md), [13](../../13-Cost-Optimization/README.md) |  |
| AWS Elastic Beanstalk | [03](../../03-Compute/README.md), [01](../../01-AWS-Fundamentals/README.md), [14](../../14-Practice/README.md) |  |
| AWS Outposts | [03](../../03-Compute/README.md), [10](../../10-Migration/README.md), [11](../../11-Analytics/README.md) |  |
| AWS Serverless Application Repository | [03](../../03-Compute/README.md), [14](../../14-Practice/README.md) |  |
| VMware Cloud on AWS | [10](../../10-Migration/README.md), [03](../../03-Compute/README.md), [14](../../14-Practice/README.md) |  |
| AWS Wavelength | [01](../../01-AWS-Fundamentals/README.md), [03](../../03-Compute/README.md), [06](../../06-Networking/README.md) |  |

### Containers

| Service | Modules | Note |
|---------|---------|------|
| Amazon ECR | [07](../../07-Security/README.md), [03](../../03-Compute/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| Amazon ECS | [03](../../03-Compute/README.md), [12](../../12-Architecture-Patterns/README.md), [08](../../08-Application-Integration/README.md) |  |
| Amazon ECS Anywhere | [08](../../08-Application-Integration/README.md), [03](../../03-Compute/README.md), [14](../../14-Practice/README.md) |  |
| Amazon EKS | [03](../../03-Compute/README.md), [11](../../11-Analytics/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| Amazon EKS Anywhere | [03](../../03-Compute/README.md), [08](../../08-Application-Integration/README.md), [14](../../14-Practice/README.md) |  |
| Amazon EKS Distro | [14](../../14-Practice/README.md) | *Light.* |

### Database

| Service | Modules | Note |
|---------|---------|------|
| Amazon Aurora | [05](../../05-Database/README.md), [12](../../12-Architecture-Patterns/README.md), [10](../../10-Migration/README.md) |  |
| Amazon Aurora Serverless | [05](../../05-Database/README.md), [13](../../13-Cost-Optimization/README.md), [14](../../14-Practice/README.md) |  |
| Amazon DocumentDB | [05](../../05-Database/README.md), [07](../../07-Security/README.md), [10](../../10-Migration/README.md) |  |
| Amazon DynamoDB | [05](../../05-Database/README.md), [12](../../12-Architecture-Patterns/README.md), [14](../../14-Practice/README.md) |  |
| Amazon ElastiCache | [05](../../05-Database/README.md), [12](../../12-Architecture-Patterns/README.md), [14](../../14-Practice/README.md) |  |
| Amazon Keyspaces | [05](../../05-Database/README.md), [03](../../03-Compute/README.md), [14](../../14-Practice/README.md) |  |
| Amazon Neptune | [05](../../05-Database/README.md), [14](../../14-Practice/README.md), [10](../../10-Migration/README.md) |  |
| Amazon RDS | [05](../../05-Database/README.md), [12](../../12-Architecture-Patterns/README.md), [10](../../10-Migration/README.md) |  |
| Amazon Redshift | [11](../../11-Analytics/README.md), [05](../../05-Database/README.md), [08](../../08-Application-Integration/README.md) |  |

### Developer Tools

| Service | Modules | Note |
|---------|---------|------|
| AWS X-Ray | [09](../../09-Monitoring/README.md), [12](../../12-Architecture-Patterns/README.md), [14](../../14-Practice/README.md) |  |

### Front-End Web and Mobile

| Service | Modules | Note |
|---------|---------|------|
| AWS Amplify | [08](../../08-Application-Integration/README.md), [14](../../14-Practice/README.md) |  |
| Amazon API Gateway | [12](../../12-Architecture-Patterns/README.md), [08](../../08-Application-Integration/README.md), [07](../../07-Security/README.md) |  |
| AWS Device Farm | [08](../../08-Application-Integration/README.md), [14](../../14-Practice/README.md) |  |

### Machine Learning

| Service | Modules | Note |
|---------|---------|------|
| Amazon Comprehend | [11](../../11-Analytics/README.md), [05](../../05-Database/README.md), [14](../../14-Practice/README.md) |  |
| Amazon Lex | [11](../../11-Analytics/README.md), [14](../../14-Practice/README.md) | *Light.* |
| Amazon Polly | [11](../../11-Analytics/README.md), [14](../../14-Practice/README.md) |  |
| Amazon Rekognition | [11](../../11-Analytics/README.md), [14](../../14-Practice/README.md) | *Light.* |
| Amazon SageMaker AI | [11](../../11-Analytics/README.md), [13](../../13-Cost-Optimization/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| Amazon Textract | [11](../../11-Analytics/README.md), [14](../../14-Practice/README.md) |  |
| Amazon Transcribe | [11](../../11-Analytics/README.md), [14](../../14-Practice/README.md) | *Light.* |
| Amazon Translate | [11](../../11-Analytics/README.md) | *Light.* |

### Management and Governance

| Service | Modules | Note |
|---------|---------|------|
| AWS Auto Scaling | - | *Light.* |
| AWS CLI | [01](../../01-AWS-Fundamentals/README.md), [02](../../02-IAM/README.md), [09](../../09-Monitoring/README.md) |  |
| AWS CloudFormation | [01](../../01-AWS-Fundamentals/README.md), [09](../../09-Monitoring/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| AWS CloudTrail | [09](../../09-Monitoring/README.md), [07](../../07-Security/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |
| Amazon CloudWatch | [09](../../09-Monitoring/README.md), [08](../../08-Application-Integration/README.md), [13](../../13-Cost-Optimization/README.md) |  |
| AWS Compute Optimizer | [13](../../13-Cost-Optimization/README.md), [12](../../12-Architecture-Patterns/README.md), [14](../../14-Practice/README.md) |  |
| AWS Config | [09](../../09-Monitoring/README.md), [07](../../07-Security/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |
| AWS Control Tower | [01](../../01-AWS-Fundamentals/README.md) |  |
| AWS Health Dashboard | [09](../../09-Monitoring/README.md), [07](../../07-Security/README.md), [10](../../10-Migration/README.md) |  |
| AWS License Manager | [01](../../01-AWS-Fundamentals/README.md), [14](../../14-Practice/README.md) | *Light.* |
| Amazon Managed Grafana | [05](../../05-Database/README.md) | *Light.* |
| Amazon Managed Service for Prometheus | - | *Light.* |
| AWS Management Console | [01](../../01-AWS-Fundamentals/README.md), [02](../../02-IAM/README.md), [09](../../09-Monitoring/README.md) |  |
| AWS Organizations | [01](../../01-AWS-Fundamentals/README.md), [13](../../13-Cost-Optimization/README.md), [07](../../07-Security/README.md) |  |
| AWS Proton | [14](../../14-Practice/README.md) | *Light.* AWS ended support for Proton on 7 October 2026; the exam guide still lists it. |
| AWS Service Catalog | [01](../../01-AWS-Fundamentals/README.md), [14](../../14-Practice/README.md) | *Light.* |
| AWS Systems Manager | [09](../../09-Monitoring/README.md), [07](../../07-Security/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |
| AWS Well-Architected Tool | [12](../../12-Architecture-Patterns/README.md), [14](../../14-Practice/README.md) | *Light.* |

### Media Services

| Service | Modules | Note |
|---------|---------|------|
| Amazon Kinesis Video Streams | [11](../../11-Analytics/README.md), [08](../../08-Application-Integration/README.md), [14](../../14-Practice/README.md) |  |

### Migration and Transfer

| Service | Modules | Note |
|---------|---------|------|
| AWS Application Discovery Service | [10](../../10-Migration/README.md) |  |
| AWS Application Migration Service | [10](../../10-Migration/README.md), [03](../../03-Compute/README.md), [14](../../14-Practice/README.md) |  |
| AWS DataSync | [10](../../10-Migration/README.md), [04](../../04-Storage/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| AWS DMS | [10](../../10-Migration/README.md), [05](../../05-Database/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| AWS Snow Family | [10](../../10-Migration/README.md), [04](../../04-Storage/README.md), [03](../../03-Compute/README.md) |  |
| AWS Transfer Family | [10](../../10-Migration/README.md), [14](../../14-Practice/README.md) |  |

### Networking and Content Delivery

| Service | Modules | Note |
|---------|---------|------|
| AWS Client VPN | [14](../../14-Practice/README.md), [06](../../06-Networking/README.md) | *Light.* |
| Amazon CloudFront | [06](../../06-Networking/README.md), [12](../../12-Architecture-Patterns/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |
| AWS Direct Connect | [06](../../06-Networking/README.md), [07](../../07-Security/README.md), [10](../../10-Migration/README.md) |  |
| Elastic Load Balancing (ELB) | [03](../../03-Compute/README.md), [12](../../12-Architecture-Patterns/README.md), [06](../../06-Networking/README.md) |  |
| AWS Global Accelerator | [06](../../06-Networking/README.md), [07](../../07-Security/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| AWS PrivateLink | [06](../../06-Networking/README.md), [01](../../01-AWS-Fundamentals/README.md), [03](../../03-Compute/README.md) |  |
| Amazon Route 53 | [06](../../06-Networking/README.md), [12](../../12-Architecture-Patterns/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |
| AWS Site-to-Site VPN | [07](../../07-Security/README.md), [06](../../06-Networking/README.md), [14](../../14-Practice/README.md) |  |
| AWS Transit Gateway | [06](../../06-Networking/README.md), [01](../../01-AWS-Fundamentals/README.md), [14](../../14-Practice/README.md) |  |
| Amazon VPC | [06](../../06-Networking/README.md), [01](../../01-AWS-Fundamentals/README.md), [07](../../07-Security/README.md) |  |

### Security, Identity, and Compliance

| Service | Modules | Note |
|---------|---------|------|
| AWS Artifact | [07](../../07-Security/README.md), [14](../../14-Practice/README.md) |  |
| AWS Certificate Manager (ACM) | [07](../../07-Security/README.md), [06](../../06-Networking/README.md), [14](../../14-Practice/README.md) |  |
| AWS CloudHSM | [07](../../07-Security/README.md), [14](../../14-Practice/README.md) |  |
| Amazon Cognito | [12](../../12-Architecture-Patterns/README.md), [02](../../02-IAM/README.md), [08](../../08-Application-Integration/README.md) |  |
| Amazon Detective | [07](../../07-Security/README.md), [01](../../01-AWS-Fundamentals/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| AWS Directory Service | [07](../../07-Security/README.md), [03](../../03-Compute/README.md), [14](../../14-Practice/README.md) |  |
| AWS Firewall Manager | [07](../../07-Security/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |
| Amazon GuardDuty | [07](../../07-Security/README.md), [09](../../09-Monitoring/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |
| AWS IAM Identity Center | [02](../../02-IAM/README.md), [07](../../07-Security/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |
| Amazon Inspector | [07](../../07-Security/README.md), [13](../../13-Cost-Optimization/README.md), [14](../../14-Practice/README.md) |  |
| AWS KMS | [07](../../07-Security/README.md), [04](../../04-Storage/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| Amazon Macie | [07](../../07-Security/README.md), [14](../../14-Practice/README.md) |  |
| AWS Network Firewall | [07](../../07-Security/README.md) |  |
| AWS Resource Access Manager (AWS RAM) | [01](../../01-AWS-Fundamentals/README.md) |  |
| AWS Secrets Manager | [07](../../07-Security/README.md), [14](../../14-Practice/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |
| AWS Security Hub | [07](../../07-Security/README.md), [09](../../09-Monitoring/README.md), [14](../../14-Practice/README.md) |  |
| AWS Shield | [07](../../07-Security/README.md), [06](../../06-Networking/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| AWS WAF | [07](../../07-Security/README.md), [06](../../06-Networking/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| IAM | [02](../../02-IAM/README.md), [07](../../07-Security/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |

### Serverless

| Service | Modules | Note |
|---------|---------|------|
| AWS Fargate | [03](../../03-Compute/README.md), [13](../../13-Cost-Optimization/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| AWS Lambda | [08](../../08-Application-Integration/README.md), [12](../../12-Architecture-Patterns/README.md), [03](../../03-Compute/README.md) |  |

### Storage

| Service | Modules | Note |
|---------|---------|------|
| AWS Backup | [10](../../10-Migration/README.md), [05](../../05-Database/README.md), [12](../../12-Architecture-Patterns/README.md) |  |
| Amazon EBS | [04](../../04-Storage/README.md), [13](../../13-Cost-Optimization/README.md), [07](../../07-Security/README.md) |  |
| Amazon EFS | [04](../../04-Storage/README.md), [10](../../10-Migration/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |
| Amazon FSx (for all types) | [04](../../04-Storage/README.md), [10](../../10-Migration/README.md), [14](../../14-Practice/README.md) |  |
| Amazon S3 | [04](../../04-Storage/README.md), [11](../../11-Analytics/README.md), [13](../../13-Cost-Optimization/README.md) |  |
| Amazon S3 Glacier | [04](../../04-Storage/README.md), [13](../../13-Cost-Optimization/README.md), [14](../../14-Practice/README.md) |  |
| AWS Storage Gateway | [10](../../10-Migration/README.md), [04](../../04-Storage/README.md), [01](../../01-AWS-Fundamentals/README.md) |  |

## Lightly covered services

What each one is, at the level the exam expects, with the official page to read.

| Service | What to know |
|---------|--------------|
| [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) | One scaling plan across several resource types: EC2 Auto Scaling groups, ECS services, DynamoDB tables and indexes, Aurora replicas, Spot Fleets. Use EC2 Auto Scaling for EC2 groups on their own |
| [Amazon EKS Distro](https://aws.amazon.com/eks/eks-distro/) | The Kubernetes distribution EKS uses, for running your own clusters anywhere. EKS Anywhere adds AWS-supported tooling for on-premises clusters |
| [Amazon Lex](https://aws.amazon.com/lex/) | Chatbots and voice bots (speech recognition plus natural-language understanding) |
| [Amazon Rekognition](https://aws.amazon.com/rekognition/) | Image and video analysis: objects, faces, text, unsafe content |
| [Amazon Transcribe](https://aws.amazon.com/transcribe/) | Speech to text |
| [Amazon Translate](https://aws.amazon.com/translate/) | Text translation between languages |
| [AWS License Manager](https://aws.amazon.com/license-manager/) | Tracks and enforces software licence usage (for example per-core or per-socket licences) across AWS and on premises |
| [Amazon Managed Grafana](https://aws.amazon.com/grafana/) | Managed Grafana dashboards over CloudWatch, Prometheus, OpenSearch and other data sources |
| [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) | Managed, Prometheus-compatible metrics for containers, typically EKS |
| [AWS Proton](https://aws.amazon.com/proton/) | Lets platform teams publish standard infrastructure templates that developers deploy from. AWS ended support on 7 October 2026 |
| [AWS Service Catalog](https://aws.amazon.com/servicecatalog/) | Approved CloudFormation-based products that users can launch without broad IAM permissions |
| [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/) | Reviews a workload against the Well-Architected pillars and tracks the improvement plan |
| [AWS Client VPN](https://aws.amazon.com/vpn/client-vpn/) | Managed OpenVPN-based remote access for individual users. Site-to-Site VPN connects networks instead |

## Out-of-scope services

AWS lists these as out of scope. Modules may still mention them for context.

| Category | Services |
|----------|----------|
| Application Integration | Amazon Managed Workflows for Apache Airflow (Amazon MWAA) |
| Compute | Amazon Lightsail |
| Database | Amazon RDS on VMware |
| Developer Tools | AWS CDK, AWS CloudShell, AWS CodeArtifact, AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, Amazon Corretto, AWS Fault Injection Simulator (AWS FIS), AWS Tools and SDKs |
| Front-End Web and Mobile | Amazon Location Service |
| Game Tech | Amazon GameLift |
| Internet of Things | All services |
| Machine Learning | Apache MXNet on AWS, AWS Deep Learning AMIs (DLAMI), AWS Deep Learning Containers, Amazon HealthLake, AWS Inferentia, Amazon Personalize, PyTorch on AWS, TensorFlow on AWS |
| Management and Governance | AWS Console Mobile Application, AWS Distro for OpenTelemetry |
| Media Services | AWS Elemental Appliances and Software, AWS Elemental MediaConnect, AWS Elemental MediaConvert, AWS Elemental MediaLive, AWS Elemental MediaPackage, AWS Elemental MediaTailor, Amazon Interactive Video Service (Amazon IVS) |
| Migration and Transfer | Migration Evaluator |
| Networking and Content Delivery | AWS Cloud Map |
| Quantum Technologies | Amazon Braket |
| Satellite | AWS Ground Station |

Source: [Out-of-scope AWS services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-out-of-scope-services.html).
