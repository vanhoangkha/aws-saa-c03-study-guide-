# Module 08: Application Integration

## Overview
Application integration services enable loose coupling and communication between distributed components. This module covers messaging, queuing, and event-driven services.

## Learning Objectives
- Implement message queuing with SQS
- Build pub/sub systems with SNS
- Create event-driven architectures with EventBridge
- Orchestrate workflows with Step Functions
- Understand service integration patterns

---

## 1. Amazon SQS (Simple Queue Service)

### What is SQS?
- Fully managed **message queuing** service
- Decouple and scale microservices
- **Unlimited throughput**, unlimited messages
- **Retention**: 1 minute to 14 days (default 4 days)
- **Low latency** (<10 ms)

### SQS Queue Types

#### Standard Queue
- **Unlimited throughput**
- **At-least-once delivery** (messages may be delivered multiple times)
- **Best-effort ordering** (messages may arrive out of order)
- Use case: High throughput, order not critical

#### FIFO Queue (First-In-First-Out)
- **Limited throughput**: 300 msg/sec (3,000 with batching)
- **Exactly-once processing**
- **Strict ordering** preserved
- **Name must end with .fifo**
- Use case: Order is critical (e.g., banking transactions)

### SQS Features

**Message Size**
- **1 MiB maximum** per message (raised from 256 KB; older practice questions may still say 256 KB)
- Use SQS Extended Client (Java) to store large payloads in S3

**Visibility Timeout**
- When consumer receives message, it becomes invisible to other consumers
- **Default: 30 seconds** (max 12 hours)
- Consumer must delete message or it returns to queue
- Use `ChangeMessageVisibility` API to extend

**Long Polling**
- Wait for messages to arrive (1-20 seconds)
- Reduces API calls and cost
- **Enable**: Set `ReceiveMessageWaitTimeSeconds` > 0

**Dead Letter Queue (DLQ)**
- Queue for messages that fail processing
- Set **Maximum Receives** threshold
- Use for debugging failed messages

**Delay Queue**
- Delay message delivery up to **15 minutes**
- Default: 0 seconds
- Can override per message with `DelaySeconds`

**Message Retention**
- **1 minute to 14 days**
- Default: 4 days

### SQS Security
- **Encryption**:
  - In-flight: HTTPS
  - At-rest: KMS
- **IAM policies**: Control API access
- **SQS Access Policies**:
  - Cross-account access
  - Allow other services to write (S3, SNS)

### SQS Patterns

**Decoupling**
```
Producer → SQS Queue → Consumer (Auto Scaling based on queue depth)
```

**Fan-out with SNS**
```
SNS Topic → SQS Queue 1
         → SQS Queue 2
         → SQS Queue 3
```

---

## 2. Amazon SNS (Simple Notification Service)

### What is SNS?
- **Pub/Sub messaging** service
- Send messages to **multiple subscribers**
- **Topic**: Logical access point (publishers send here)
- **Subscribers**: Receive all messages

### SNS Subscribers
- **SQS**: Message queues
- **Lambda**: Serverless functions
- **HTTP/HTTPS**: Webhooks
- **Email**: Email notifications
- **SMS**: Text messages
- **Mobile Push**: iOS, Android, Amazon apps
- **Kinesis Data Firehose**: Stream to S3, Redshift

### SNS Features

**Topic Types**
- **Standard**: Best-effort ordering, at-least-once delivery
- **FIFO**: Strict ordering, exactly-once delivery
  - Default 300 messages/sec per topic; high throughput mode raises this to match standard topics
  - Subscribers must be SQS queues (FIFO or standard); email, SMS and HTTP endpoints are not allowed

**Message Filtering**
- Filter messages based on attributes
- Subscribers receive only relevant messages
- JSON policy for filtering

Example Filter Policy:
```json
{
  "event": ["order_placed"],
  "price": [{"numeric": [">", 100]}]
}
```

**Message Size**
- **256 KiB by default**, configurable up to **1 MiB** (`MaximumMessageSize` topic attribute) for SQS, Lambda and Firehose subscriptions

**Fanout Pattern**
- Combine SNS + SQS
- Single SNS message → multiple SQS queues
- Fully decoupled, no data loss
- Each queue can have different consumers

### SNS Security
- **Encryption**:
  - In-flight: HTTPS
  - At-rest: KMS
- **IAM policies**: Control API access
- **SNS Access Policies**:
  - Cross-account access
  - Allow services to publish (S3, CloudWatch)

---

## 3. Amazon EventBridge (CloudWatch Events)

