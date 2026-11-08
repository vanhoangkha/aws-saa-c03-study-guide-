# Fast Learning - Migration & Transfer

> **Time to Complete**: 40-50 minutes

## Must-Know Concepts (5 Minutes)

### Migration Service Selector (SDASMAD)
```
DATABASE? → DMS (Database Migration Service)
SERVERS? → Application Discovery Service (closed to new customers), MGN
LARGE DATA? → DataSync, Snowball (closed to new customers), Snowmobile (retired)
STORAGE? → Storage Gateway, Transfer Family
APPLICATIONS? → Application Migration Service (MGN)
```

**Memory Aid**: "Snow Delivers, DMS Migrates, DataSync Syncs, Storage Gateway Gates"

## Quick Reference Tables

### Snow Family (Physical Data Transfer)
Status (November 2026): AWS no longer offers Snow Family devices to new customers. Snowcone was discontinued on 12 Nov 2024, Snowmobile is no longer offered, and Snowball Edge has been available only to existing customers since 7 Nov 2025 (support ends 31 Dec 2026). New projects use AWS DataSync, AWS Data Transfer Terminal or Outposts.

| Device | Capacity | Use Case | Transfer Speed |
|--------|----------|----------|----------------|
| **Snowcone** (discontinued) | 8 TB | Edge computing, small transfers | Portable (fits in backpack) |
| **Snowball Edge Storage** | 210 TB | Large migrations, edge storage | Petabyte scale |
| **Snowball Edge Compute** | 28 TB NVMe, 104 vCPUs | ML, processing at edge | Compute + storage |
| **Snowmobile** (retired) | 100 PB | Exabyte-scale migrations | Truck (literal!) |

**Decision**: Internet < 1 week → Direct transfer, Otherwise → Snow device

### Migration Services Matrix
| Service | What It Migrates | Direction | Use Case |
|---------|------------------|-----------|----------|
| **DMS** | Databases | Any ↔ AWS | Homogeneous/heterogeneous DB |
| **DataSync** | Files | On-prem ↔ AWS | NFS/SMB to S3/EFS/FSx |
| **Transfer Family** | Files via SFTP/FTP | Internet → S3/EFS | SFTP uploads to cloud |
| **Storage Gateway** | Hybrid storage | On-prem ↔ S3 | Hybrid cloud storage |
| **MGN** | Servers/VMs | On-prem → EC2 | Lift-and-shift migration |

## Exam Hot Topics

### 1. AWS DMS (Database Migration Service)
```
CAPABILITIES:
├── Homogeneous (Oracle → Oracle)
├── Heterogeneous (Oracle → PostgreSQL)
│   └── Requires SCT (Schema Conversion Tool) or DMS Schema Conversion
├── One-time migration
├── Continuous replication (CDC - Change Data Capture)
└── Migration + ongoing replication

SOURCES (20+):
├── On-premises databases
├── EC2 instances
├── RDS
├── S3
└── Azure SQL, MongoDB, etc.

TARGETS:
├── RDS, Aurora
├── Redshift
├── DynamoDB
├── S3
├── OpenSearch Service
└── Kinesis, DocumentDB

EXAM TIP: Minimal-downtime migration
└── Source DB stays online during migration
```

### 2. Snow Family Deep Dive
```
SNOWCONE (Smallest, discontinued Nov 2024)
├── 8 TB (HDD) or 14 TB (SSD)
├── 4 GB memory, 2 vCPUs
├── USB-C power (very portable)
├── DataSync agent pre-installed
└── Use: IoT, drone data, remote locations

SNOWBALL EDGE (Medium, closed to new customers since 7 Nov 2025)
├── Storage Optimized: 210 TB
├── Compute Optimized: 28 TB NVMe, 104 vCPUs
├── Can cluster 3-16 nodes
├── EC2/Lambda at edge
└── Use: Datacenter migrations, edge processing

SNOWMOBILE (Massive, no longer offered)
├── 100 PB capacity
├── Ruggedized shipping container
├── GPS tracked, video surveillance
├── Dedicated security team
└── Use: Exabyte-scale, datacenter shutdown
```

**Transfer Time Calculation**: 
- 100 TB over 100 Mbps = ~93 days (at full line rate)
- Same with Snowball = ~1 week (including shipping)

### 3. AWS Storage Gateway Types
| Type | Interface | Use Case | Local Cache |
|------|-----------|----------|-------------|
| **File Gateway** | NFS/SMB | File storage in S3 | Yes |
| **Volume Gateway** | iSCSI | Block storage | Yes |
| **Tape Gateway** | iSCSI VTL | Backup (tape replacement) | Yes |

```
FILE GATEWAY
├── Files stored as objects in S3
├── SMB/NFS protocols
├── Local cache for frequent access
├── Lifecycle policies to Glacier
└── Use: File share backup to cloud

VOLUME GATEWAY (2 modes)
├── Cached Volumes: Primary in S3, cache local
└── Stored Volumes: Primary local, backup to S3

TAPE GATEWAY
├── Virtual Tape Library (VTL)
├── Integrates with backup software
├── Tapes archived to Glacier
└── Use: Replace physical tapes
```

