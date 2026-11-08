# 10: Migration & Transfer - Ultra Fast Learning
- **Transfer Family**: SFTP/FTPS/FTP to S3/EFS
- **DR**: Backup & Restore (cheapest) → Multi-Site (fastest)
- **AWS Backup**: Centralized, cross-service backup
- **Migration Hub**: Centralized tracking (not migration) (closed to new customers)
- **MGN**: Replaces SMS, continuous replication
- **Snowmobile**: 10+ PB data transfer (no longer offered)
- **Snow**: >10 TB data, limited bandwidth (closed to new customers)
- **DMS**: Keep source operational, use SCT for heterogeneous
- **DataSync**: Automated, scheduled, 10x faster
- **7 Rs**: Rehost (fastest), Refactor (most benefits)
## Quick Exam Tips

- **RPO (Recovery Point Objective)**: Acceptable data loss
- **RTO (Recovery Time Objective)**: Time to recover
### RTO vs RPO

4. **Multi-Site/Hot-Site**: Full production, instant failover (real-time)
3. **Warm Standby**: Scaled-down version running (minutes)
2. **Pilot Light**: Core services running, scale up when needed (10s of minutes)
1. **Backup & Restore**: Cheapest, slowest (hours/days)
### DR Strategies (Cost → Recovery Time)

## Disaster Recovery Strategies

- **Snapshots**: Service-specific, manual/automated
- **Backup**: Centralized, policy-based, cross-service
### Backup vs Snapshots

- **PITR** (Point-in-Time Recovery)
- **Cross-region/account** backup
- **Backup vaults**: Organize backups
- **Backup plans**: Schedules, retention, lifecycle
- **Supported**: EC2, EBS, RDS, Aurora, DynamoDB, EFS, FSx, Storage Gateway
- **Centralized backup** across AWS services
## AWS Backup

- **Supports**: Physical, virtual, cloud servers
- **Minimal downtime**, cutover window
- **Continuous replication**
- **Lift-and-shift** (rehost)
- **Replaces SMS** (now listed as AWS Transform MGN)
## Application Migration Service (MGN)

- Automate, schedule, track VM migrations
- **Discontinued** (use Application Migration Service instead)
## Server Migration Service (SMS)

- **Status**: closed to new customers since 7 Nov 2025
- **Integration**: Migration Hub
- **Agent-based**: Detailed info (processes, connections)
- **Agentless**: VMware vCenter
- **Discover on-premises** servers
## Application Discovery Service

- **Status**: closed to new customers since 7 Nov 2025 (AWS Transform offers similar tracking)
- **Not a migration tool** (just tracking/planning)
- **Integrates with**: MGN, DMS (Server Migration Service is discontinued)
- **Track migrations** from single location
## Migration Hub

- **Time**: `(Data Size / Network Speed) > Ship Time`
- **Network**: Limited bandwidth, expensive data transfer
- **>10 TB**: Consider Snow devices
### When to Use Snow?

- **Status**: no longer offered
- **Use case**: Datacenter migration, 10+ PB data
- **Physical truck** to your datacenter
- **100 PB** per truck
### Snowmobile

- **Status**: closed to new customers since 7 Nov 2025; support ends 31 Dec 2026
- **Cluster**: 3-16 devices
- **Use case**: Local processing + data transfer
- **Compute Optimized**: 28 TB NVMe, 104 vCPUs
- **Storage Optimized**: 210 TB, 104 vCPUs
### Snowball Edge

- **Status**: discontinued 12 Nov 2024
- **Use case**: Edge computing, small data transfer
- **DataSync agent** pre-installed
- **Small**, rugged, portable
- **8 TB** usable storage
### Snowcone

## Snow Family

- Example: SQL Server → PostgreSQL
- **Not needed** for same engine (homogeneous)
- Convert schema for heterogeneous migrations
### Schema Conversion Tool (SCT)

- **Replication task**: Migration job
- **Target endpoint**: Target database
- **Source endpoint**: Source database
- **Replication instance**: EC2 running DMS
### DMS Components

- **CDC only**: Only ongoing changes
- **Full load + CDC**: Initial + ongoing changes
- **Full load**: One-time migration
### Migration Types

- **Heterogeneous**: Oracle → Aurora (need SCT)
- **Homogeneous**: Oracle → Oracle
- **Source DB stays operational** during migration
- Migrate databases to AWS
### DMS Basics

## Database Migration Service (DMS)

- **Integration**: Existing authentication (AD, LDAP)
- **Use case**: Migrate file transfer workflows
- **Store in**: S3, EFS
- **Managed SFTP/FTPS/FTP** service
## AWS Transfer Family

- **Speed**: 10x faster than open-source tools
- **Agent**: Install on-premises
- **Schedule**: Hourly, daily, weekly
- **Destinations**: S3, EFS, FSx
- **Bandwidth optimization**, compression, encryption
- **Automated data transfer** (on-premises ↔ AWS)
## AWS DataSync

**Exam Tip**: Match scenario to strategy.

   - Example: vSphere VMs → VMware Cloud on AWS
   - Move VMware workloads at the hypervisor level, no application changes
7. **Relocate**

   - Migrate later
   - Keep on-premises (for now)
6. **Retain (Revisit)**

   - Reduce cost and complexity
   - Turn off unused applications
5. **Retire**

   - **Most expensive**, most benefits
   - Example: Monolith → Microservices/Lambda
   - Redesign for cloud-native
4. **Refactor/Re-architect**

   - Example: Exchange → Office 365
   - Switch to SaaS
3. **Repurchase (Drop-and-Shop)**

   - Example: Self-managed DB → RDS
   - Minor optimizations, no code changes
2. **Replatform (Lift-Tinker-Shift)**

   - Use: AWS Application Migration Service (MGN)
   - **Fastest**, least changes
   - Move as-is to AWS (VMs → EC2)
1. **Rehost (Lift-and-Shift)**

## 7 Rs Migration Strategies