### What is EventBridge?
- **Serverless event bus**
- React to events from AWS services, SaaS apps, custom apps
- **Rules** to route events to targets
- **Successor to CloudWatch Events**

### Event Sources
- **AWS Services**: EC2, S3, RDS, CloudTrail, etc.
- **SaaS Partners**: Datadog, Zendesk, Auth0, etc.
- **Custom Applications**: Your own apps

### Event Targets
- **Lambda**: Invoke functions
- **Step Functions**: Start workflows
- **SNS/SQS**: Send notifications
- **Kinesis**: Stream data
- **ECS Tasks**: Run containers
- **CodePipeline**: Start pipelines
- **SSM**: Run commands
- **And 20+ more...**

### EventBridge Components

**Event Buses**
- **Default Event Bus**: AWS service events
- **Partner Event Bus**: SaaS partner events
- **Custom Event Bus**: Your application events
- Can set **permissions** for cross-account access

**Rules**
- Match event patterns
- Route to one or more targets
- Can have multiple rules per event bus

**Event Pattern Example**
```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["terminated"]
  }
}
```

**Schedule**
- **Cron expressions**: `cron(0 12 * * ? *)`
- **Rate expressions**: `rate(5 minutes)`

### EventBridge Schema Registry
- Discover, create, manage event schemas
- Generate code bindings for applications
- Versioned schemas

### EventBridge vs CloudWatch Events
- EventBridge = CloudWatch Events + more features
- EventBridge supports SaaS integrations
- EventBridge has Schema Registry
- Same API, same pricing

---

## 4. AWS Step Functions

### What is Step Functions?
- **Serverless workflow orchestration**
- Visual workflow editor
- Coordinate Lambda, ECS, Fargate, Batch, SageMaker, etc.
- Handle errors, retries, parallel execution

### Workflow Types

**Standard Workflows**
- **Duration**: Up to 1 year
- **Execution rate**: 2,000 per second
- **Pricing**: Per state transition
- **Use case**: Long-running workflows

**Express Workflows**
- **Duration**: Up to 5 minutes
- **Execution rate**: 100,000+ per second
- **Pricing**: Per execution
- **Use case**: High-volume, short-duration

### Step Functions States

**Task**: Do work (Lambda, ECS, etc.)
**Choice**: Conditional logic
**Parallel**: Execute branches in parallel
**Wait**: Delay for time period
**Succeed**: Successful end
**Fail**: Failure end
**Pass**: Pass input to output
**Map**: Iterate over array

### Example State Machine
```json
{
  "StartAt": "ProcessOrder",
  "States": {
    "ProcessOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:...",
      "Next": "CheckInventory"
    },
    "CheckInventory": {
      "Type": "Choice",
      "Choices": [{
        "Variable": "$.inStock",
        "BooleanEquals": true,
        "Next": "ShipOrder"
      }],
      "Default": "OrderFailed"
    },
    "ShipOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:...",
      "End": true
    },
    "OrderFailed": {
      "Type": "Fail"
    }
  }
}
```

### Error Handling
- **Retry**: Automatic retry with backoff
- **Catch**: Handle errors gracefully
- **Timeout**: Prevent infinite loops

---

## 5. Amazon MQ

### What is Amazon MQ?
- Managed **message broker** service
- Supports **Apache ActiveMQ** and **RabbitMQ**
- **MQTT, AMQP, STOMP, OpenWire** protocols
- Use when migrating from on-premises message brokers

### When to Use
- **Amazon MQ**: Migrating existing apps using open protocols
- **SQS/SNS**: New cloud-native applications

### Amazon MQ Features
- Multi-AZ for high availability
- Automatic failover
- Encryption (at-rest with KMS, in-transit with TLS)

### Amazon SWF (Simple Workflow Service)
- Older workflow service that coordinates tasks across distributed components and keeps workflow state
- **Pull model**: you write *workers* that poll for tasks and *deciders* that choose the next step. Workers can run on EC2 or on premises
- Supports long-running tasks and steps that need a human
- AWS now recommends **Step Functions** for most new workflows. Step Functions pushes tasks to AWS services and needs far less code. On the exam, pick SWF only when the question names SWF-specific pieces such as deciders and workers. Otherwise pick Step Functions

---

## 6. Amazon Kinesis

### Kinesis Family

#### Kinesis Data Streams
- **Real-time data streaming**
- Collect, process, analyze streaming data
- **Retention**: 1-365 days
- **Shards**: Provisioned throughput
  - 1 MB/sec input per shard
  - 2 MB/sec output per shard
- **Use case**: Real-time analytics, log processing

