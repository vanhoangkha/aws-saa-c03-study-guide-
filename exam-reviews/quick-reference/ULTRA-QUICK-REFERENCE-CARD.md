# AWS SAA-C03 - ULTRA QUICK REFERENCE CARD (100% COVERAGE)

**Complete edge-case coverage for exam day success - Print or save on your phone**

**Updated:** March 2, 2026  
**Coverage:** All services + 150+ edge cases + advanced scenarios + exam strategies  
**Purpose:** Final 30-minute review before exam + quick reference during study

---

## WHAT'S INCLUDED

 **15 Must-Memorize Critical Rules**  
 **150+ Edge Cases & Traps** (commonly missed scenarios)  
 **Advanced Exam Scenarios** (pattern recognition for complex questions)  
 **Service Combinations** (what pairs with what)  
 **Anti-Patterns** (what NOT to do - eliminates wrong answers)  
 **Performance/Security/Cost Optimization Patterns**  
 **30-Second Question Analysis Method** (time management)  
 **Top 20 Gotcha Facts** (most commonly failed questions)  
 **Numerical Values to Memorize** (limits that appear on exam)  
 **Service Confusion Clarification** (similar services explained)  
 **Exam Day Strategies** (before/during/after tactics)  

---

## MUST MEMORIZE (15 Critical Rules)

1. **CloudFront + ACM cert** = us-east-1 ONLY
2. **Memory metric** = Need CloudWatch agent (not default)
3. **S3 minimum storage** = IA 30 days, Glacier IR/Flexible 90, Deep Archive 180
4. **Multi-AZ** = HA (sync) | **Read Replica** = Scale (async)
5. **IAM evaluation** = DENY always wins (SCP beats IAM)
6. **ECS dynamic ports** = ALB or NLB + awsvpc/bridge (not CLB)
7. **Instance store** = Lost on stop/terminate
8. **VPC peering DNS** = Enable in BOTH VPCs
9. **Glacier transitions** = Cannot go OUT without restore
10. **Bucket default class** = Only NEW objects (not existing)
11. **SCPs** = DON'T affect management account
12. **File Gateway** = S3 objects (admins can access), Volume = blocks only
13. **RDS IAM Auth** = Token 15 min, MySQL/MariaDB/PostgreSQL/Aurora only
14. **SQS FIFO** = 300 msg/s (3000 batched), ends in `.fifo`
15. **Aurora Global** = <1s lag, <1 min failover (cross-region HA)

---

## SERVICE SELECTION (Quick Decision)

### Caching
- **Redis**: Persistence, HA, Multi-AZ, complex data
- **Memcached**: Simple, multi-threaded, no persistence
- **DAX**: DynamoDB only, microsecond latency

### Storage
- **FSx Lustre**: HPC, ML (100s GB/s)
- **FSx Windows**: SMB, Active Directory
- **EFS**: Linux shared filesystem
- **S3**: Object storage

### Global Services
- **CloudFront**: HTTP/HTTPS, caching, CDN
- **Global Accelerator**: Static IP, TCP/UDP, non-HTTP

### Database HA
- **RDS Multi-AZ**: Same region, auto-failover (1-2 min)
- **Aurora Global**: Cross-region, <1s lag, <1 min failover
- **DynamoDB Global**: Multi-region, multi-write

### Messaging & Integration
- **Queue (1-to-1, pull)**: SQS
- **Pub/Sub (1-to-many, push)**: SNS
- **Ordered + Exactly-once**: SQS FIFO
- **Real-time streaming**: Kinesis Data Streams
- **Load to S3/Redshift**: Amazon Data Firehose (ex-Kinesis Data Firehose)
- **Event routing**: EventBridge
- **Workflow orchestration**: Step Functions
- **JMS/AMQP migration**: Amazon MQ

### Hybrid & Migration
- **Hybrid file storage**: Storage Gateway
- **File migration**: DataSync (10x faster)
- **DB migration**: DMS + SCT (if different engine)
- **Physical transfer < 10TB**: Snowcone (retired)
- **Physical transfer 10-80TB**: Snowball Edge (closed to new customers)
- **Physical transfer > 10PB**: Snowmobile (retired)
- **Snow Family status**: no devices for new customers; use DataSync or AWS Data Transfer Terminal
- **SFTP to S3**: Transfer Family

### Multi-Account Management
- **Centralized billing**: AWS Organizations
- **Enforce policies**: Service Control Policies (SCPs)
- **Automated setup**: Control Tower
- **Share resources**: Resource Access Manager (RAM)

### VPC Connectivity
- **VPC Endpoint Gateway**: S3/DynamoDB (FREE)
- **VPC Endpoint Interface**: Other services ($0.01/hr)
- **Transit Gateway**: >10 VPCs, hub-spoke
- **VPC Peering**: Simple 1-to-1

### VPC Advanced Features
- **Flow Logs**: Capture all traffic (accepted + rejected), VPC/Subnet/ENI level
- **DNS Settings**: enableDnsHostnames + enableDnsSupport (both needed for peering)
- **Private Link**: Expose service privately via NLB + VPC endpoint
- **NAT Gateway**: Managed NAT, HA per AZ, 5 Gbps, scales to 100 Gbps
- **NAT Instance**: EC2-based, self-managed, cheaper but not HA
- **Internet Gateway**: 1 per VPC, scales automatically
- **Egress-Only IGW**: IPv6 outbound only
- **Direct Connect**: Dedicated network (1-10 Gbps), consistent latency
- **DX + VPN**: DX primary, VPN backup/failover, BGP routing
- **VPN**: Site-to-Site VPN over internet (up to 1.25 Gbps)

---

## COST OPTIMIZATION

- **Cost Explorer**: Visualize costs, forecasting, RI recommendations
- **Cost Allocation Tags**: Track costs by project/team/environment
- **Budgets**: Set custom budgets, alerts
- **Compute Optimizer**: Right-sizing recommendations
- **Trusted Advisor**: Cost optimization checks (Business/Enterprise support)
- **S3 Intelligent-Tiering**: Auto-move between access tiers, no retrieval fees
- **S3 Lifecycle Policies**: Auto-transition to cheaper storage classes
- **Reserved Instances**: Up to 72% discount (1-3 year commitment)
- **Savings Plans**: Up to 72% discount, more flexible than RIs
- **Spot Instances**: Up to 90% discount, can be interrupted
- **RDS Reserved Instances**: Up to 69% discount

---
- **Athena**: Query S3 with SQL
- **Glue Crawler**: Discover schemas
- **QuickSight**: BI dashboards

### Secrets
- **Secrets Manager**: Auto-rotation, RDS integration
- **Parameter Store**: Simple, free, no auto-rotation

