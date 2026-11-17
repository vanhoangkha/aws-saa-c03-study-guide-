# 13: Cost Optimization - Ultra Fast Learning

## AWS Pricing Fundamentals

### Pay-As-You-Go Model
- **No upfront costs**: Start/stop anytime
- **Pay for what you use**: Per second/hour/GB
- **No termination fees**: Cancel anytime

### Pricing Dimensions
1. **Compute**: Per second/hour (EC2, Lambda)
2. **Storage**: Per GB stored (S3, EBS)
3. **Data Transfer**:
   - **IN**: Free (most cases)
   - **OUT**: Charges apply
   - **Same region**: Often free
   - **Cross-region**: Charges apply

## AWS Free Tier

**Current model (accounts created on or after 15 July 2025)**: up to $200 in credits; free plan for 6 months or a paid plan; credits expire 12 months after account creation

### Legacy model (accounts created before 15 July 2025): three types

**1. Always Free**
- **Lambda**: 1M requests/month
- **DynamoDB**: 25 GB storage, 25 RCU/WCU
- **SNS**: 1M publishes/month
- **CloudWatch**: 10 metrics, 10 alarms
- **Cognito**: 10K MAUs (Lite/Essentials tiers)

**2. 12 Months Free** (accounts created before 15 July 2025)
- **EC2**: 750 hrs/month t2.micro (Linux/Windows)
- **S3**: 5 GB Standard storage
- **RDS**: 750 hrs/month db.t2.micro
- **EBS**: 30 GB

**3. Trials**
- **Inspector**: 15 days
- **QuickSight**: 30 days
- **Lightsail**: 1 month (Lightsail is out of scope for SAA-C03)

## EC2 Cost Optimization

### Pricing Models
| Model | Discount | Commitment | Use Case |
|-------|----------|------------|----------|
| On-Demand | 0% | None | Short, unpredictable |
| Savings Plans | Up to 72% | 1-3 years | Flexible workloads |
| Reserved | Up to 72% | 1-3 years | Steady state |
| Spot | Up to 90% | None | Fault-tolerant |
| Dedicated | 0% | None | Compliance |

### Savings Plans
- **Compute Savings Plans**: Most flexible (EC2, Fargate, Lambda) - up to 66%
- **EC2 Instance Savings Plans**: Specific instance family/region - up to 72%
- **Database Savings Plans**: Managed databases (RDS, Aurora, DynamoDB and more) - up to 35%, 1-year only
- **1 or 3 years**: Greater discount for longer term
- **Payment**: All upfront (max discount), partial upfront, no upfront

### Reserved Instances
- **Standard**: Up to 72% discount, can't change
- **Convertible**: Up to 66% discount, can be exchanged for a different family, OS or tenancy
- **Scheduled** (retired): No longer sold; use Capacity Reservations plus Savings Plans
- **Scope**: Regional or zonal
- **Marketplace**: Sell unused reservations

### Spot Instances
- **Up to 90% discount**
- **2-minute warning** before termination
- **Use cases**: Batch jobs, big data, stateless workloads
- **Spot Fleet**: Mix of Spot + On-Demand
- **Spot Block**: 1-6 hours (deprecated)

### Right-Sizing
- Match instance type to workload
- Use **CloudWatch** metrics to identify underutilized
- **Compute Optimizer**: ML-based recommendations
- Start small, scale up as needed

## Storage Cost Optimization

### S3 Storage Classes (Cost: Cheap → Expensive)
1. **S3 Glacier Deep Archive**: $1/TB/month
2. **S3 Glacier Flexible**: $3.6/TB/month
3. **S3 Glacier Instant**: $4/TB/month
4. **S3 One Zone-IA**: $10/TB/month
5. **S3 Standard-IA**: $12.5/TB/month
6. **S3 Intelligent-Tiering**: $4-23/TB/month across its automatic tiers, plus $0.0025 per 1,000 objects monitoring
7. **S3 Standard**: $23/TB/month

**Optimization**:
- **Lifecycle policies**: Auto-transition to cheaper classes
- **Intelligent-Tiering**: Unknown access patterns
- **Delete old data**: Expiration policies

### EBS Optimization
- **gp3**: Cheaper than gp2, better performance
- **Delete unattached volumes**
- **Snapshots**: Incremental, compress, delete old
- **Cold HDD (sc1)**: Cheapest for cold data

## Database Cost Optimization

### RDS
- **Reserved Instances**: Up to 69% discount
- **Stop instances**: Dev/test environments
- **Right-size**: Use CloudWatch metrics
- **Aurora Serverless**: Pay per second used
- **Read Replicas**: Cheaper than scaling master

### DynamoDB
- **On-Demand**: Unpredictable workloads
- **Provisioned**: Cheaper for predictable (use auto-scaling)
- **Reserved Capacity**: Up to 77% discount
- **Delete old data**: TTL (free)

## Data Transfer Optimization