#### Amazon Data Firehose (formerly Kinesis Data Firehose)
- **Load streaming data** into destinations
- **Near real-time**: buffer interval 0-900 seconds (zero buffering delivers within seconds)
- **Destinations**: S3, Redshift, OpenSearch, Splunk, HTTP
- Automatic scaling, no shards
- Can transform data with Lambda
- **Use case**: ETL, data lakes

#### Kinesis Data Analytics (now Amazon Managed Service for Apache Flink)
- Status (November 2026): Kinesis Data Analytics for SQL is discontinued (no new apps from 15 Oct 2025, apps deleted from 27 Jan 2026). Use Amazon Managed Service for Apache Flink.
- **Real-time analytics** on streaming data
- Use **Apache Flink** (Java, Scala, Python, or SQL through Flink Studio)
- Analyze data from Kinesis Data Streams or Firehose
- **Use case**: Real-time dashboards, metrics

#### Kinesis Video Streams
- Stream video from devices to AWS
- Analyze with ML, video processing
- **Use case**: Smart homes, security cameras

### Kinesis vs SQS
- **Kinesis**: Real-time, multiple consumers read same data, ordering per shard
- **SQS**: Message deletion after consumption, simpler

---

## 7. AWS AppSync

### What is AppSync?
- Managed **GraphQL** API service
- Real-time data synchronization
- Offline capabilities for mobile apps
- **Data sources**: DynamoDB, Lambda, HTTP, RDS, OpenSearch

### AppSync Features
- **GraphQL**: Single endpoint for flexible queries
- **Subscriptions**: Real-time updates
- **Resolvers**: Transform GraphQL to data source calls
- **Conflict resolution**: For offline sync

---

## Newer Features to Know

Added after the original SAA-C03 release. Questions can use them, usually as the most managed or lowest-effort option.

| Feature | What it does | Choose it when |
|---------|--------------|----------------|
| EventBridge Pipes | Point-to-point integration: source, optional filter, enrichment, target | Connect SQS, Kinesis, DynamoDB Streams or MSK to a target without glue code |
| EventBridge Scheduler | Serverless scheduler for one-time and recurring tasks at scale, with time zones | Replace cron on EC2 or scheduled rules |
| Step Functions Distributed Map | Runs thousands of parallel child workflows over items such as S3 objects or CSV rows | Large-scale parallel processing of data in S3 |
| Larger payloads | SNS up to 1 MiB when the topic is configured for it; EventBridge events up to 1 MB; SQS messages up to 1 MiB | Avoid claim-check patterns for payloads under 1 MB |

---

## Integration Patterns Summary

### Synchronous
- **API Gateway + Lambda**: RESTful APIs
- **ALB + EC2/ECS**: Traditional load balancing

### Asynchronous
- **SQS**: Queue-based decoupling
- **SNS**: Pub/Sub fanout
- **EventBridge**: Event routing

### Streaming
- **Kinesis**: Real-time data streams
- **Kafka (MSK)**: Managed Apache Kafka

### Workflow
- **Step Functions**: Orchestrate services
- **SWF**: Legacy workflow service

---

## Practice Questions

**Q1.** What is the maximum message size in SQS?
- A. 64 KB
- B. 128 KB
- C. 256 KB
- D. 1 MiB

**Answer**: D (the limit was raised from 256 KB to 1 MiB; older practice material may still say 256 KB)

**Q2.** Which service provides exactly-once message processing with strict ordering?
- A. SQS Standard
- B. SQS FIFO
- C. SNS Standard
- D. SNS FIFO

**Answer**: B

**Q3.** How can you send a single message to multiple SQS queues?
- A. Use SQS fanout
- B. Use SNS topic with multiple SQS subscribers
- C. Use Lambda to forward messages
- D. Not possible

**Answer**: B

**Q4.** What is the maximum retention period for SQS messages?
- A. 4 days
- B. 7 days
- C. 14 days
- D. 30 days

**Answer**: C

---

## Key Takeaways

 SQS for decoupling, SNS for pub/sub fanout  
 SQS FIFO for exactly-once, ordered processing  
 EventBridge for event-driven architectures (AWS + SaaS events)  
 Step Functions for workflow orchestration  
 Kinesis for real-time streaming data  
 Use SNS + SQS fanout pattern for multiple consumers  
 SQS visibility timeout prevents duplicate processing  
 EventBridge has built-in integrations with 20+ AWS services  
 Choose SQS/SNS for new apps, Amazon MQ for migrations  
 Kinesis Data Streams for real-time, Firehose for near real-time  

---

**Previous Module**: [Module 07: Security & Compliance](../07-Security/README.md)  
**Next Module**: [Module 09: Monitoring & Management](../09-Monitoring/README.md)