### AWS Organizations & SCPs
- **Management Account**: Cannot be restricted by SCPs, pays all bills
- **Member Accounts**: Subject to SCPs, inherit from OUs
- **SCPs**: Maximum permissions (don't grant), preventive control
- **SCP Formula**: Effective = IAM policy AND SCP
- **Common SCP Uses**: Region restrict, require encryption, prevent org exit

### Storage Gateway (Hybrid Storage)
- **File Gateway**: NFS/SMB → S3 objects (admins can access via console)
- **Volume Gateway Cached**: Primary in S3, cache local
- **Volume Gateway Stored**: Primary local, async backup to S3
- **Tape Gateway**: Virtual tapes → S3 Glacier (backup software)

### Migration & Transfer
- **DataSync**: Automated file transfer (NFS/SMB → S3/EFS/FSx), 10x faster
- **DMS**: Database migration, minimal downtime, CDC
- **SCT**: Schema Conversion Tool (different DB engines)
- **Snowcone** (retired): 8 TB, edge computing, portable
- **Snowball Edge** (closed to new customers): 80 TB, large migrations
- **Snowmobile** (retired): 100 PB, exabyte-scale (literal truck!)
- **Snow Family status**: no devices for new customers; use DataSync or AWS Data Transfer Terminal
- **Transfer Family**: SFTP/FTPS → S3/EFS

### Application Integration
- **SQS Standard**: Unlimited throughput, at-least-once, best-effort order
- **SQS FIFO**: 300 msg/s, exactly-once, ordered, name ends `.fifo`
- **SNS**: Pub/Sub, push to multiple targets, fan-out
- **EventBridge**: Event-driven, 20+ targets, scheduled/AWS events
- **Step Functions**: Orchestrate workflows, visual, error handling
- **Kinesis Data Streams**: Real-time, custom processing, replay
- **Kinesis Firehose**: Load to S3/Redshift, near real-time, managed

---

## KEY NUMBERS

| What | Value |
|------|-------|
| S3 IA minimum | 30 days |
| Auto Scaling cooldown | 5 min (300s) |
| Glacier Expedited | 1-5 min |
| Glacier Standard | 3-5 hours |
| Glacier Bulk | 5-12 hours |
| Deep Archive Standard | 12 hours |
| Deep Archive Bulk | 48 hours |
| Aurora Global lag | <1 second |
| RDS Multi-AZ failover | 1-2 minutes |
| IAM token validity | 15 minutes |
| Lambda@Edge timeout | 30 seconds |
| CloudFront Functions | <1 millisecond |
| Kinesis retention default | 1 day (max 365) |
| API Gateway RPS | 10,000 steady, 5,000 burst |
| VPC Peering limit | 50 per VPC default (max 125) |
| Spread placement | 7 instances per AZ |
| Partition placement | 7 partitions per AZ |
| S3 multipart max parts | 10,000 |
| EBS io2 max IOPS | 256,000 |
| EBS io2 Block Express | 256,000 IOPS |
| gp3 base IOPS | 3,000 |
| gp3 base throughput | 125 MB/s |
| SQS FIFO throughput | 300 msg/s (3,000 batched) |
| Snowcone capacity (retired) | 8 TB (HDD) / 14 TB (SSD) |
| Snowball Edge (closed to new customers) | 80 TB model discontinued 2024 |
| Snowmobile (retired) | 100 PB per truck |
| S3 Transfer Acceleration | 50-500% faster |
| S3 performance | 3,500 PUT/s, 5,500 GET/s per prefix |

---

## STORAGE CLASSES (Cheapest → Most Expensive)

1. S3 Glacier Deep Archive ($0.00099/GB) CHEAPEST
2. S3 Glacier Flexible ($0.004/GB)
3. S3 Intelligent-Tiering ($0.0025-0.023/GB)
4. S3 One Zone-IA ($0.01/GB)
5. S3 Standard-IA ($0.0125/GB)
6. S3 Standard ($0.023/GB)

---

## EC2 INSTANCE TYPES (Quick Guide)

- **C5/C6** = Compute-optimized (CPU heavy)
- **M5/M6** = General purpose (balanced)
- **R5/R6** = Memory-optimized (RAM heavy)
- **T3/T4** = Burstable (variable, cheap)
- **I3/I4** = Storage-optimized (IOPS)
- **G4/P3** = GPU (ML, graphics)

---

## EC2 ADVANCED FEATURES

- **Instance Metadata**: http://169.254.169.254/latest/meta-data/
- **Public IP**: Changes on stop/start (use Elastic IP for static)
- **ENA**: Elastic Network Adapter (up to 100 Gbps)
- **EFA**: Elastic Fabric Adapter (HPC, MPI, inter-node)
- **Enhanced Networking**: SR-IOV for high bandwidth, low latency
- **Instance Store**: Ephemeral storage, lost on stop/terminate
- **EBS-Optimized**: Dedicated bandwidth for EBS
- **T3 Unlimited**: Burst above baseline (pay extra)

---

## EC2 PRICING MODELS

| Model | Discount | Flexibility | Use Case |
|-------|----------|-------------|----------|
| On-Demand | 0% | Full | Variable workloads |
| Standard RI | 72% | None | Steady state |
| Convertible RI | 66% | Change type | Some flexibility |
| Savings Plans | 66-72% | High | Flexible commitment |
| Spot | 90% | Can interrupt | Fault-tolerant |

---

## ROUTING POLICIES (Route 53)

- **Simple**: One resource
- **Weighted**: % traffic split (A/B testing)
- **Latency**: Lowest latency region
- **Failover**: Primary/secondary + health checks
- **Geolocation**: User's country/continent
- **Geoproximity**: Distance + bias (-99 to +99)
- **Multi-value**: Multiple IPs + health checks

### Route 53 Health Checks

- **Endpoint**: HTTP/HTTPS/TCP health check
- **Calculated**: Combine multiple health checks (AND/OR/NOT)
- **CloudWatch Alarm**: Based on CloudWatch metrics

---

## CLOUDWATCH MONITORING

- **Default EC2 Metrics**: CPU, Network, Disk ops (NO memory/disk space)
- **CloudWatch Agent**: Required for memory, disk space, custom metrics
- **Agent aggregation_dimensions**: Define metric dimensions
- **Cross-Account**: Share metrics for central monitoring
- **Logs Retention**: Indefinite by default (not 7 days)
- **Alarms**: Metric-based, composite, anomaly detection
- **Dashboards**: Custom metric visualization
- **EventBridge (CloudWatch Events)**: Event-driven automation

---

## CLOUDFRONT ADVANCED

- **Origin Access Control (OAC)**: Access private S3 without public bucket (OAI is legacy)
- **Origin Failover**: Primary + secondary origin, automatic failover
- **Cache Behaviors**: Path-based routing (/api/*, /images/*), priority order
- **Signed URLs**: Single file access, include expiration/IP
- **Signed Cookies**: Multiple files, don't change URLs
- **Custom Error Pages**: Custom HTML for 4xx/5xx errors
- **Cache Invalidation**: First 1000 paths free/month, then $0.005/path
- **Geo-Restriction**: Whitelist/blacklist countries
- **Lambda@Edge**: Run code at edge (30s timeout)
- **CloudFront Functions**: Lightweight (<1ms), viewer request/response

---

## LOAD BALANCERS

| Feature | ALB | NLB | CLB |
|---------|-----|-----|-----|
| Layer | 7 (HTTP) | 4 (TCP) | 4 & 7 |
| Static IP | No | Yes | No |
| Path routing | Yes | No | No |
| ECS dynamic ports | Yes | Yes | No |
| WebSockets | Yes | Yes | No |
| Performance | Good | Extreme | Legacy |

### ALB Advanced Features
- **Path-Based Routing**: Route by URL path, query strings, headers
- **Host-Based Routing**: Multiple domains on one ALB
- **Cognito Integration**: Offload authentication to ALB
- **Lambda Targets**: Invoke Lambda from ALB
- **IP as Targets**: Route to on-premises via IP
- **Slow Start Mode**: Gradual traffic increase to new targets
- **Sticky Sessions**: Route to same target (session affinity)
- **Connection Draining**: Complete in-flight requests before terminating

### NLB Features
- **Static IP**: One static IP per AZ
- **Preserve Source IP**: Client IP visible to targets
- **TLS Termination**: Decrypt at NLB
- **Ultra-Low Latency**: Millions of requests/sec
- **TCP/UDP/TLS**: Layer 4 protocols
- **PrivateLink**: Expose services privately

---

## EBS VOLUME TYPES

| Type | IOPS | Throughput | Use Case |
|------|------|------------|----------|
| gp3 | 3K-80K | 125-2,000 MiB/s | General |
| gp2 | 3 IOPS/GB | Up to 250 MB/s | Legacy |
| io2 | Up to 256K | Up to 4,000 MB/s | High perf (all Block Express) |
| io1 | Up to 64K | Up to 1000 MB/s | Older |
| st1 | 500 | 500 MB/s | Throughput |
| sc1 | 250 | 250 MB/s | Cold data |

**Key Points:**
- **SSD (gp/io)**: Small random I/O, transactional workloads, databases
- **HDD (st/sc)**: Large sequential I/O, big data, cannot be boot volumes
- **gp3**: Most cost-effective for general workloads, tune IOPS/throughput independently
- **io2**: 99.999% durability, critical databases

---

## FSx FILE SYSTEMS

- **FSx for Windows**: SMB, Active Directory, Multi-AZ, DFS, shadow copies
- **FSx for Lustre**: HPC, ML, 100s GB/s, S3 integration, data repository tasks
- **FSx for NetApp ONTAP**: NFS, SMB, iSCSI, multi-protocol
- **FSx for OpenZFS**: Linux, snapshots, compression

### FSx for Lustre Deployment Types
- **Scratch**: Temporary, 6x faster, no replication
- **Persistent**: Long-term, HA, auto-replication

---

## ELASTICACHE

### Redis vs Memcached

| Feature | Redis | Memcached |
|---------|-------|-----------|
| Persistence | Yes | No |
| Replication | Yes (Multi-AZ) | No |
| Backup/Restore | Yes | No |
| Data Types | Advanced (sorted sets, lists) | Simple (strings) |
| Multi-threaded | No | Yes |
| Pub/Sub | Yes | No |
| Use Case | HA, persistence, complex | Simple, multi-core, distributed |

### DAX (DynamoDB Accelerator)
- **DynamoDB-only** cache
- **Microsecond** latency (vs milliseconds)
- **Drop-in compatible** with DynamoDB API
- **Write-through** caching

---

## DATABASE ADVANCED FEATURES

### RDS Features
- **Multi-AZ**: Sync replication, auto-failover (1-2 min), same region HA
- **Read Replicas**: Async, read scaling, can be cross-region, up to 15
- **IAM Auth**: Token-based (15 min), MySQL/MariaDB/PostgreSQL/Aurora only
- **Storage Auto Scaling**: Auto-increase when <10% free
- **Blue/Green Deployments**: Test on clone, 1-min switchover
- **Enhanced Monitoring**: OS-level metrics (1-60 second intervals)
- **Performance Insights**: Database performance monitoring

### Aurora Features
- **Aurora Global Database**: <1s replication lag, <1 min failover, 10 secondary regions (2025, was 5)
- **Aurora Serverless**: Auto-scales ACUs, pay per second, intermittent workloads
- **Aurora Multi-Master**: Retired (Aurora MySQL 5.6 only, single Region)
- **Backtrack**: Rewind to point in time (no restore needed)
- **Parallel Query**: Faster analytical queries
- **Cloning**: Fast DB clones (copy-on-write)

### DynamoDB
- **Auto Scaling**: Target 70% utilization
- **Global Tables**: Multi-region, multi-active, last-writer-wins
- **Streams**: Change data capture, 24-hour retention
- **On-Demand**: Pay per request (vs Provisioned)
- **Transactions**: ACID support
- **TTL**: Auto-delete expired items

---

## PLACEMENT GROUPS

- **Cluster**: Single AZ, low latency (10 Gbps), HPC
- **Spread**: Max 7/AZ, isolated, critical apps
- **Partition**: 7 partitions/AZ, Hadoop/Kafka

---

## ECS & CONTAINERS

- **Task Definition**: Blueprint (image, CPU, memory, ports, IAM roles)
- **Dynamic Port Mapping**: ALB + awsvpc/bridge network mode
- **ECS on Outposts**: On-premises AWS (vs Local Zones for low latency)
- **Fargate**: Serverless containers, no EC2 management
- **EC2 Launch Type**: More control, Reserved Instance savings

---

## AUTO SCALING

- **Target Tracking**: Maintain metric at target (e.g., 70% CPU)
- **Step Scaling**: Different actions for different thresholds
- **Scheduled Scaling**: Predictable load patterns
- **Cooldown**: 5 min default, prevents rapid scaling
- **Standby State**: Upgrade instance without traffic
- **Lifecycle Hooks**: Custom actions during launch/terminate

---

## SECURITY COMPARISON

### Security Group vs NACL

| Feature | Security Group | NACL |
|---------|---------------|------|
| Level | Instance | Subnet |
| State | Stateful | Stateless |
| Rules | Allow only | Allow + Deny |
| Evaluation | All rules | Numbered order |

### Encryption Options

| Type | Who Manages | Key Location |
|------|-------------|--------------|
| SSE-S3 | AWS | AWS |
| SSE-KMS | AWS KMS | KMS |
| SSE-C | You | Your systems |
| Client-side | You | You encrypt |

### Security Services

- **GuardDuty**: Threat detection (CloudTrail, VPC Flow, DNS logs)
- **AWS Config**: Compliance monitoring, auto-remediation
- **Security Hub**: Centralized security findings
- **WAF**: Web Application Firewall, rate-based rules, geo-blocking
- **Shield**: DDoS protection (Standard free, Advanced paid)
- **Inspector**: EC2/container vulnerability scanning
- **Macie**: S3 data classification, PII detection

---

## S3 ADVANCED FEATURES

- **Multipart Upload**: Use >100MB, required >5GB
- **Transfer Acceleration**: 50-500% faster, use s3-accelerate endpoint
- **Byte-Range Fetches**: Parallel downloads, resume on failure
- **Pre-Signed URLs**: Temporary access, configurable expiry
- **Object Lock**: Compliance (can't delete), Governance (can bypass)
- **Bucket Keys (SSE-KMS)**: Reduce KMS calls by 99%
- **Cross-Region Replication**: Versioning required, new objects only
- **Requester Pays**: Requester pays transfer, owner pays storage
- **Block Public Access**: 4 settings (account + bucket level)
- **Server Access Logging**: Must enable manually

---

## LAMBDA DEPLOYMENT

- **Version**: Immutable snapshot
- **$LATEST**: Mutable, current code
- **Alias**: Pointer to version(s)
- **Weighted alias**: Split traffic (10% v2, 90% v1)

### Lambda Advanced Features
- **Provisioned Concurrency**: Pre-warmed instances, no cold starts
- **Reserved Concurrency**: Limit max concurrent executions
- **Environment Variables**: Can be encrypted with KMS
- **Layers**: Share code/libraries across functions (up to 5 layers)
- **Extensions**: Integrate monitoring, security tools
- **Lambda@Edge**: Run at CloudFront edge locations (30s timeout)
- **CloudFront Functions**: Lightweight (<1ms), viewer request/response only

### Lambda Limits
- **Memory**: 128 MB - 10 GB (1 MB increments)
- **Timeout**: Max 15 minutes
- **Deployment Package**: 50 MB (zipped), 250 MB (unzipped)
- **Concurrent Executions**: 1000 per region (can request increase)
- **/tmp Storage**: 512 MB - 10 GB

---

## API GATEWAY

- **REST API**: HTTP/HTTPS APIs, full feature set
- **HTTP API**: Lower latency, lower cost (70% cheaper), simpler
- **WebSocket API**: Two-way communication, real-time
- **Edge-Optimized**: CloudFront distribution (default)
- **Regional**: Same region as API
- **Private**: VPC endpoint only
- **Throttling**: 10,000 RPS steady-state, 5,000 burst (returns 429)
- **Caching**: TTL 0-3600 seconds
- **Stage Variables**: Environment-specific configuration
- **Canary Deployments**: Test new versions with % traffic

---

## IAM & COGNITO

### IAM Key Concepts
- **IAM User**: Long-term credentials, specific person/service
- **IAM Role**: Temporary credentials, assumed by entities
- **IAM Policy**: JSON document defining permissions
- **IAM Group**: Collection of users with shared permissions
- **Permission Boundaries**: Maximum permissions a user can have
- **Policy Evaluation**: Explicit DENY → Explicit ALLOW → Implicit DENY

### Federation
- **SAML 2.0**: Enterprise identity (Active Directory, ADFS)
- **Web Identity**: Social logins (Google, Facebook, Amazon)
- **AWS SSO (IAM Identity Center)**: Multi-account centralized access
- **Custom Identity Broker**: Custom authentication + STS

### Cognito
- **User Pools**: User directory, authentication (sign-up/sign-in)
- **Identity Pools**: Authorization, temporary AWS credentials
- **Social Identity Providers**: Google, Facebook, Amazon, Apple
- **SAML Identity Providers**: Enterprise federation
- **Use Case**: User Pools (authenticate WHO), Identity Pools (authorize WHAT)

---

## WELL-ARCHITECTED FRAMEWORK (6 Pillars)

### 1. Operational Excellence
- **Design Principles**: IaC, annotate documentation, small reversible changes, refine procedures, anticipate failure, learn from failures
- **Key Services**: CloudFormation, Config, CloudWatch, CloudTrail, X-Ray

### 2. Security
- **Design Principles**: Strong identity foundation, traceability, security at all layers, automate security, protect data in transit/at rest, least privilege
- **Key Services**: IAM, Cognito, KMS, CloudTrail, GuardDuty, Security Hub, WAF, Shield

### 3. Reliability
- **Design Principles**: Test recovery, auto-recover, scale horizontally, stop guessing capacity, manage change through automation
- **Key Services**: Multi-AZ, Auto Scaling, Route 53, Backup, CloudFormation

### 4. Performance Efficiency
- **Design Principles**: Use advanced technologies, go global in minutes, use serverless, experiment, consider mechanical sympathy
- **Key Services**: CloudFront, Lambda, Auto Scaling, EBS types, ElastiCache

### 5. Cost Optimization
- **Design Principles**: Adopt consumption model, measure efficiency, stop spending on data center, analyze expenditure, use managed services
- **Key Services**: Cost Explorer, RIs, Savings Plans, S3 lifecycle, Auto Scaling

### 6. Sustainability
- **Design Principles**: Understand impact, establish goals, maximize utilization, adopt efficient hardware, use managed services, reduce downstream impact
- **Key Services**: EC2 Auto Scaling, Graviton processors, Lambda, S3 Intelligent-Tiering

---

## DISASTER RECOVERY (DR) STRATEGIES

**RTO** (Recovery Time Objective): How quickly to recover  
**RPO** (Recovery Point Objective): How much data loss acceptable

| Strategy | RTO | RPO | Cost | When to Use |
|----------|-----|-----|------|-------------|
| **Backup & Restore** | Hours-Days | Hours | Low | Non-critical, cost-sensitive |
| **Pilot Light** | 10min-Hours | Minutes | Medium | Important, some downtime OK |
| **Warm Standby** | Minutes | Seconds | High | Business-critical |
| **Multi-Site** | Real-time | Near-zero | Highest | Mission-critical, zero downtime |

### Implementation Details
- **Backup & Restore**: Daily backups to S3, deploy from scratch during disaster
- **Pilot Light**: DB replica running, AMIs ready, scale up during disaster
- **Warm Standby**: Scaled-down full stack (30% capacity), scale to 100% on DR
- **Multi-Site**: Full capacity in multiple regions, Route 53 active-active

---

## ELASTIC BEANSTALK DEPLOYMENT

| Strategy | Downtime | Cost | Risk | Rollback |
|----------|----------|------|------|----------|
| All at once | Yes | Low | High | Manual |
| Rolling | No | Low | Medium | Manual |
| Rolling + batch | No | Medium | Medium | Manual |
| Immutable | No | High | Low | Quick |
| Blue/Green | No | High | Lowest | Instant |

---

## EDGE CASES & ADVANCED SCENARIOS (100% Coverage)

### VPC & Networking Edge Cases

**No: TRAP: VPC peering is transitive**
- Yes: TRUTH: NOT transitive. A-B and B-C doesn't mean A-C
- Solution: Use Transit Gateway for hub-spoke

**No: TRAP: VPC peering works across different CIDR**
- Yes: TRUTH: CIDRs cannot overlap
- Yes: Example: 10.0.0.0/16 can peer with 10.1.0.0/16, NOT with 10.0.0.0/8 (overlap)

**No: TRAP: Route table automatically updated with peering**
- Yes: TRUTH: Must manually add routes in BOTH VPCs
- Yes: Action: Add destination CIDR → peering connection target

**No: TRAP: Security groups reference works cross-region**
- Yes: TRUTH: Only works within same region
- Cross-region: Must use CIDR blocks

**No: TRAP: NAT Gateway supports port forwarding**
- TRUTH: Only supports outbound. Use bastion host for inbound
- Yes: Bastion: EC2 in public subnet with SSH access

**No: TRAP: VPC Flow Logs capture packet contents**
- TRUTH: Metadata only (IPs, ports, protocol). Use packet sniffer for content
- Yes: Can't capture: DHCP, AWS DNS, metadata (169.254.169.254)

**No: TRAP: Can attach multiple internet gateways to VPC**
- Yes: TRUTH: Only ONE internet gateway per VPC
- Yes: IGW scales automatically, highly available

**No: TRAP: Private subnet can access internet via IGW**
- Yes: TRUTH: Needs NAT Gateway/Instance in public subnet
- Yes: Route: private subnet → NAT (in public) → IGW → internet

**No: TRAP: Direct Connect provides encryption by default**
- TRUTH: NOT encrypted. Use VPN over Direct Connect for encryption
- Yes: Or: Application-level encryption (TLS/SSL)

**TRAP: VPN connection limited to 1.25 Gbps cannot be increased**
- TRUTH: Use ECMP with Transit Gateway for 2.5 Gbps (2 tunnels)
- Yes: VPG: No ECMP support. TGW: Supports ECMP

### S3 Edge Cases

**No: TRAP: S3 versioning can be completely disabled**
- Yes: TRUTH: Once enabled, can only SUSPEND (not disable)
- Yes: Delete marker: Created when object deleted with versioning

**No: TRAP: S3 Standard-IA cheaper for all infrequent access**
- Yes: TRUTH: Need >128KB objects accessed <1x/month
- Yes: <128KB or frequent access: Standard is cheaper

**No: TRAP: S3 lifecycle immediately transitions objects**
- Yes: TRUTH: 30 days in Standard before Standard-IA/One Zone-IA; Glacier classes any time
- Yes: Standard → Glacier Deep Archive directly is allowed; minimum storage durations still apply

**No: TRAP: Restored Glacier object stays in Standard**
- Yes: TRUTH: Copy stays for specified days, then deletes
- Yes: Original remains in Glacier. Must copy to keep in Standard

**No: TRAP: S3 Cross-Region Replication retroactive**
- Yes: TRUTH: Only NEW objects after enabling
- Existing: Use S3 Batch Replication

**TRAP: S3 encryption can be changed without re-upload**
- Yes: TRUTH: Must copy object in-place to change encryption
- Yes: Command: aws s3 cp s3://bucket/key s3://bucket/key --sse...

**No: TRAP: MFA Delete protects against all deletes**
- Yes: TRUTH: Only protects version deletion + versioning suspension
- Yes: Delete markers: Can be created without MFA

**No: TRAP: S3 Select retrieves whole object then filters** (S3 Select closed to new customers; use Athena)
- Yes: TRUTH: Filters at S3 level, retrieves only needed data (up to 400% faster)
- Use for: CSV, JSON, Parquet queries

**No: TRAP: S3 Transfer Acceleration always faster**
- Yes: TRUTH: Test first. May be slower for nearby regions
- Yes: AWS provides speed comparison tool

**No: TRAP: Requester Pays works with anonymous requests**
- Yes: TRUTH: Requires authenticated AWS account
- Yes: Requester pays: Transfer + request costs. Owner pays: Storage

### RDS & Database Edge Cases

**No: TRAP: RDS Multi-AZ standby can be used for reads**
- TRUTH: Standby NOT accessible. Use Read Replicas for reads
- Yes: Multi-AZ: HA only. Read Replica: Read scaling

**No: TRAP: RDS Multi-AZ automatic failover is instant**
- Yes: TRUTH: 1-2 minutes failover time
- Yes: DNS name stays same, endpoints automatically switch

**No: TRAP: Read Replica promotion is instant**
- Yes: TRUTH: Stops replication, creates independent database
- Yes: Can take several minutes depending on data volume

**No: TRAP: RDS cross-region read replica requires Multi-AZ**
- Yes: TRUTH: Can create from single-AZ source
- Yes: Cross-region replica: Async replication, higher lag

**No: TRAP: RDS encryption can be enabled on existing database**
- Yes: TRUTH: Must create snapshot, copy encrypted, restore from encrypted
- Yes: Not possible: no encrypted read replica of an unencrypted DB

**No: TRAP: RDS automated backups persist after deletion**
- Yes: TRUTH: Deleted with instance (unless retain option set)
- Yes: Manual snapshots: Persist until explicitly deleted

**No: TRAP: Aurora Global Database has zero replication lag**
- Yes: TRUTH: <1 second lag (typically <1s, not zero)
- Yes: Cross-region: Physical replication, not logical

**No: TRAP: Aurora Serverless scales instantly**
- Yes: TRUTH: Scaling takes seconds (not instant)
- Yes: During scaling: Connections preserved (no downtime)

**No: TRAP: DynamoDB strongly consistent reads default**
- Yes: TRUTH: Eventually consistent by default
- Yes: Strong: Costs 2× RCU, specify in API call

**No: TRAP: DynamoDB LSI can be added after table creation**
- Yes: TRUTH: LSI only at creation. GSI can be added anytime
- Yes: LSI: Max 5. GSI: Max 20

**No: TRAP: DynamoDB auto-scales instantly**
- Yes: TRUTH: CloudWatch triggers scaling (few minutes delay)
- Yes: On-Demand: Instant, but 2× cost of provisioned

**No: TRAP: DynamoDB Global Tables have eventual consistency**
- Yes: TRUTH: Typically <1 second. Last writer wins for conflicts
- Yes: All regions: Read and write capability

### EC2 & Compute Edge Cases

**TRAP: Stopped EC2 instance no longer charged**
- Yes: TRUTH: EBS volumes still charged. Also: Elastic IPs charged when not attached
- Yes: Terminate: Stops all charges (except snapshots)

**No: TRAP: Instance store backed AMI can be stopped**
- Yes: TRUTH: Can only terminate (data lost)
- Yes: EBS-backed: Can stop (EBS persists)

**No: TRAP: All EC2 instance types available in all AZs**
- Yes: TRUTH: Some instance types limited to specific AZs
- Yes: Check: AWS docs or try launching

**No: TRAP: Placement groups span across regions**
- Yes: TRUTH: Single AZ only (cluster), or same region (spread/partition)
- Yes: Cluster: Single AZ for 10 Gbps. Spread: 7/AZ max

**No: TRAP: Enhanced networking enabled by default**
- Yes: TRUTH: Requires specific AMI + instance type
- Yes: Check: Instance type must support ENA or Intel 82599 VF

**TRAP: EC2 IAM role can be changed without restart**
- Yes: TRUTH: Can be changed without restart (added capability)
- Yes: New credentials: Available within seconds

**No: TRAP: Spot instance interruption gives hours of notice**
- Yes: TRUTH: Only 2 minutes warning via instance metadata
- Yes: Poll: http://169.254.169.254/latest/meta-data/spot/termination-time

**No: TRAP: Reserved Instance applied to stopped instances**
- Yes: TRUTH: Only running instances. Stopped = waste RI benefit
- Yes: Stop RI: Still paying for reservation

**No: TRAP: Convertible RI can change to different family freely**
- Yes: TRUTH: Can change, but must be equal or greater value
- Yes: Exchange fee: None, but discount up to 66% (vs 72%)

### Lambda Edge Cases

**No: TRAP: Lambda can run indefinitely**
- Yes: TRUTH: Max 15 minutes (900 seconds)
- Yes: Long tasks: Step Functions, ECS, Batch

**No: TRAP: Lambda has unlimited concurrent executions**
- Yes: TRUTH: 1,000 per region default (can request increase)
- Yes: Reserved concurrency: Guarantees but limits max

**No: TRAP: Lambda VPC mode has same performance as non-VPC**
- Yes: TRUTH: VPC cold starts slower (now improved with Hyperplane ENI)
- Yes: VPC: Needed to access private resources (RDS, ElastiCache)

**No: TRAP: Lambda@Edge runs at all CloudFront events**
- Yes: TRUTH: 4 events: viewer request/response, origin request/response
- Yes: Viewer: Edge location. Origin: Regional edge cache

**No: TRAP: Lambda automatically retries all failed invocations**
- Yes: TRUTH: Async only (S3, SNS). Sync (API Gateway): Application must retry
- Yes: DLQ: Configure for failed async invocations

**No: TRAP: Lambda environment variables stored securely**
- Yes: TRUTH: Encrypted at rest but visible in console
- Yes: Sensitive: Encrypt with KMS, decrypt in code

### ECS & Container Edge Cases

**No: TRAP: ECS dynamic port mapping works with CLB**
- Yes: TRUTH: ALB and NLB support it. Only CLB requires static ports
- Yes: Network mode: awsvpc or bridge (not host)

**No: TRAP: Fargate cheaper than EC2 launch type**
- Yes: TRUTH: Usually 20-30% more expensive
- Fargate: No instance management. EC2: Can use RIs/Spot

**No: TRAP: ECS service auto-replaces failed tasks immediately**
- Yes: TRUTH: Health check grace period (default 0, can set up to 7200s)
- Yes: Before grace period: Won't mark unhealthy

**No: TRAP: ECS task IAM role applies to all containers**
- Yes: TRUTH: Task role = all containers. Can't set per-container
- Multiple roles: Use separate task definitions

### Auto Scaling Edge Cases

**No: TRAP: Auto Scaling launches instances immediately**
- Yes: TRUTH: Cooldown period prevents rapid scaling (default 300s)
- Yes: Simple scaling: Waits full cooldown. Target tracking: Smarter

**No: TRAP: Auto Scaling health checks immediate**
- Yes: TRUTH: Grace period (default 300s). Won't terminate during grace
- Yes: Set based on app startup time

**No: TRAP: Termination policy random**
- Yes: TRUTH: Follows policy: oldest launch config, closest to billing hour, etc.
- Yes: Custom: Set termination policy in ASG settings

**No: TRAP: ASG spans regions**
- Yes: TRUTH: Single region only. Multiple AZs within region
- Cross-region: Use CloudFormation StackSets

**No: TRAP: Standby instances count toward min capacity**
- Yes: TRUTH: Don't count. ASG launches replacements
- Use: Troubleshoot, upgrade, then return to InService

### Load Balancer Edge Cases

**No: TRAP: ALB supports UDP traffic**
- Yes: TRUTH: HTTP/HTTPS/gRPC only (Layer 7)
- UDP: Use NLB (Layer 4)

**No: TRAP: Cross-zone load balancing free for all LBs**
- Yes: TRUTH: ALB = free. NLB = charged. CLB = optional (free if enabled)
- Yes: Recommendation: Enable for even distribution

**No: TRAP: Sticky sessions work with path-based routing**
- Yes: TRUTH: Works, but session cookie applies to entire ALB
- Better: Use external session store (ElastiCache, DynamoDB)

**No: TRAP: ALB can route to Lambda + EC2 in same target group**
- Yes: TRUTH: Target group must be homogeneous (all Lambda OR all IP)
- Different targets: Use multiple target groups + rules

**No: TRAP: NLB preserves source IP by default**
- TRUTH: YES by default for instance targets. IP targets: NO for TCP/TLS, YES for UDP
- Yes: IP targets (TCP/TLS): Enable preserve client IP attribute

**No: TRAP: Load balancer security group blocks outbound by default**
- Yes: TRUTH: Default SG outbound rule allows all; add rules only if you removed it
- Yes: Pattern: LB SG outbound → Target SG inbound from LB SG

### CloudFront & CDN Edge Cases

**No: TRAP: CloudFront caches everything**
- Yes: TRUTH: Respects Cache-Control headers. Default TTL: 24 hours
- Yes: Don't cache: Set Cache-Control: no-cache

**No: TRAP: CloudFront origin failover automatic**
- Yes: TRUTH: Must configure origin group (primary + secondary)
- Yes: Failover triggers: chosen status codes (500/502/503/504, 403/404), timeouts

**No: TRAP: CloudFront signed URLs work indefinitely**
- Yes: TRUTH: Must set expiration time
- Yes: Canned policy: URL + expiration. Custom: URL + conditions + expiration

**No: TRAP: CloudFront cache invalidation free**
- Yes: TRUTH: First 1,000 paths/month free, then $0.005/path
- Better: Use versioned file names (file-v2.js)

**No: TRAP: CloudFront serves from nearest edge**
- Yes: TRUTH: Considers latency, not just distance
- Yes: May route to farther edge if better performance

**No: TRAP: Lambda@Edge can modify response body**
- TRUTH: YES, but 1MB limit on body size
- Yes: Viewer request/response: 40KB limit

### Route 53 Edge Cases

**No: TRAP: Route 53 health checks free**
- Yes: TRUTH: $0.50/month per health check
- Yes: Fast interval (10s): $1.00/month

**No: TRAP: Alias records work with any AWS service**
- Yes: TRUTH: Only specific services (ELB, CloudFront, S3 website, Elastic Beanstalk, API Gateway)
- EC2: Must use A record with IP (not alias)

**No: TRAP: Weighted routing splits traffic exactly**
- Yes: TRUTH: Approximate. DNS caching affects precision
- Better precision: Use ALB weighted target groups

**No: TRAP: Geolocation routing uses IP geolocation**
- Yes: TRUTH: Uses DNS resolver's location (may differ from user)
- Yes: VPN/proxy: May route incorrectly

**No: TRAP: Route 53 resolves private hosted zone from internet**
- Yes: TRUTH: Only from associated VPCs
- Hybrid: Use Route 53 Resolver for on-premises access

### IAM & Security Edge Cases

**No: TRAP: IAM user can have unlimited policies**
- Yes: TRUTH: Default 10 managed policies per user/group, 20 per role (adjustable)
- Workaround: Use groups, consolidate policies

**No: TRAP: IAM role session duration default 1 hour**
- Yes: TRUTH: Default 1 hour, max 12 hours (can configure)
- Yes: Federation: Max session duration set in trust policy

**No: TRAP: Resource-based policy trumps IAM policy**
- Yes: TRUTH: IAM + resource policy = union (both allow works)
- Except: Explicit deny always wins

**No: TRAP: MFA works for all API calls**
- Yes: TRUTH: Only specific actions (e.g., delete). Check policy conditions
- Yes: STS GetSessionToken: Can enforce MFA for temp credentials

**No: TRAP: AWS Organizations SCP overrides IAM**
- Yes: TRUTH: SCP + IAM = intersection (both must allow)
- Yes: Management account: SCPs don't apply

**No: TRAP: S3 bucket policy allows all actions with s3:***
- TRUTH: Yes, but can be dangerous. Use least privilege
- Yes: Better: s3:GetObject, s3:PutObject specifically

**No: TRAP: KMS CMK can be shared across accounts freely**
- Yes: TRUTH: Must grant in key policy AND IAM policy in target account
- Yes: Both required: Key policy allows, IAM policy uses

**No: TRAP: SSM Parameter Store free for all parameters**
- Yes: TRUTH: Standard = free (4KB max). Advanced = $0.05/param/month (8KB max)
- Yes: Standard: No parameter policies. Advanced: Has policies

### Storage Gateway Edge Cases

**No: TRAP: File Gateway files immediately in S3**
- Yes: TRUTH: Async upload. Local cache first, then S3
- Yes: Notification: S3 event when upload complete

**No: TRAP: Volume Gateway can be accessed from S3 console**
- Yes: TRUTH: Stored as EBS snapshots, not S3 objects
- Yes: File Gateway: Objects visible in S3

**No: TRAP: Tape Gateway integrates with all backup software**
- TRUTH: Must support iSCSI VTL (most enterprise software does)
- Yes: Examples: Veeam, Commvault, Veritas

**No: TRAP: Storage Gateway needs dedicated EC2 instance**
- Yes: TRUTH: Can run on-premises VM or EC2
- Yes: On-prem: VMware, Hyper-V, KVM. Cloud: EC2

### Kinesis Edge Cases

**No: TRAP: Kinesis Data Streams unlimited throughput**
- Yes: TRUTH: 1MB/s or 1000 records/s per shard
- Scale: Add more shards or use on-demand mode

**No: TRAP: Kinesis Firehose real-time**
- Yes: TRUTH: Near real-time (buffer can be 0 s since 2023)
- Real-time: Use Data Streams

**No: TRAP: Kinesis Data Streams retains data indefinitely**
- Yes: TRUTH: 1 day default, max 365 days
- Yes: After retention: Data lost (not in S3 automatically)

**No: TRAP: Enhanced fan-out free**
- Yes: TRUTH: $0.015/shard-hour + $0.013/GB
- Yes: Standard: Shared 2MB/s. Enhanced: Dedicated 2MB/s per consumer

**No: TRAP: Kinesis automatically handles resharding**
- TRUTH: Must manually split/merge shards (or use on-demand)
- Yes: On-demand: Auto-scales (4 MB/s write per shard)

### SQS Edge Cases

**No: TRAP: SQS guarantees ordering**
- TRUTH: Standard = best-effort. FIFO = guaranteed
- Yes: Standard: At-least-once delivery (duplicates possible)

**No: TRAP: SQS FIFO unlimited throughput**
- Yes: TRUTH: 300 msg/s default (3,000 batched); high-throughput mode raises it well beyond (Region-dependent)
- Need more: Enable high throughput for FIFO + many message group IDs

**No: TRAP: Long polling always better than short polling**
- Yes: TRUTH: Long polling reduces costs but delays message delivery
- Yes: Long: Wait up to 20s. Short: Returns immediately (even if empty)

**No: TRAP: Dead-letter queue works automatically**
- Yes: TRUTH: Must configure redrive policy (max receives)
- Yes: DLQ: Separate queue, must manually process or delete

**No: TRAP: Visibility timeout applies per message**
- TRUTH: YES, and can be changed per message (0s to 12 hours)
- Yes: Default: 30 seconds. Max: 12 hours

### Migration & Transfer Edge Cases

**No: TRAP: DataSync works with any protocol**
- Yes: TRUTH: NFS, SMB, or S3 API only
- Other protocols: Use custom scripts or third-party tools

**No: TRAP: Snowball supports all AWS services**
- Yes: TRUTH: S3 compatible, some EC2 AMI support
- Yes: No: Direct EBS, RDS, or other service imports

**No: TRAP: DMS handles schema conversion automatically**
- TRUTH: Use Schema Conversion Tool (SCT) for heterogeneous migrations
- Yes: Homogeneous (MySQL→MySQL): DMS only. Heterogeneous (Oracle→PostgreSQL): SCT + DMS

**No: TRAP: DMS migration is instant**
- Yes: TRUTH: Full load + CDC (change data capture)
- Yes: Phases: Full load → ongoing replication → cutover

### Well-Architected Edge Cases

**No: TRAP: Well-Architected has mandatory requirements**
- TRUTH: Best practices framework (not compliance standard)
- Use: Design guidance, not audit checklist

**No: TRAP: Cost optimization means cheapest always**
- Yes: TRUTH: Balance cost with performance, security, reliability
- Yes: Example: Multi-AZ costs more but provides HA

**No: TRAP: Reliability means zero downtime**
- Yes: TRUTH: Meet defined SLAs and graceful degradation
- Yes: Design for failure, not for perfection

---

## ADVANCED EXAM SCENARIOS (Pattern Recognition)

### Scenario Pattern Recognition

**Keywords → Solution Mapping**

| When Question Says | They Really Want |
|-------------------|------------------|
| "Minimize operational overhead" | Managed service, serverless, not self-managed |
| "Most cost-effective" | Cheapest option that works, check S3 classes, Spot, RIs |
| "Least privilege" | IAM with minimum permissions, never use * wildcard |
| "Cannot afford data loss" | Multi-AZ, sync replication, RDS Multi-AZ not read replica |
| "Sub-millisecond latency" | DAX (DynamoDB), ElastiCache Redis/Memcached, not RDS |
| "Video/audio streaming" | Kinesis Video Streams or CloudFront, not Data Streams |
| "Ordered processing" | SQS FIFO, Kinesis Data Streams (not SQS Standard) |
| "Exactly-once processing" | SQS FIFO with deduplication, not Standard |
| "SQL queries on S3" | Athena (not EMR unless specified) |
| "Real-time analytics" | Managed Service for Apache Flink (ex-Kinesis Data Analytics), not Firehose (near real-time) |
| "Warm standby" | Scaled-down full environment, not backup only |
| "RPO near zero" | Continuous replication, Multi-AZ, Aurora Global |
| "Static IP address" | Elastic IP, NLB (not ALB), Global Accelerator |
| "Web Application Firewall" | AWS WAF, not just Security Groups |
| "DDoS protection" | AWS Shield (Standard free, Advanced paid) |
| "Hybrid file access" | Storage Gateway, not just Direct Connect |
| "IoT device management" | AWS IoT services are out of scope for SAA-C03; expect them only as distractors |
| "Workflow coordination" | Step Functions, not multiple Lambdas manually |
| "API throttling" | API Gateway rate limiting, not just ALB |
| "Temporary access" | IAM roles + STS, not IAM users |

### Complex Scenario Solutions

**Scenario 1: Global Application with Low Latency**
```
Requirements: Users worldwide, <100ms latency, HA
Solution: CloudFront + Route 53 latency routing + 
         Multi-region deployment + Aurora Global Database
Why NOT: Single region (too slow for global users)
```

**Scenario 2: Hybrid Cloud with Centralized Logging**
```
Requirements: On-premises + AWS, centralized logs, search
Solution: CloudWatch Logs agent (on-prem) → CloudWatch Logs → 
         Subscription filter → Kinesis Firehose → OpenSearch
Why NOT: Just S3 (can't search efficiently)
```

**Scenario 3: Large File Processing Pipeline**
```
Requirements: 10GB files, parallel processing, fault-tolerant
Solution: S3 event → SQS → Auto Scaling EC2/Lambda (with layers) → 
         Process in parallel → Output to S3
Why NOT: Single Lambda (15-min + 10GB limit exceeded)
```

**Scenario 4: Database Migration with Minimal Downtime**
```
Requirements: Oracle to PostgreSQL, <1 hour downtime
Solution: AWS SCT (schema conversion) → DMS (full load + CDC) → 
         Test on target → Quick cutover
Why NOT: Backup/restore (too much downtime, no CDC)
```

**Scenario 5: Secure API with Rate Limiting**
```
Requirements: Public API, authenticated, 1000 req/sec per user
Solution: API Gateway + Cognito User Pools + 
         Usage plans with API keys + Per-client throttling
Why NOT: Lambda + ALB (no built-in rate limiting per user)
```

**Scenario 6: Cost Optimization for Dev/Test**
```
Requirements: Dev/test environment, only used 9-5 weekdays
Solution: EventBridge scheduled rules → Lambda → 
         Start/Stop EC2, RDS (Instance Scheduler)
Why NOT: 24/7 operation (wastes 2/3 of costs)
```

**Scenario 7: Compliance Data Retention**
```
Requirements: 7 years retention, immutable, regulatory
Solution: S3 Glacier Deep Archive + S3 Object Lock Compliance Mode + 
         S3 Inventory + AWS Backup (for other resources)
Why NOT: Governance mode (can be overridden), Standard S3 (too expensive)
```

**Scenario 8: Multi-Tier Application HA**
```
Requirements: Web tier, app tier, DB tier, 99.99% availability
Solution: ALB + Multi-AZ Auto Scaling (app) + 
         RDS Multi-AZ (DB) + ElastiCache Redis Multi-AZ + 
         Route 53 health checks
Why NOT: Single AZ (no HA), read replicas instead of Multi-AZ
```

**Scenario 9: S3 Performance at Scale**
```
Requirements: 10,000 PUT/sec, high throughput
Solution: Distribute across multiple prefixes (3,500 PUT/s per prefix) + 
         Use random prefix naming + Multipart upload for large files
Why NOT: Single prefix (bottleneck), sequential names (hot partition)
```

**Scenario 10: Serverless Event Processing**
```
Requirements: S3 upload triggers processing, handle errors
Solution: S3 event → Lambda → Process → DLQ (for failures) → 
         CloudWatch alarms for DLQ depth
Why NOT: Direct processing without error handling (data loss on failure)
```

---

## QUESTION TYPE IDENTIFIERS

### Spot the Distractor Answers

**Pattern 1: Technically Works But Not Optimal**
- Question: "Most cost-effective database solution..."
- Distractor: Aurora (works but expensive)
- Correct: RDS MySQL with Reserved Instances

**Pattern 2: Missing Required Configuration**
- Question: "Enable DNS resolution for VPC peering..."
- Distractor: "Create peering connection" (incomplete)
- Correct: "Create peering + enable DNS settings in BOTH VPCs"

**Pattern 3: Service Confusion**
- Question: "Stream video from IoT devices..."
- Distractor: Kinesis Data Streams
- Correct: Kinesis Video Streams

**Pattern 4: Wrong Tool for Job**
- Question: "Run containers without managing servers..."
- Distractor: ECS with EC2 launch type
- Correct: ECS with Fargate or Lambda

**Pattern 5: Cost vs Performance Trade-off**
- Question: "Balance cost and performance for caching..."
- Distractor: ElastiCache with largest instance
- Correct: Start small, monitor, scale as needed

### Multi-Step Solutions

**If question requires MULTIPLE steps:**

Example: "Company needs to..."
1. Identify ALL requirements (cost, performance, security, HA)
2. Eliminate answers that miss ANY requirement
3. Choose answer addressing ALL requirements
4. Verify no simpler solution exists

**Red Flags in Answers:**
- "Manually" anything (automation preferred)
- "Self-managed" vs managed service (prefer managed)
- "Complicated" multi-step vs simple solution
- Missing error handling or monitoring
- No encryption when data sensitivity mentioned
- No HA when availability mentioned

---

## ADVANCED SERVICE COMBINATIONS

### Common Service Pairings

| Primary Service | Common Pair | Why Together |
|----------------|-------------|--------------|
| Lambda | API Gateway | Serverless HTTP APIs |
| Lambda | DynamoDB | Serverless data storage |
| Lambda | SQS | Async processing, decoupling |
| Lambda | EventBridge | Event-driven automation |
| ECS | ALB | Container load balancing |
| ECS | Service Discovery | Microservices communication |
| RDS | ElastiCache | Database query caching |
| RDS | Read Replicas | Read scaling |
| S3 | CloudFront | Content delivery |
| S3 | Athena | SQL queries on data lake |
| S3 | Glue | ETL processing |
| Kinesis Data Streams | Lambda | Stream processing |
| Kinesis Firehose | S3/Redshift | Data ingestion |
| API Gateway | Cognito | API authentication |
| ALB | WAF | Web application security |
| Route 53 | CloudFront | Global DNS + CDN |
| Direct Connect | VPN | Hybrid connectivity + backup |
| CloudWatch | SNS | Monitoring + alerting |
| CloudTrail | S3 + Athena | Audit log analysis |

### Anti-Patterns (What NOT to Do)

 **Using RDS for caching** → Use ElastiCache instead  
 **Using S3 for frequent random I/O** → Use EBS or EFS  
 **Using Lambda for long-running tasks** → Use ECS, Batch, or EC2  
 **Using EC2 for simple cron jobs** → Use EventBridge + Lambda  
 **Using EBS for shared file storage** → Use EFS instead  
 **Using NAT Gateway for VPC endpoint traffic** → Use VPC endpoints (cheaper)  
 **Using public S3 buckets** → Use pre-signed URLs or CloudFront OAC  
 **Using IAM users for applications** → Use IAM roles  
 **Using hardcoded credentials** → Use Secrets Manager or Parameter Store  
 **Using single AZ for production** → Always Multi-AZ for HA  
 **Using SQS Standard for strict ordering** → Use SQS FIFO  
 **Using default VPC for production** → Create custom VPC  
 **Using root account for operations** → Use IAM users/roles  
 **Using unencrypted data at rest** → Enable encryption  
 **Using public subnets for databases** → Always private subnets  

---

## PERFORMANCE OPTIMIZATION PATTERNS

### Database Performance Hierarchy

**1. Caching Layer** (Fastest, lowest cost impact)
- ElastiCache (Redis/Memcached) for session/query cache
- DAX for DynamoDB (microsecond latency)
- CloudFront for static content

**2. Read Scaling** (Moderate cost, high benefit)
- RDS Read Replicas (up to 15)
- DynamoDB On-Demand or higher provisioned capacity
- Aurora Read Replicas (up to 15, better performance than RDS)

**3. Vertical Scaling** (Higher cost, immediate benefit)
- Larger instance types (more CPU/RAM)
- Provisioned IOPS storage (io2, io2 Block Express)
- Enhanced networking (ENA)

**4. Horizontal Scaling** (Complex, highest scalability)
- Sharding/partitioning
- DynamoDB partition key design
- Multiple Aurora clusters (writes)

### Storage Performance Ladder

**Highest Performance → Lowest Cost:**
1. Instance Store (ephemeral, lowest latency)
2. EBS io2 Block Express (256,000 IOPS)
3. EBS io2 (256,000 IOPS)
4. EBS gp3 (80,000 IOPS, good default)
5. EBS gp2 (3 IOPS/GB, legacy)
6. EBS st1 (throughput-optimized HDD)
7. EBS sc1 (cold HDD, lowest cost)

**For Shared Storage:**
- FSx for Lustre (100+ GB/s, HPC)
- EFS (General Purpose or Max I/O)
- FSx for Windows (SMB, Active Directory)

### Network Performance Optimization

**1. Placement Groups**
- Cluster: 10 Gbps between instances (HPC)
- Spread: Isolated hardware (critical apps)
- Partition: Group isolation (big data)

**2. Enhanced Networking**
- ENA (Elastic Network Adapter): 100 Gbps
- EFA (Elastic Fabric Adapter): HPC, MPI, low latency

**3. Endpoint Optimization**
- VPC Endpoints: Bypass NAT Gateway
- PrivateLink: Private service access
- Direct Connect: Consistent low latency

**4. CDN & Caching**
- CloudFront: Global edge caching
- S3 Transfer Acceleration: Faster uploads
- Route 53: Latency-based routing

---

## SECURITY IN DEPTH PATTERNS

### Defense in Depth Layers

**1. Network Security**
```
Internet → CloudFront/Shield → WAF → ALB → 
Private Subnet → Security Groups → 
NACLs → VPC Flow Logs (monitoring)
```

**2. Data Security**
```
Client → TLS/SSL (in transit) → 
AWS Service → KMS (at rest) → 
Encrypted Storage → Access Logs → CloudTrail
```

**3. Identity & Access**
```
User → MFA → IAM/Cognito → 
Temporary Credentials (STS) → 
Resource-based Policies → 
Permission Boundaries → SCPs (Organizations)
```

**4. Application Security**
```
Input Validation → WAF Rules → 
API Gateway (throttling) → 
Lambda (isolated execution) → 
Secrets Manager (credentials) → 
CloudWatch (monitoring)
```

### Security Service Selection

| Threat | AWS Service | Use When |
|--------|------------|----------|
| DDoS | Shield Standard (free) | Basic protection |
| DDoS | Shield Advanced ($3000/mo) | Critical apps, 24/7 response |
| SQL Injection | WAF | Web applications |
| Unauthorized Access | IAM + MFA | All resources |
| Data Breach | KMS + Encryption | Sensitive data |
| Malware | GuardDuty | Threat detection |
| Vulnerability | Inspector | EC2/container scanning |
| PII Discovery | Macie | S3 data classification |
| Compliance | Config + Security Hub | Continuous compliance |
| Audit Trail | CloudTrail | All API calls |
| Network Intrusion | VPC Flow Logs + GuardDuty | Network monitoring |

---

## EXAM DAY FINAL STRATEGIES

### The 30-Second Question Analysis Method

**Step 1: Identify the Constraint (5 seconds)**
- Cost? → Cheapest option that works
- Performance? → Fastest/lowest latency
- Security? → Most secure, least privilege
- Operational? → Least management, most automated
- Multiple? → Prioritize: Security > HA > Cost > Performance

**Step 2: Identify Key Phrases (5 seconds)**
- "Most cost-effective" = cheapest
- "Minimize operational overhead" = managed service/serverless
- "Cannot afford data loss" = Multi-AZ, sync replication
- "Real-time" = Kinesis Data Streams, not Firehose
- "Near real-time" = Kinesis Firehose acceptable
- "Sub-millisecond" = ElastiCache or DAX

**Step 3: Eliminate Obviously Wrong (10 seconds)**
- Missing encryption when data sensitivity mentioned
- Single AZ when HA required
- Manual process when automation possible
- Self-managed when managed service available
- Expensive when cheaper option works

**Step 4: Choose Best Remaining (10 seconds)**
- Simplest solution that meets ALL requirements
- Most aligned with AWS best practices
- Scalable and maintainable

### Answer Selection Priorities

**When Multiple Answers Seem Correct:**

1. **Security over everything else** - If question mentions sensitive data, regulated industry
2. **Managed over self-managed** - Unless cost explicitly prioritized over operations
3. **Multi-AZ over single AZ** - Unless cost explicitly prioritized over availability
4. **Automation over manual** - Always prefer automated solutions
5. **Simpler over complex** - If two solutions work, choose simpler

**Red Flag Answers (Usually Wrong):**
- Answers with "manually scale" or "administrator monitors"
- Self-managed solutions when managed alternative exists
- Complex multi-service chains when simple solution works
- No error handling or logging mentioned
- Missing encryption for sensitive data
- Missing backup strategy for critical data
- Single point of failure without justification

### Most Commonly Missed Question Types

**Type 1: The Minimum Days Trap**
- Question: "Transition from S3 Standard to Glacier..."
- Wrong: "Immediately"
- Right: "30 days minimum before first transition"

**Type 2: The Service Limit Trap**
- Question: "Lambda function needs to run for 20 minutes..."
- Wrong: "Increase Lambda timeout"
- Right: "Use Step Functions or ECS/Batch" (Lambda max 15 min)

**Type 3: The Encryption Key Trap**
- Question: "Use SSE-C encryption..."
- Wrong: "AWS manages keys"
- Right: "Customer provides key with EVERY request"

**Type 4: The Region Trap**
- Question: "CloudFront distribution certificate..."
- Wrong: "Same region as origin"
- Right: "us-east-1 ONLY"

**Type 5: The Standby Access Trap**
- Question: "RDS Multi-AZ for read scaling..."
- Wrong: "Standby can handle reads"
- Right: "Use Read Replicas; standby NOT accessible"

**Type 6: The Transitivity Trap**
- Question: "VPC A peers with B, B peers with C..."
- Wrong: "A can access C"
- Right: "Peering NOT transitive; must create A-C"

**Type 7: The Protocol Trap**
- Question: "UDP traffic load balancing..."
- Wrong: "Application Load Balancer"
- Right: "Network Load Balancer" (ALB = HTTP/HTTPS only)

**Type 8: The Consistency Trap**
- Question: "DynamoDB immediate consistency..."
- Wrong: "Default behavior"
- Right: "Eventually consistent default; must request strongly consistent"

**Type 9: The Versioning Trap**
- Question: "Disable S3 versioning..."
- Wrong: "Disable option in console"
- Right: "Once enabled, can only SUSPEND"

**Type 10: The Authentication Trap**
- Question: "EC2 instance needs S3 access..."
- Wrong: "Store IAM user credentials on instance"
- Right: "Attach IAM role to instance"

---

## ULTRA-CRITICAL "GOTCHA" LIST

### Top 20 Most Missed Exam Facts

1. **CloudFront ACM certificate MUST be in us-east-1** (not any region)
2. **VPC peering is NOT transitive** (A-B + B-C ≠ A-C)
3. **Gateway Endpoint only for S3 and DynamoDB** (everything else = Interface)
4. **RDS Multi-AZ standby is NOT readable** (use Read Replicas for reads)
5. **S3 versioning cannot be fully disabled** (only suspended once enabled)
6. **Lambda maximum execution time is 15 minutes** (not unlimited)
7. **Spot instances get only 2 minutes warning** (not hours)
8. **ECS dynamic port mapping needs ALB or NLB** (not CLB)
9. **DynamoDB LSI can only be created at table creation** (GSI can be added later)
10. **Data Firehose is near real-time** (buffer can be 0 s; still not true real-time)
11. **Memory is NOT a default CloudWatch metric** (need CloudWatch agent)
12. **S3 Standard-IA has 30-day minimum storage duration** (charged for 30 days even if deleted)
13. **Instance store data is lost on stop/terminate** (only EBS persists)
14. **SSE-C requires customer to provide key with EVERY request** (AWS doesn't store it)
15. **IAM explicit deny ALWAYS wins** (over any allow)
16. **SQS FIFO default is 300 msg/s** (3,000 batched; high-throughput mode goes well beyond, Region-dependent)
17. **NAT Gateway/Instance required for private subnet internet** (can't use IGW directly)
18. **Cross-zone load balancing is charged for NLB** (free for ALB)
19. **Glacier objects must be restored before access** (can't directly retrieve)
20. **VPG does NOT support ECMP** (only Transit Gateway supports ECMP)

### Service Confusion Clarification

**These Services Sound Similar But Are Different:**

| Often Confused | Actual Purpose |
|----------------|----------------|
| **CloudWatch vs CloudTrail** | Metrics/Logs vs API audit trail |
| **Security Groups vs NACLs** | Stateful vs stateless |
| **IAM Roles vs Resource Policies** | Identity-based vs resource-based |
| **Kinesis Data Streams vs Firehose** | Real-time processing vs data loading |
| **ECS vs EKS** | AWS container orchestration vs Kubernetes |
| **Fargate vs Lambda** | Containers vs functions |
| **Aurora vs RDS** | AWS-optimized MySQL/PostgreSQL vs standard |
| **ElastiCache vs DAX** | General caching vs DynamoDB-specific |
| **Storage Gateway File vs Volume** | File objects (S3) vs block storage (EBS) |
| **DataSync vs DMS** | File transfer vs database migration |
| **Snowball vs Direct Connect** | Physical data transfer vs dedicated network |
| **WAF vs Shield** | Application protection vs DDoS protection |
| **GuardDuty vs Inspector** | Threat detection vs vulnerability scanning |
| **Config vs CloudTrail** | Resource compliance vs API audit |
| **Systems Manager vs OpsWorks (retired)** | AWS tool vs Chef/Puppet automation (OpsWorks EOL; use Systems Manager) |

### Numerical Values to Memorize

**S3:**
- Standard-IA: 30 days minimum, $0.01/GB retrieval
- Glacier Flexible: 90 days minimum, 3-5 hours standard retrieval
- Glacier Deep Archive: 180 days minimum, 12 hours retrieval
- Multipart: >100MB recommended, >5GB required
- Max object size: 50 TB
- Max PUT: 5GB (use multipart for larger)

**Lambda:**
- Max execution: 15 minutes (900 seconds)
- Max memory: 10,240 MB (10 GB)
- Max deployment package: 50 MB zipped, 250 MB unzipped
- Max /tmp: 10 GB
- Max concurrency: 1,000 per region (default)
- Max layers: 5 per function

**RDS:**
- Read replicas: Max 15
- Automated backup retention: 1-35 days
- Multi-AZ failover: 1-2 minutes
- Max storage: 64 TB (most engines)

**DynamoDB:**
- LSI: Max 5, only at table creation
- GSI: Max 20, can add anytime
- Item size: Max 400 KB
- Query: Returns max 1 MB per call
- Scan: Returns max 1 MB per call

**VPC:**
- Subnets per VPC: 200
- Route tables per VPC: 200
- Security groups per VPC: 2,500
- Rules per security group: 60 inbound, 60 outbound
- NACLs per VPC: 200
- VPC peering connections: 50 per VPC default (max 125)

**EC2:**
- On-Demand vCPUs: 5-1,152 per region (varies by instance type)
- EBS volumes per instance: Depends on instance type
- Placement group instances: No limit (cluster limited to single AZ)

**Kinesis:**
- Data Streams shard capacity: 1 MB/s or 1,000 records/s write, 2 MB/s read
- Data Streams retention: 1-365 days
- Firehose buffer: can be 0 s (zero buffering, 2023)
- Video Streams: Unlimited concurrent streams

---

## FINAL PRE-EXAM CHECKLIST

### 30 Minutes Before Exam

**Quick Review (10 min):**
1. CloudFront certificate = us-east-1 ONLY
2. Gateway endpoint = S3 + DynamoDB ONLY
3. Multi-AZ standby = NOT readable
4. VPC peering = NOT transitive
5. Memory metric = Need CloudWatch agent
6. S3 versioning = Cannot fully disable
7. Lambda max = 15 minutes
8. DynamoDB LSI = Table creation only
9. Glacier = Must restore first
10. SSE-C = Customer provides key every request

**Confidence Builders (10 min):**
- Review your strongest domain (quick confidence boost)
- Scan through visual memory cards
- Deep breath exercises

**Mental Preparation (10 min):**
- Positive self-talk: "I am prepared"
- Visualize success
- Stay hydrated
- Empty bladder (130-minute exam!)

### During Exam Strategy

**Time Management:**
- 65 questions in 130 minutes = 2 minutes per question
- Flag uncertain questions (review later)
- Don't spend >3 minutes on any single question first pass
- Reserve 20 minutes at end for flagged questions

**When Stuck:**
1. Re-read question carefully (look for keywords)
2. Eliminate obviously wrong answers
3. If still stuck, make educated guess and flag
4. Move on (don't dwell)

**Red Flags You Misread:**
- Your answer feels "too easy"
- Question seems to have two correct answers
- All answers seem wrong

**When This Happens:**
- Re-read question stem carefully
- Look for negative words (NOT, EXCEPT, LEAST)
- Check if question asks for multiple answers

### Post-Exam (If You Fail)

**Immediate Actions:**
1. Note topics you struggled with
2. Don't despair (many pass on second attempt)
3. Review score report by domain

**Study Plan:**
1. Focus on failed domains (spend 80% of time)
2. Retake practice tests for those domains
3. Hands-on labs for weak areas
4. Schedule retake in 2-4 weeks

---

## SUCCESS AFFIRMATIONS

**You are ready when:**
- Can explain differences between similar services
- Know when to use each service
- Understand the "why" not just "what"
- Can identify trade-offs (cost vs performance vs security)
- Scoring consistently 80%+ on practice tests
- Weak domains now at least 70%+
- Can answer questions in <2 minutes
- Sleep well, eat well, stress managed

**Remember:**
- This exam tests practical knowledge, not memorization
- The "most correct" answer meets ALL requirements
- Simpler is usually better
- Managed services preferred over self-managed
- Security is never optional
- You've prepared thoroughly - trust your preparation.

---

## COMMON TRAPS TO AVOID

### Compute Cost Optimization

| Workload Type | Best Option | Savings |
|--------------|-------------|---------|
| Steady-state 24/7 | Reserved Instances | 72% |
| Flexible family | Compute Savings Plans | 66% |
| Variable, burstable | T3/T4 instances | 40% vs M5 |
| Fault-tolerant | Spot Instances | 90% |
| Batch/flexible | Spot + On-Demand mix | 70% |
| Dev/test | Instance Scheduler | 65% |
| Serverless-capable | Lambda | Pay per use |
| Container-based | Fargate Spot | 70% |

### Storage Cost Optimization

| Access Pattern | Best S3 Class | Cost/GB |
|---------------|---------------|---------|
| Frequent (>1x/month) | S3 Standard | $0.023 |
| Infrequent (<1x/month) | S3 Standard-IA | $0.0125 |
| Unknown pattern | S3 Intelligent-Tiering | Auto |
| Single AZ acceptable | S3 One Zone-IA | $0.01 |
| Archive (min access) | S3 Glacier Flexible | $0.004 |
| Long-term archive | S3 Glacier Deep Archive | $0.00099 |

**Database Cost Optimization:**
- RDS Reserved Instances: 69% savings
- Aurora Serverless: Pay per ACU-hour (intermittent)
- DynamoDB On-Demand: Unpredictable traffic
- DynamoDB Reserved: 75% savings (predictable)

---

## COMMON TRAPS TO AVOID

 **Memory is default metric** → Need CloudWatch agent  
 **CloudFront cert in any region** → Must be us-east-1  
 **Bucket default affects existing** → Only new objects  
 **Can transition from Glacier** → Must restore first  
 **VPC peering auto DNS** → Must enable both sides  
 **VPC peering is transitive** → NOT transitive (use TGW)  
 **Read replica for HA** → Multi-AZ for HA  
 **Multi-AZ standby readable** → NOT readable (only failover)  
 **Instance store persists** → Lost on stop  
 **SSE-C = AWS manages** → You manage keys  
 **IAM allow > deny** → Deny ALWAYS wins  
 **CloudWatch logs auto-expire** → Indefinite default  
 **SCPs affect management account** → They DON'T  
 **File Gateway = blocks** → Files as S3 objects  
 **Volume Gateway = S3 console access** → Blocks only  
 **Tape Gateway for file access** → For backup/archive only  
 **DataSync = database migration** → Files only (use DMS for DBs)  
 **Snowball for <10TB** → Use DataSync or direct upload  
 **SQS FIFO unlimited throughput** → 300 msg/s default (3000 batched), more with high-throughput mode  
 **EventBridge = SNS** → EB for event routing, SNS for pub/sub  
 **Step Functions = Lambda** → Orchestration vs single function  
 **S3 versioning disableable** → Once on, only SUSPEND  
 **RDS encryption after creation** → Must snapshot, copy encrypted, restore  
 **Lambda runs forever** → Max 15 minutes  
 **Spot gives hours warning** → Only 2 minutes  
 **ECS dynamic ports with CLB** → ALB or NLB only  
 **Cross-zone LB always free** → ALB free, NLB charged  
 **DynamoDB LSI add later** → Only at table creation  
 **Kinesis Firehose real-time** → Near real-time (even with 0 s buffer)  
 **Enhanced networking default** → Specific instance types only  

---

## QUICK DECISION TREES

### Need High Availability?
- **Database**: Multi-AZ RDS or Aurora Global
- **Compute**: Multi-AZ + Auto Scaling + ALB
- **Storage**: S3 (11 9's durability) or EFS (Multi-AZ)
- **DNS**: Route 53 with health checks + failover

### Need to Reduce Costs?
- **Compute**: Spot instances, RIs, Savings Plans, right-sizing
- **Storage**: S3 lifecycle policies, Intelligent-Tiering, delete unused
- **Database**: Aurora Serverless, RDS RIs, right-size instances
- **Network**: VPC endpoints (avoid NAT gateway charges)

### Need Better Performance?
- **Database**: ElastiCache (Redis/Memcached), DAX (DynamoDB)
- **Compute**: Larger instance, placement groups, ENA/EFA
- **Storage**: Provisioned IOPS (io2), instance store
- **Content**: CloudFront CDN, S3 Transfer Acceleration

### Need More Security?
- **Network**: Private subnets, NACLs, Security Groups, VPC endpoints
- **Data**: KMS encryption, S3 encryption, RDS encryption
- **Access**: MFA, least privilege IAM, SCPs
- **Monitoring**: CloudTrail, GuardDuty, Config, Security Hub

### Serverless Architecture?
- **Compute**: Lambda
- **API**: API Gateway
- **Database**: DynamoDB
- **Storage**: S3
- **Auth**: Cognito
- **Orchestration**: Step Functions

---

## EXAM KEYWORDS (What They Mean)

- **"Lowest cost"** → Cheapest storage class, Spot, RIs
- **"Highest performance"** → Provisioned IOPS, cluster placement, caching
- **"Most secure"** → Encryption, private subnets, least privilege
- **"Minimum operational overhead"** → Managed services, serverless
- **"Highly available"** → Multi-AZ, multiple regions
- **"Scalable"** → Auto Scaling, serverless, elastic
- **"Real-time"** → Kinesis, DynamoDB Streams, Lambda
- **"Near real-time"** → Firehose, CloudWatch
- **"Decoupled"** → SQS, SNS, EventBridge
- **"Disaster recovery"** → Pilot Light, Warm Standby, Multi-Site
- **"Cannot be overridden"** → SCPs (not IAM policies)
- **"Temporary credentials"** → IAM roles, STS, Cognito Identity Pools

---

## TEST-TAKING STRATEGIES

### Before the Exam
1. Review this card 2-3 times
2. Get good sleep (8 hours)
3. Eat a light meal before exam
4. Arrive 15 minutes early (or log in early for online)

### During the Exam
1. **Read Carefully**: Every word matters
2. **Eliminate Wrong Answers**: Remove obviously incorrect options first
3. **Look for Keywords**: "lowest cost", "highest performance", etc.
4. **Flag & Move On**: If stuck >2 minutes, flag and continue
5. **Watch for Traps**: Services that sound right but aren't optimal
6. **Consider All Requirements**: Cost AND performance AND security

### Common Traps
- Services that work but aren't optimal
- Missing required configurations (e.g., DNS for VPC peering)
- Wrong region requirements (CloudFront cert = us-east-1)
- Assuming default behaviors that don't exist
- Confusing similar services (EBS types, storage classes)

### If Unsure
1. What is the PRIMARY requirement? (cost, performance, security?)
2. What is EXPLICITLY stated vs assumed?
3. Which answer is MOST aligned with AWS best practices?
4. Which is the SIMPLEST solution that meets requirements?

---

## TIME MANAGEMENT (Exam)

- **130 minutes** / 65 questions = **2 min/question**
- Spend <1 min on easy questions (bank extra time)
- Flag and skip if >2 minutes
- Reserve 30 minutes for review at end
- Review flagged questions with fresh eyes

---

## FINAL CHECKLIST (Before Exam)

- [ ] CloudFront certs = us-east-1
- [ ] Memory = CloudWatch agent
- [ ] Multi-AZ = HA, Read Replica = scale
- [ ] IAM deny wins always
- [ ] S3 IA = 30-day minimum
- [ ] Glacier retrieval times memorized
- [ ] Instance types (C/M/R/T) purposes
- [ ] VPC Endpoint: Gateway (S3/DDB), Interface (others)
- [ ] Caching: Redis vs Memcached vs DAX
- [ ] FSx: Lustre (HPC), Windows (SMB)
- [ ] SCPs don't affect management account
- [ ] Storage Gateway: File (S3 objects), Volume (blocks), Tape (archive)
- [ ] DataSync (files), DMS (databases), Snow (physical)
- [ ] SQS FIFO: 300 msg/s, ends in .fifo
- [ ] EventBridge (event routing), SNS (pub/sub), SQS (queue)
- [ ] Step Functions (workflows), Lambda (single function)
- [ ] Aurora Global: <1s lag, <1min failover
- [ ] RDS IAM Auth: 15 min token
- [ ] ECS dynamic ports: ALB or NLB (not CLB)
- [ ] Auto Scaling cooldown: 5 minutes

---

## STAY CALM & CONFIDENT

 You've studied hard
 You know the material
 Read questions carefully
 Eliminate wrong answers first


---

*Ultra Quick Reference Card v1.0*  
*AWS Certified Solutions Architect Associate (SAA-C03)*  
*Print or save for last-minute review*