### 4. AWS DataSync
```
WHAT: Automated data transfer service
PROTOCOLS: NFS, SMB, HDFS, S3 API (object storage), other clouds
DESTINATIONS: S3, EFS, FSx

FEATURES:
├── Automatic encryption (in-transit)
├── Data validation/integrity checks
├── Bandwidth throttling
├── Schedule transfers
├── A single task can fully use a 10 Gbps link
└── Incremental transfers

AGENT: Required for on-premises storage
USES: One-time migration or scheduled sync

VS STORAGE GATEWAY:
├── DataSync: One-time/scheduled transfers
└── Storage Gateway: Continuous hybrid storage
```

## Common Exam Scenarios

### Scenario 1: Migrate Oracle to PostgreSQL
**Q**: Migrate Oracle database to RDS PostgreSQL with minimal downtime
**ANSWER**: DMS + SCT (Schema Conversion Tool) for heterogeneous migration

### Scenario 2: Transfer 80 TB, Slow Internet
**Q**: Transfer 80 TB data, internet is 100 Mbps (would take months)
**ANSWER**: AWS Snowball Edge (1 week including shipping); new customers can't order Snow devices and use DataSync or AWS Data Transfer Terminal

### Scenario 3: Continuous File Sync to S3
**Q**: On-prem file server needs to continuously sync to S3
**ANSWER**: AWS Storage Gateway (File Gateway mode)

### Scenario 4: SFTP Upload to S3
**Q**: Third parties upload files via SFTP, need to land in S3
**ANSWER**: AWS Transfer Family (SFTP, FTPS, FTP to S3)

### Scenario 5: One-Time NFS Migration
**Q**: Migrate 10 TB NFS share to EFS, one-time
**ANSWER**: AWS DataSync

### Scenario 6: Entire Datacenter Migration
**Q**: Migrate 500 servers from on-prem to AWS
**ANSWER**: AWS Application Migration Service (MGN)

### Scenario 7: Database with Continuous Replication
**Q**: MySQL on-prem, need ongoing replication to RDS
**ANSWER**: DMS with CDC (Change Data Capture)

### Scenario 8: Exabyte-Scale Transfer
**Q**: 10 EB (exabytes) of data to migrate
**ANSWER**: AWS Snowmobile (100 PB each, need ~100); Snowmobile is no longer offered

## Speed Learning Tips

### DMS Replication Instance
```
WHAT: EC2 instance running DMS software
SIZE: Choose based on data volume & complexity
MULTI-AZ: Optional (for HA)

MIGRATION TYPES:
├── Full Load (one-time)
├── Full Load + CDC (ongoing)
└── CDC only (replicate changes)
```

### Schema Conversion Tool (SCT)
```
WHEN NEEDED: Heterogeneous migrations
├── Oracle → PostgreSQL
├── SQL Server → MySQL
├── Oracle → Aurora
└── MySQL → MySQL (not needed)

CAPABILITIES:
├── Converts schema
├── Converts stored procedures
├── Converts views
├── Assessment report (compatibility)
└── Suggests cloud-native alternatives
```

### Transfer Acceleration Decision
```
When to use each:

DIRECT CONNECT:
Yes: Dedicated, consistent bandwidth
Yes: 1, 10, 100 or 400 Gbps dedicated (lower speeds via hosted connections)
Yes: Private connection
No: Weeks to months setup
No: Expensive

SNOWBALL (closed to new customers):
Yes: 10+ TB data
Yes: Poor internet
Yes: One-time migration
No: Shipping time (days)

DATASYNC:
Yes: Scheduled transfers
Yes: NFS/SMB sources
Yes: Automated
No: Bound by available network bandwidth

TRANSFER FAMILY:
Yes: SFTP/FTP protocol needed
Yes: External users uploading
No: Higher cost
```

## Rapid-Fire Facts

### Snow Family Comparison
```
CHOOSE SNOWCONE IF (discontinued):
├── < 8-14 TB
├── Extreme portability needed
├── Edge computing (IoT)
└── Harsh environments

CHOOSE SNOWBALL IF (closed to new customers):
├── 10 TB - 10 PB
├── Need clustering
├── Edge compute (EC2/Lambda)
└── Standard datacenter migration

CHOOSE SNOWMOBILE IF (no longer offered):
├── > 10 PB
├── Entire datacenter
└── Don't mind a truck showing up
```

### Application Migration Service (MGN)
```
FORMERLY: CloudEndure Migration
NOW LISTED AS: AWS Transform MGN

PROCESS:
1. Install agent on source servers
2. Continuous replication begins
3. Test in AWS (non-disruptive)
4. Cutover when ready
5. Source servers shut down

FEATURES:
├── Block-level replication
├── Minimal downtime (minutes)
├── Wide OS support
├── Automated conversion
└── Free for 2,160 hours (90 days) per server, then per hour; AWS resources extra

VS SERVER MIGRATION SERVICE (SMS):
└── MGN is newer, recommended (SMS discontinued)
```

