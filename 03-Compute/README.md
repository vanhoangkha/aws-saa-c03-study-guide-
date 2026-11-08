# Module 03: Compute Services

## Overview

AWS compute services for SAA-C03 exam: EC2, Lambda, containers, Auto Scaling, and Load Balancers.

The exam guide weights domains, not services: Secure Architectures 30%, Resilient Architectures 26%, High-Performing Architectures 24%, Cost-Optimized Architectures 20%. Compute topics appear in all four.

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
| Reserved (1-3 yr) | Up to 72% (Standard), up to 66% (Convertible) | Steady state |
| Savings Plans | Up to 72% (EC2 Instance SP), up to 66% (Compute SP) | Flexible commitment |
| Spot | Up to 90% | Fault-tolerant workloads |
| Dedicated Hosts | On-Demand per host, or up to 70% off with a Dedicated Host Reservation | Compliance, licensing |

### Placement Groups
- **Cluster**: Low latency, same AZ (same high-bisection network segment, not a single rack)
- **Spread**: Max 7 running instances per AZ per group, critical apps
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
- Cooldown periods (default 300s, used by simple scaling)

---

## 3. Elastic Load Balancing

| Type | Layer | Use Case | Features |
|------|-------|----------|----------|
| ALB | 7 (HTTP/HTTPS) | Microservices, containers | Path/host routing, Lambda targets |
| NLB | 4 (TCP/UDP) | Extreme performance | Static IP, millions req/sec |
| GWLB | 3 (Network) | Virtual appliances | Firewalls, IDS |
| CLB | 4 & 7 | Previous generation | Not recommended |

### Features
- Health checks
- Sticky sessions
- Cross-zone load balancing (ALB: always on at the load balancer, can be turned off per target group; NLB and GWLB: off by default)
- SSL/TLS termination

---

## 4. AWS Lambda

### Limits
- Max execution: **15 minutes**
- Memory: 128 MB - 10,240 MB (CPU scales with memory; 1,769 MB = 1 vCPU)
- /tmp storage: 512 MB - 10,240 MB
- Concurrent executions: 1,000 per Region (default, can be raised; new accounts may start lower)
- Deployment package: 50 MB zipped (direct upload), 250 MB unzipped including layers; container images up to 10 GB

### Invocation Types
1. **Synchronous**: API Gateway, CLI
2. **Asynchronous**: S3, SNS, EventBridge
3. **Event Source Mapping**: SQS, Kinesis, DynamoDB Streams

### Pricing (x86, US East (N. Virginia), first tier)
- $0.20 per 1M requests
- $0.0000166667 per GB-second
- Free tier: 1M requests and 400,000 GB-seconds per month

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

### EKS (Elastic Kubernetes Service)
- Managed Kubernetes
- Compatible with standard K8s
- $0.10 per cluster per hour while the Kubernetes version is in standard support, $0.60 in extended support

### Fargate
- Serverless containers
- Works with ECS and EKS
- Pay for the vCPU and memory a task or pod requests, per second

---

## 6. Other Services

### Elastic Beanstalk (PaaS)
- Deploy code, AWS handles infrastructure
- Supports: Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker
- Auto scaling, load balancing included

### AWS Batch
- Managed batch computing
- Automatic resource provisioning
- Can use EC2 On-Demand, Spot or Fargate capacity (Spot for cost savings)

### Lightsail
- Out of scope for SAA-C03 (listed as out of scope in the exam guide)
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
- EC2 instance store = ephemeral (lost on stop, hibernate or terminate)
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

## References

Pages this module was checked against (November 2026). The full list is in [docs/REFERENCES.md](../docs/REFERENCES.md).

- [Savings Plans and Reserved Instances (Cost Optimization whitepaper)](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/savings-plans.html)
- [Sell Reserved Instances in the RI Marketplace](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html)
- [EC2 placement strategies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-strategies.html)
- [EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)
- [Amazon EC2 T3 instances](https://aws.amazon.com/ec2/instance-types/t3/)
- [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- [Lambda pricing](https://aws.amazon.com/lambda/pricing/)
- [Lambda asynchronous invocation](https://docs.aws.amazon.com/help-panel/lambda/latest/console/configuration-async.html)
- [ALB target group health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html)
- [ALB target group attributes (cross-zone load balancing)](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html)
- [Amazon EKS extended support pricing](https://aws.amazon.com/blogs/containers/amazon-eks-extended-support-for-kubernetes-versions-pricing/)
- [The 7 Rs migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html)
- [Migrate an Amazon QLDB ledger to Amazon Aurora PostgreSQL](https://aws.amazon.com/blogs/database/migrate-an-amazon-qldb-ledger-to-amazon-aurora-postgresql/)

