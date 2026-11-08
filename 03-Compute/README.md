# Module 03: Compute Services

## Overview

AWS compute services for SAA-C03 exam: EC2, Lambda, containers, Auto Scaling, and Load Balancers.

**Exam Weight**: ~20-25%

---

## Key Services

1. **Amazon EC2** - Virtual servers
2. **AWS Lambda** - Serverless functions
3. **Auto Scaling** - Automatic capacity management
4. **Elastic Load Balancing** - Distribute traffic
5. **ECS/EKS/Fargate** - Container services
6. **Elastic Beanstalk** - PaaS deployment

---

## 1. Amazon EC2

### Instance Types (CRAM FACTS)
- **C** - Compute Optimized
- **R** - Memory Optimized (RAM)
- **M** - General Purpose (Medium)
- **T** - Burstable Performance
- **I/D/H** - Storage Optimized

### Pricing Models
| Model | Discount | Use Case |
|-------|----------|----------|
| On-Demand | None | Short-term, unpredictable |
| Reserved (1-3 yr) | Up to 72% | Steady state |
| Savings Plans | Up to 72% (EC2 Instance SP), up to 66% (Compute SP) | Flexible commitment |
| Spot | Up to 90% | Fault-tolerant workloads |
| Dedicated | None | Compliance, licensing |

### Placement Groups
- **Cluster**: Low latency, same AZ
- **Spread**: Max 7/AZ, critical apps
- **Partition**: Distributed apps (Hadoop, Kafka)

### Hibernate
- Saves the instance's RAM to the EBS root volume, then stops the instance. On start, RAM is reloaded and running processes resume. The instance keeps its ID, private IP and Elastic IP.
- Use it to pre-warm instances that take a long time to boot or to fill memory caches.
- Requirements: hibernation enabled at launch, an encrypted EBS root volume large enough to hold the RAM, and RAM under 150 GiB (Linux) or at most 16 GiB (Windows).
- Billing: no instance charge while hibernated, only EBS storage (including the saved RAM) and any Elastic IP.
- Stop clears RAM. Hibernate keeps it. Both keep EBS data. Neither keeps instance store data.

---

## 2. Auto Scaling

### Scaling Policies
1. **Target Tracking**: Maintain metric (e.g., CPU 50%)
2. **Step Scaling**: Add/remove based on alarms
3. **Scheduled**: Time-based scaling
4. **Predictive**: ML-based forecasting

### Key Concepts
- Min/Desired/Max capacity
- Health checks
- Lifecycle hooks
- Cooldown periods (default 300s)

---

## 3. Elastic Load Balancing

| Type | Layer | Use Case | Features |
|------|-------|----------|----------|
| ALB | 7 (HTTP/HTTPS) | Microservices, containers | Path/host routing, Lambda targets |
| NLB | 4 (TCP/UDP) | Extreme performance | Static IP, millions req/sec |
| GWLB | 3 (Network) | Virtual appliances | Firewalls, IDS |
| CLB | 4 & 7 | Legacy | Not recommended |

### Features
- Health checks
- Sticky sessions
- Cross-zone load balancing
- SSL/TLS termination

---

## 4. AWS Lambda

### Limits
- Max execution: **15 minutes**
- Memory: 128 MB - 10 GB
- /tmp storage: 512 MB - 10 GB
- Concurrent executions: 1,000 (default)

### Invocation Types
1. **Synchronous**: API Gateway, CLI
2. **Asynchronous**: S3, SNS, EventBridge
3. **Event Source Mapping**: SQS, Kinesis, DynamoDB Streams

### Pricing
- $0.20 per 1M requests
- $0.00001667 per GB-second

---

## 5. Container Services

### ECS (Elastic Container Service)
**Launch Types:**
- **EC2**: You manage instances
- **Fargate**: Serverless, AWS manages

**Components:**
- Task Definition
- Task
- Service
- Cluster

**IAM roles for ECS tasks:**
- **Task role**: permissions your application code uses (for example, read from S3 or DynamoDB)
- **Task execution role**: permissions the ECS agent uses to pull images from ECR and send logs to CloudWatch Logs
- Give each task its own task role; do not rely on the EC2 instance role for application permissions

### EKS (Elastic Kubernetes Service)
- Managed Kubernetes control plane
- Compatible with standard K8s tooling
- $0.10/hour per cluster in standard Kubernetes version support ($0.60/hour in extended support)
- Worker nodes: managed node groups, self-managed EC2, Fargate, or EKS Auto Mode
- Pods get AWS permissions through EKS Pod Identity or IAM roles for service accounts (IRSA)

### Fargate
- Serverless containers
- Works with ECS and EKS
- Billed per second for the vCPU and memory a task or pod requests (one-minute minimum for Linux tasks)

### ECR (Elastic Container Registry)
- Managed private registry for container images and OCI artifacts; ECR Public for public images
- Images are encrypted at rest; access is controlled with IAM and repository policies (for cross-account pulls)
- **Image scanning**: basic scanning, or enhanced scanning with Amazon Inspector for continuous vulnerability scanning
- **Lifecycle policies**: expire old or untagged images to control storage cost
- **Replication**: cross-Region and cross-account
- **Pull through cache**: cache images from upstream registries such as Docker Hub or Quay in ECR
- **Private subnets**: tasks with no internet access need interface endpoints for `ecr.api` and `ecr.dkr` plus an S3 gateway endpoint (image layers are stored in S3), or a NAT gateway

### Containers on premises
- **ECS Anywhere**: run ECS tasks on your own servers, managed from the ECS control plane
- **EKS Anywhere**: create and operate Kubernetes clusters on your own infrastructure with EKS tooling
- **EKS Distro**: the Kubernetes distribution EKS uses, for clusters you install and manage yourself

---

## 6. Other Services

### Elastic Beanstalk (PaaS)
- Deploy code, AWS handles infrastructure
- Supports: Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker
- Auto scaling, load balancing included

### AWS Batch
- Managed batch computing
- Automatic resource provisioning
- Uses Spot instances for cost savings

### Lightsail
- Simple VPS
- Fixed monthly pricing
- Pre-configured templates

### Amazon WorkSpaces
- Managed virtual desktops (Windows or Linux) streamed to users
- Replaces on-premises VDI. Integrates with AWS Directory Service and existing Active Directory
- Billed monthly or hourly per desktop

---

## Exam Tips

### Decision Tree
```
Need compute?
├─ Run code without servers? → Lambda
├─ Containers?
│  ├─ Without managing servers? → Fargate
│  ├─ With Kubernetes? → EKS
│  └─ AWS orchestration? → ECS
├─ Just deploy code? → Elastic Beanstalk
└─ Full control? → EC2
```

### Common Scenarios
- **Variable workload** → Auto Scaling + Spot
- **Lowest latency networking** → Cluster placement group
- **Content-based routing** → ALB
- **Millions of req/sec, static IP** → NLB
- **Steady 3-year workload** → Reserved Instances
- **Fault-tolerant batch job** → Spot Instances
- **Run code on events** → Lambda
- **Serverless containers** → Fargate

### Key Points
- EC2 instance store = ephemeral (lost on stop)
- EBS = persistent block storage (AZ-specific)
- T instances = burstable CPU
- Spot instances = 2-minute warning before termination
- Lambda max = 15 minutes
- ALB = Layer 7, content routing
- NLB = Layer 4, extreme performance
- Auto Scaling ensures min/max capacity

---

**Estimated Study Time**: 8-10 hours  
**Difficulty**: 3/3

[Previous: IAM](../02-IAM/README.md) | [Next: Storage ](../04-Storage/README.md) | [Main](../README.md)

