# 04: Storage Services - Ultra Fast Learning

## S3 Storage Classes
| Class | Use Case | Retrieval | Min Storage | Availability |
|-------|----------|-----------|-------------|--------------|
| Standard | Frequent access | Instant | None | 99.99% |
| Intelligent-Tiering | Unknown pattern | Instant | None | 99.9% |
| Standard-IA | Infrequent | Instant | 30 days | 99.9% |
| One Zone-IA | Non-critical | Instant | 30 days | 99.5% |
| Glacier Instant | Archive + instant | Instant | 90 days | 99.9% |
| Glacier Flexible | Archive | 1-5 min to 12 hr | 90 days | 99.99% |
| Glacier Deep Archive | Long-term | 12-48 hours | 180 days | 99.99% |

**Mnemonic: S-I-S-O-G³** (Standard, Intelligent, Standard-IA, One Zone, 3 Glaciers)

## S3 Key Features

### Versioning
- Keep multiple versions of objects
- Protects from accidental deletes
- Once enabled, can only **suspend** (not disable)
- Delete marker on delete (can restore)

### Encryption
- **SSE-S3**: AWS managed keys (AES-256), default for every bucket since Jan 2023
- **SSE-KMS**: AWS KMS managed keys (audit trail)
- **SSE-C**: Customer provided keys (disabled by default on new buckets since April 2026)
- **Client-Side**: Encrypt before upload

### Replication
- **CRR**: Cross-Region (compliance, latency)
- **SRR**: Same-Region (log aggregation, test/prod sync)
- Requires versioning enabled
- Only new objects replicated (existing objects need batch job)

### Lifecycle Policies
- Transition actions (move to cheaper class)
- Expiration actions (delete after X days)
- Apply to prefixes or tags

### S3 Performance
- **3,500 PUT/COPY/POST/DELETE** per second per prefix
- **5,500 GET/HEAD** per second per prefix
- **Multipart upload**: Required >5 GB, recommended >100 MB (max 10,000 parts, 50 TB object)
- **S3 Transfer Acceleration**: CloudFront edge locations for upload
- **Byte-Range Fetches**: Parallel downloads

## EBS (Elastic Block Store)

### EBS Volume Types
| Type | IOPS | Throughput | Use Case |
|------|------|------------|----------|
| gp3 | 80K | 2,000 MiB/s | General, cost-effective |
| gp2 | 16K | 250 MiB/s | General, burst |
| io2/io1 | 256K/64K | 4,000/1,000 MiB/s | High performance DB |
| st1 | 500 | 500 MB/s | Big data, logs |
| sc1 | 250 | 250 MB/s | Cold storage |

**SSD (gp, io)**: Small random I/O, databases  
**HDD (st, sc)**: Large sequential I/O, big data

### EBS Features
- **AZ-locked**: Must be in same AZ as EC2
- **Snapshots**: Stored in S3, incremental, cross-region copy
- **Encryption**: Uses KMS, transparent, snapshot encrypted too
- **Multi-Attach**: io1/io2 only, max 16 instances (cluster)

## EFS (Elastic File System)
- **Network file system** (NFS v4.1)
- **Multi-AZ**, can mount to multiple EC2
- **Linux only** (not Windows)
- **Higher price per GB** than EBS, but you pay only for data stored
- **Auto-scaling**, pay per use
- **Performance modes**: General Purpose (default, recommended), Max I/O (previous generation)
- **Throughput modes**: Elastic (default, recommended), Provisioned, Bursting
- **Storage classes**: Standard, IA, Archive (lifecycle policy)

## Storage Gateway
- **Hybrid cloud** storage
- **Types**:
  - **File Gateway**: S3 via NFS/SMB
  - **Volume Gateway**: iSCSI, cached or stored
  - **Tape Gateway**: Virtual tapes to S3/Glacier

## Snow Family (closed to new customers)
- **Snowcone** (retired): 8 TB, edge computing
- **Snowball Edge**: 210 TB (Storage Optimized) or 28 TB NVMe + 104 vCPUs (Compute Optimized)
- **Snowmobile** (retired): 100 PB, truck
- **Use case**: TB/PB data transfer, limited bandwidth

## FSx
- **FSx for Windows**: Windows file server, SMB, AD integration
- **FSx for Lustre**: High-performance computing, ML, 100+ GB/s
- **FSx for NetApp ONTAP**: NFS, SMB, iSCSI
- **FSx for OpenZFS**: NFS, over 1M IOPS from cache (up to 350,000 IOPS from disk)

## Quick Exam Tips
- **S3**: Object storage, unlimited, 50 TB max object (5 GB max single PUT)
- **S3 Standard**: 99.99% availability, 11 nines durability
- **Glacier**: Minutes to hours retrieval
- **EBS**: Block storage, AZ-locked, persistent
- **Instance Store**: Ephemeral, lost on stop, hibernate or terminate
- **EFS**: Multi-AZ file system, Linux only
- **Lifecycle**: Automate transitions between storage classes
- **Versioning**: Protects from deletes, cannot disable once enabled
- **MFA Delete**: Extra protection for versioned buckets
- **S3 encryption in transit**: HTTPS (SSL/TLS)
- **Presigned URL**: Temporary access (CLI default 3600 sec; up to 7 days with IAM user credentials, 12 hours from the console)