### Transfer Family Features
```
PROTOCOLS:
├── SFTP (SSH File Transfer Protocol)
├── FTPS (FTP over SSL/TLS)
├── FTP (File Transfer Protocol)
├── AS2 (Applicability Statement 2)
└── Browser-based (Transfer Family web apps)

AUTHENTICATION:
├── Service-managed users
├── Custom identity provider (Lambda)
└── Active Directory/LDAP

DESTINATIONS:
├── Amazon S3
└── Amazon EFS

USE CASES:
├── Third-party file uploads
├── Replace on-prem SFTP servers
└── Secure file transfer to cloud
```

## 5-Minute Master Review

### Migration Decision Tree
```
1. What are you migrating?
   DATABASE → DMS (+ SCT if needed)
   FILES → DataSync or Storage Gateway
   SERVERS → Application Migration Service
   LARGE DATA → Snow family
   
2. For databases, same engine?
   YES → DMS only
   NO → DMS + SCT (or DMS Schema Conversion)
   
3. For data transfer, how much?
   < 10 TB + good internet → Direct upload/DataSync
   10 TB - 10 PB + slow internet → Snowball (closed to new customers)
   > 10 PB → Snowmobile (no longer offered)
   
4. Need ongoing sync?
   YES → Storage Gateway or DMS (CDC)
   NO → DataSync or Snow family
```

### Common Migration Patterns
```
1. DATABASE MIGRATION (Zero Downtime)
   On-prem DB → DMS (CDC) → RDS → Cutover
   
2. LIFT-AND-SHIFT (Servers)
   On-prem servers → MGN → EC2
   
3. FILE SHARE TO CLOUD
   On-prem NFS → DataSync → EFS → Cutover
   
4. LARGE DATA TRANSFER
   Datacenter → Snowball → S3 → Process
   
5. HYBRID STORAGE
   On-prem apps ←→ Storage Gateway ←→ S3
```

### DMS Best Practices
 Use Multi-AZ for production
 Enable CloudWatch logging
 Test with validation enabled
 Use CDC for minimal downtime
 Size replication instance appropriately
 Use SCT assessment before migration
 Migrate to Aurora when possible (better performance)

### Common Mistakes to Avoid
 Using internet for massive data transfer (use Snow)
 Not testing DMS migration before cutover
 Forgetting SCT for heterogeneous migrations
 Choosing wrong Snow device for data size
 Not considering bandwidth for transfer time
 Using discontinued SMS (use MGN instead)
 Not enabling validation in DMS
 Underestimating replication instance size

## Exam Practice Speedrun

**Quick Questions** (Answers at bottom)

1. Tool for heterogeneous DB migration? __
2. Snowball Edge storage capacity? __
3. Service for NFS to EFS migration? __
4. Can DMS do ongoing replication? __
5. Snowmobile capacity? __
6. What protocol does Transfer Family support? __
7. Storage Gateway type for file storage? __
8. Is SCT needed for MySQL to MySQL? __

---

### Migration Timelines
```
PLANNING PHASE:
├── Discovery (Application Discovery Service)
├── TCO calculation (AWS Pricing Calculator)
├── Migration strategy (7 Rs)
└── Proof of concept

7 RS OF MIGRATION:
├── Rehost (lift-and-shift) - MGN
├── Relocate (hypervisor-level, e.g. VMware Cloud on AWS)
├── Replatform (lift-tinker-shift) - Some optimization
├── Repurchase (SaaS) - New product
├── Refactor (re-architect) - Cloud-native
├── Retire (turn off) - Decommission
└── Retain (keep on-prem) - Not ready
```

### Application Discovery Service
Status (November 2026): AWS Application Discovery Service has been closed to new customers since 7 Nov 2025.
```
TYPES:
├── Agentless (VMware vCenter)
│   └── VM inventory, config, performance
└── Agent-based (any server)
    └── Detailed dependencies, performance

OUTPUTS:
├── Server inventory
├── Application dependencies
├── Performance data
└── Migration planning data

INTEGRATES WITH:
├── AWS Migration Hub
├── Athena (query data)
└── S3 (export data)
```

## Next Steps
- Time spent: ~40-50 min
- Practice: Understand DMS, Snow device selection
- Ready for: Migration practice questions
- Move to: [Module 11 - Analytics](../11-Analytics/FAST-LEARN.md)

---

**Quick Answers**: 
1) SCT (Schema Conversion Tool) + DMS
2) 210 TB (Storage Optimized)
3) AWS DataSync
4) Yes (CDC - Change Data Capture)
5) 100 PB
6) SFTP, FTPS, FTP, AS2 (plus browser-based web apps)
7) File Gateway
8) No (same engine = homogeneous)