### Minimize Costs
- **Same region**: Free for most services
- **Use CloudFront**: Cheaper than S3 direct
- **Gateway VPC Endpoints** (S3, DynamoDB): free, avoid NAT gateway processing charges
- **Direct Connect**: Cheaper for large volumes
- **S3 Transfer Acceleration**: Faster but costs more

### Data Transfer Pricing
- **IN**: Free
- **S3 → Internet**: $0.09/GB (first 10 TB, after 100 GB/month free)
- **S3 → CloudFront**: $0.00/GB
- **CloudFront → Internet**: $0.085/GB (cheaper!)

## AWS Cost Management Tools

### Cost Explorer
- **Visualize spending** over time
- **Filter**: By service, tag, account
- **Forecast**: Next 18 months
- **Reserved Instance recommendations**
- **Savings Plans recommendations**

### AWS Budgets
- **Set custom budgets**: Cost, usage, RI/SP utilization
- **Alerts**: SNS notifications when threshold exceeded
- **Types**: Cost, usage, reservation, savings plans
- **Free** without actions; first 2 action-enabled budgets free, then $0.10/day each

### Cost and Usage Report (CUR)
- **Most detailed** billing report
- **Hourly/daily/monthly** granularity
- **Store in S3**: Query with Athena
- **Integration**: QuickSight for visualization

### Cost Allocation Tags
- **Track costs** by project, team, environment
- **User-defined tags**: `project:website`
- **AWS-generated tags**: `aws:createdBy`
- **Activate tags** in Billing console
- **Tag resources** consistently

### AWS Compute Optimizer
- **ML-based recommendations** for EC2, EBS, Lambda
- **Right-sizing**: Identify over-provisioned resources
- **Free** (requires opt-in; enhanced infrastructure metrics are paid)
- **Supports**: EC2, Auto Scaling, EBS, Lambda

### Trusted Advisor
- **Cost optimization checks** (Business Support+, Enterprise Support or Unified Operations)
- Idle RDS, unattached ELBs, underutilized EC2
- **Basic Support**: service limit checks plus selected security and fault tolerance checks

## Cost Optimization Strategies

### 1. Turn Off Unused Resources
- Stop EC2 instances (dev/test)
- Delete unattached EBS volumes
- Delete old snapshots
- Remove unused Elastic IPs

### 2. Right-Size Resources
- Use Compute Optimizer
- Monitor CloudWatch metrics
- Start small, scale up

### 3. Purchase Commitments
- Savings Plans (most flexible)
- Reserved Instances (specific)
- Reserved Capacity (DynamoDB, RDS, Redshift)

### 4. Use Spot Instances
- Batch processing
- Big data workloads
- Stateless applications

### 5. Optimize Storage
- Lifecycle policies (S3)
- Delete old data
- Compress files
- Use cheaper storage classes

### 6. Optimize Data Transfer
- CloudFront for content delivery
- VPC Endpoints for AWS services
- Direct Connect for large volumes

### 7. Use Serverless
- Lambda (no idle capacity)
- DynamoDB On-Demand
- Aurora Serverless
- Fargate (no EC2 management)

### 8. Monitor and Alert
- Cost Explorer (visualize)
- Budgets (alert)
- Cost Anomaly Detection (ML)

## Billing & Pricing

### Consolidated Billing (Organizations)
- **One bill** for all accounts
- **Volume discounts**: Combined usage
- **Reserved Instance sharing**: Across accounts
- **Free** feature

### AWS Pricing Calculator
- **Estimate costs** before deployment
- **Configure services**: Instance types, storage, transfer
- **Export**: CSV, PDF
- **URL**: calculator.aws

### Support Plans
| Plan | Cost | Use Case |
|------|------|----------|
| Basic | Free | Everyone |
| Business Support+ | From $29/month | Dev and production workloads |
| Enterprise | From $5K/month | Mission-critical |
| Unified Operations | Contact AWS | Largest, most critical workloads |

Status (November 2026): Developer and Business Support closed to new subscriptions on 2 December 2025 and end on 1 January 2027 (Business Support+ replaces both). Enterprise On-Ramp also ends on 1 January 2027.

## Quick Exam Tips
- **Savings Plans**: Most flexible (up to 72%)
- **Reserved Instances**: Specific instance (up to 72%)
- **Spot**: Up to 90%, can be terminated
- **S3 Lifecycle**: Auto-transition to cheaper classes
- **Cost Explorer**: Visualize, forecast, recommendations
- **Budgets**: Set alerts (free); action-enabled budgets $0.10/day after the first 2
- **CUR**: Most detailed billing data
- **Tags**: Track costs by project/team
- **Compute Optimizer**: ML-based right-sizing
- **Consolidated Billing**: Combined usage, volume discounts
- **CloudFront**: Cheaper data transfer than S3 direct
- **Gateway VPC Endpoints**: Avoid NAT gateway charges for S3/DynamoDB
- **Trusted Advisor**: Cost optimization checks (Business Support+ and above)
- **Stop unused resources**: Biggest savings.
- **Free tier**: up to $200 credits for accounts from 15 July 2025; 12-month model for older accounts

