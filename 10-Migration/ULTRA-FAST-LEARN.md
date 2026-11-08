# 10: Migration & Transfer - Ultra Fast Learning

## 7 Rs Migration Strategies

1. **Rehost (Lift-and-Shift)**
   - Move as-is to AWS (VMs → EC2)
   - **Fastest**, least changes
   - Use: AWS Application Migration Service (MGN)

2. **Replatform (Lift-Tinker-Shift)**
   - Minor optimizations, no code changes
   - Example: Self-managed DB → RDS

3. **Repurchase (Drop-and-Shop)**
   - Switch to SaaS
   - Example: Exchange → Office 365

4. **Refactor/Re-architect**
   - Redesign for cloud-native
   - Example: Monolith → Microservices/Lambda
   - **Most expensive**, most benefits

5. **Retire**
   - Turn off unused applications
   - Reduce cost and complexity

6. **Retain (Revisit)**
   - Keep on-premises (for now)
   - Migrate later

7. **Relocate**
   - Move VMware workloads at the hypervisor level, no application changes
   - Example: vSphere VMs → VMware Cloud on AWS

**Exam Tip**: Match scenario to strategy.

## AWS DataSync
- **Automated data transfer** (on-premises ↔ AWS)
- **Bandwidth optimization**, compression, encryption
- **Destinations**: S3, EFS, FSx
- **Schedule**: Hourly, daily, weekly
- **Agent**: Install on-premises
- **Speed**: 10x faster than open-source tools

## AWS Transfer Family
- **Managed SFTP/FTPS/FTP/AS2** service (plus browser-based web apps)
- **Store in**: S3, EFS
- **Use case**: Migrate file transfer workflows
- **Integration**: Existing authentication (AD, LDAP)

## Database Migration Service (DMS)

### DMS Basics
- Migrate databases to AWS
- **Source DB stays operational** during migration
- **Homogeneous**: Oracle → Oracle
- **Heterogeneous**: Oracle → Aurora (need SCT)

### Migration Types
- **Full load**: One-time migration
- **Full load + CDC**: Initial + ongoing changes
- **CDC only**: Only ongoing changes

### DMS Components
- **Replication instance**: EC2 running DMS
- **Source endpoint**: Source database
- **Target endpoint**: Target database
- **Replication task**: Migration job

### Schema Conversion Tool (SCT)
- Convert schema for heterogeneous migrations (DMS Schema Conversion is the managed alternative)
- **Not needed** for same engine (homogeneous)
- Example: SQL Server → PostgreSQL

## Snow Family

### Snowcone
- **8 TB** usable storage
- **Small**, rugged, portable
- **DataSync agent** pre-installed
- **Use case**: Edge computing, small data transfer
- **Status**: discontinued 12 Nov 2024

### Snowball Edge
- **Storage Optimized**: 210 TB, 104 vCPUs
- **Compute Optimized**: 28 TB NVMe, 104 vCPUs
- **Use case**: Local processing + data transfer
- **Cluster**: 3-16 devices
- **Status**: closed to new customers since 7 Nov 2025; support ends 31 Dec 2026

### Snowmobile
- **100 PB** per truck
- **Physical truck** to your datacenter
- **Use case**: Datacenter migration, 10+ PB data
- **Status**: no longer offered (end of support 14 Mar 2024)

### When to Use Snow?
- **>10 TB**: Consider Snow devices
- **Network**: Limited bandwidth, expensive data transfer
- **Time**: `(Data Size / Network Speed) > Ship Time`

## Migration Hub
- **Track migrations** from single location
- **Integrates with**: MGN, DMS (Server Migration Service is discontinued)
- **Not a migration tool** (just tracking/planning)
- **Status**: closed to new customers since 7 Nov 2025 (AWS Transform offers similar tracking)

## Application Discovery Service
- **Discover on-premises** servers
- **Agentless**: VMware vCenter
- **Agent-based**: Detailed info (processes, connections)
- **Integration**: Migration Hub
- **Status**: closed to new customers since 7 Nov 2025

## Server Migration Service (SMS)
- **Discontinued** (use Application Migration Service instead)
- Automate, schedule, track VM migrations

## Application Migration Service (MGN)
- **Replaces SMS** (now listed as AWS Transform MGN)
- **Lift-and-shift** (rehost)
- **Continuous replication**
- **Minimal downtime**, cutover window
- **Supports**: Physical, virtual, cloud servers

## AWS Backup
- **Centralized backup** across AWS services
- **Supported**: EC2, EBS, RDS, Aurora, DynamoDB, EFS, FSx, Storage Gateway
- **Backup plans**: Schedules, retention, lifecycle
- **Backup vaults**: Organize backups
- **Cross-region/account** backup
- **PITR** (Point-in-Time Recovery)

### Backup vs Snapshots
- **Backup**: Centralized, policy-based, cross-service
- **Snapshots**: Service-specific, manual/automated

## Disaster Recovery Strategies

### DR Strategies (Cost → Recovery Time)
1. **Backup & Restore**: Cheapest, slowest (hours/days)
2. **Pilot Light**: Core services running, scale up when needed (10s of minutes)
3. **Warm Standby**: Scaled-down version running (minutes)
4. **Multi-Site/Hot-Site**: Full production, instant failover (real-time)

### RTO vs RPO
- **RTO (Recovery Time Objective)**: Time to recover
- **RPO (Recovery Point Objective)**: Acceptable data loss

## Quick Exam Tips
- **7 Rs**: Rehost (fastest), Refactor (most benefits)
- **DataSync**: Automated, scheduled, 10x faster
- **DMS**: Keep source operational, use SCT for heterogeneous
- **Snow**: >10 TB data, limited bandwidth (closed to new customers)
- **Snowmobile**: 10+ PB data transfer (no longer offered)
- **MGN**: Replaces SMS, continuous replication
- **Migration Hub**: Centralized tracking (not migration) (closed to new customers)
- **AWS Backup**: Centralized, cross-service backup
- **DR**: Backup & Restore (cheapest) → Multi-Site (fastest)
- **Transfer Family**: SFTP/FTPS/FTP/AS2 to S3/EFS
