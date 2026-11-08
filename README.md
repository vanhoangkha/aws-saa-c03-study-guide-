# AWS Certified Solutions Architect – Associate (SAA-C03) Study Guide

[![Checks](https://github.com/vanhoangkha/aws-saa-c03-study-guide-/actions/workflows/checks.yml/badge.svg)](https://github.com/vanhoangkha/aws-saa-c03-study-guide-/actions/workflows/checks.yml)
[![Pages](https://github.com/vanhoangkha/aws-saa-c03-study-guide-/actions/workflows/pages.yml/badge.svg)](https://github.com/vanhoangkha/aws-saa-c03-study-guide-/actions/workflows/pages.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Free study notes, diagrams and practice questions for the SAA-C03 exam, organised in 14 modules. Each module comes in three lengths, so you can pick the one that fits the time you have.

- [Exam simulator](https://vanhoangkha.github.io/aws-saa-c03-study-guide-/simulator/): a timed 65-question, 130-minute exam or a single-topic drill, drawn from 298 questions. Scores and history stay in your browser. There is no sign-up and no tracking.
- [Study site](https://vanhoangkha.github.io/aws-saa-c03-study-guide-/): the same modules with search, learning paths, the exam domain breakdown and a score tracker.
- [Exam-day reference card](exam-reviews/quick-reference/ULTRA-QUICK-REFERENCE-CARD.md): rules, edge cases, service selection and limits for the last 30 minutes.

## Contents

- [The exam](#the-exam)
- [Where to start](#where-to-start)
- [Modules](#modules)
- [Other material](#other-material)
- [Practice test reviews](#practice-test-reviews)
- [Repository layout](#repository-layout)
- [Eight-week plan](#eight-week-plan)
- [Study and exam tips](#study-and-exam-tips)
- [Contributing](#contributing)
- [License and disclaimers](#license-and-disclaimers)

## The exam

| | |
|---|---|
| Code | SAA-C03 |
| Length | 130 minutes, 65 questions (multiple choice and multiple response) |
| Passing score | 720 out of 1000 |
| Cost | 150 USD |
| Validity | 3 years |
| Delivery | Online proctored or at a test centre |

| Domain | Weight |
|--------|--------|
| 1. Design secure architectures | 30% |
| 2. Design resilient architectures | 26% |
| 3. Design high-performing architectures | 24% |
| 4. Design cost-optimized architectures | 20% |

## Where to start

Every module has three versions of the same material:

| Version | File | Time per module | All 14 modules |
|---------|------|-----------------|----------------|
| Ultra-fast | `ULTRA-FAST-LEARN.md` | about 15 min | 3-4 h |
| Fast | `FAST-LEARN.md` | about 60 min | 11-14 h |
| Full | `README.md` | about 3 h | 40-60 h |

**New to AWS.** Follow the [eight-week roadmap](docs/study-guides/STUDY-ROADMAP.md), starting with [Module 01](01-AWS-Fundamentals/README.md). Open a [free-tier account](https://aws.amazon.com/free/) and build what you read about.

**Already using AWS.** Read the [ultra-fast index](docs/study-guides/ULTRA-FAST-LEARNING-INDEX.md) to find gaps, check the [quick reference](docs/reference/QUICK-REFERENCE.md), then read the fast or full version of the weak modules. Finish with the questions in [Module 14](14-Practice/README.md).

**Final week.** Go through the [ultra-fast](docs/study-guides/ULTRA-FAST-LEARNING-INDEX.md) and [fast](docs/study-guides/FAST-LEARN-GUIDE.md) guides, the [mnemonics](docs/study-guides/QUICK-STUDY-NOTES.md) and the [visual guide](docs/reference/VISUAL-GUIDE.md), and take timed mock exams.

**Day before.** Ultra-fast guides in the morning, the [Module 14 exam tips](14-Practice/ULTRA-FAST-LEARN.md) in the afternoon, a light pass over the mnemonics in the evening, and the [reference card](exam-reviews/quick-reference/ULTRA-QUICK-REFERENCE-CARD.md) just before the exam.

## Modules

| # | Module | Ultra-fast | Fast | Full | Diagrams | Questions |
|---|--------|-----------|------|------|----------|-----------|
| 01 | AWS Fundamentals | [Ultra](01-AWS-Fundamentals/ULTRA-FAST-LEARN.md) | [Fast](01-AWS-Fundamentals/FAST-LEARN.md) | [Full](01-AWS-Fundamentals/README.md) | [Diagrams](01-AWS-Fundamentals/DIAGRAMS.md) | [Questions](01-AWS-Fundamentals/PRACTICE-QUESTIONS.md) |
| 02 | IAM | [Ultra](02-IAM/ULTRA-FAST-LEARN.md) | [Fast](02-IAM/FAST-LEARN.md) | [Full](02-IAM/README.md) | [Diagrams](02-IAM/DIAGRAMS.md) | [Questions](02-IAM/PRACTICE-QUESTIONS.md) |
| 03 | Compute (EC2, Lambda, containers) | [Ultra](03-Compute/ULTRA-FAST-LEARN.md) | [Fast](03-Compute/FAST-LEARN.md) | [Full](03-Compute/README.md) | [Diagrams](03-Compute/DIAGRAMS.md) | [Questions](03-Compute/PRACTICE-QUESTIONS.md) |
| 04 | Storage (S3, EBS, EFS) | [Ultra](04-Storage/ULTRA-FAST-LEARN.md) | [Fast](04-Storage/FAST-LEARN.md) | [Full](04-Storage/README.md) | [Diagrams](04-Storage/DIAGRAMS.md) | [Questions](04-Storage/PRACTICE-QUESTIONS.md) |
| 05 | Databases | [Ultra](05-Database/ULTRA-FAST-LEARN.md) | [Fast](05-Database/FAST-LEARN.md) | [Full](05-Database/README.md) | [Diagrams](05-Database/DIAGRAMS.md) | [Questions](05-Database/PRACTICE-QUESTIONS.md) |
| 06 | Networking (VPC) | [Ultra](06-Networking/ULTRA-FAST-LEARN.md) | [Fast](06-Networking/FAST-LEARN.md) | [Full](06-Networking/README.md) | [Diagrams](06-Networking/DIAGRAMS.md) | [Questions](06-Networking/PRACTICE-QUESTIONS.md) |
| 07 | Security | [Ultra](07-Security/ULTRA-FAST-LEARN.md) | [Fast](07-Security/FAST-LEARN.md) | [Full](07-Security/README.md) | [Diagrams](07-Security/DIAGRAMS.md) | [Questions](07-Security/PRACTICE-QUESTIONS.md) |
| 08 | Application Integration | [Ultra](08-Application-Integration/ULTRA-FAST-LEARN.md) | [Fast](08-Application-Integration/FAST-LEARN.md) | [Full](08-Application-Integration/README.md) | [Diagrams](08-Application-Integration/DIAGRAMS.md) | [Questions](08-Application-Integration/PRACTICE-QUESTIONS.md) |
| 09 | Monitoring | [Ultra](09-Monitoring/ULTRA-FAST-LEARN.md) | [Fast](09-Monitoring/FAST-LEARN.md) | [Full](09-Monitoring/README.md) | [Diagrams](09-Monitoring/DIAGRAMS.md) | [Questions](09-Monitoring/PRACTICE-QUESTIONS.md) |
| 10 | Migration and Transfer | [Ultra](10-Migration/ULTRA-FAST-LEARN.md) | [Fast](10-Migration/FAST-LEARN.md) | [Full](10-Migration/README.md) | [Diagrams](10-Migration/DIAGRAMS.md) | [Questions](10-Migration/PRACTICE-QUESTIONS.md) |
| 11 | Analytics | [Ultra](11-Analytics/ULTRA-FAST-LEARN.md) | [Fast](11-Analytics/FAST-LEARN.md) | [Full](11-Analytics/README.md) | [Diagrams](11-Analytics/DIAGRAMS.md) | [Questions](11-Analytics/PRACTICE-QUESTIONS.md) |
| 12 | Architecture Patterns | [Ultra](12-Architecture-Patterns/ULTRA-FAST-LEARN.md) | [Fast](12-Architecture-Patterns/FAST-LEARN.md) | [Full](12-Architecture-Patterns/README.md) | [Diagrams](12-Architecture-Patterns/DIAGRAMS.md) | [Questions](12-Architecture-Patterns/PRACTICE-QUESTIONS.md) |
| 13 | Cost Optimization | [Ultra](13-Cost-Optimization/ULTRA-FAST-LEARN.md) | [Fast](13-Cost-Optimization/FAST-LEARN.md) | [Full](13-Cost-Optimization/README.md) | [Diagrams](13-Cost-Optimization/DIAGRAMS.md) | [Questions](13-Cost-Optimization/PRACTICE-QUESTIONS.md) |
| 14 | Practice and Exam Prep | [Ultra](14-Practice/ULTRA-FAST-LEARN.md) | [Fast](14-Practice/FAST-LEARN.md) | [Full](14-Practice/README.md) | – | [Questions](14-Practice/PRACTICE-QUESTIONS.md) |

The modules hold about 217 Mermaid diagrams and 276 practice questions with explanations. Module 11 also has [notes on the AWS ML services](11-Analytics/AWS-ML-SERVICES-NOTES.md).

## Other material

| Document | Time | Contents |
|----------|------|----------|
| [Ultra-fast index](docs/study-guides/ULTRA-FAST-LEARNING-INDEX.md) | 3-4 h | Links to every ultra-fast summary |
| [Fast-learn guide](docs/study-guides/FAST-LEARN-GUIDE.md) | 11-14 h | Condensed notes with decision trees |
| [Diagram index](docs/reference/DIAGRAMS-INDEX.md) | 2-3 h | Every diagram, by module |
| [Quick study notes](docs/study-guides/QUICK-STUDY-NOTES.md) | 1-2 h | Mnemonics and shortcuts |
| [Flashcards](docs/study-guides/FLASHCARDS.md) | 30-60 min | Question-and-answer cards |
| [Quick reference](docs/reference/QUICK-REFERENCE.md) | 15 min | Service lookup table |
| [Architecture pattern sheet](docs/reference/SAA-ARCHITECTURE-PATTERN-MASTER-SHEET.md) | 30 min | Common scenario-to-architecture mappings |
| [Study roadmap](docs/study-guides/STUDY-ROADMAP.md) | – | The eight-week plan in detail |

External notes: the [AWS SAA-C02 Study Guide](https://github.com/keenanromain/AWS-SAA-C02-Study-Guide) by Keenan Romain, mirrored as [rdurelli/AWS-SAA-C03-Study-Guide](https://github.com/rdurelli/AWS-SAA-C03-Study-Guide). It is included as a git submodule in [external/aws-saa-c02-study-guide](external/aws-saa-c02-study-guide), which links to that repository rather than copying it. Its content belongs to its authors and carries no license. It was written for the previous exam version (SAA-C02), so check anything that may have changed against the current AWS documentation. To download it with this repository:

```bash
git clone --recurse-submodules https://github.com/vanhoangkha/aws-saa-c03-study-guide-.git
# or, in an existing clone
git submodule update --init
```

## Practice test reviews

[exam-reviews/](exam-reviews/README.md) analyses seven [Whizlabs](https://www.whizlabs.com/) practice tests taken in March 2026:

| Test | Score | Result |
|------|-------|--------|
| [1](exam-reviews/complete-reviews/Practice-Test-1-Review.md) | 34/65 (52%) | Fail |
| [2](exam-reviews/complete-reviews/Practice-Test-2-Review.md) | 49/65 (75%) | Borderline |
| [3](exam-reviews/complete-reviews/Practice-Test-3-Review.md) | 52/65 (80%) | Pass |
| [4](exam-reviews/complete-reviews/Practice-Test-4-Review.md) | 49/65 (75%) | Borderline |
| [5](exam-reviews/complete-reviews/Practice-Test-5-Review.md) | 42/65 (65%) | Fail |
| [6](exam-reviews/complete-reviews/Practice-Test-6-Review.md) | 52/65 (80%) | Pass |
| [7](exam-reviews/complete-reviews/Practice-Test-7-Review.md) | 48/65 (74%) | Borderline |

The average is 71%. Scores rose from 52% to 80% over the first six tests, then fell to 74% on test 7. Each review breaks the score down by domain, explains every missed question, and lists the topics to revisit.

The [65 reinforcement questions](exam-reviews/REINFORCEMENT-QUESTIONS-ALL-TESTS.md) are new questions written around those misses, with explanations, CLI and code examples. Answer them without looking, score yourself in the [tracker](exam-reviews/STUDY-PROGRESS-TRACKER.md), and retake them after a day and after a week.

## Repository layout

```
01-AWS-Fundamentals/ … 14-Practice/
    ULTRA-FAST-LEARN.md      15-minute summary
    FAST-LEARN.md            60-minute notes
    README.md                full module
    DIAGRAMS.md              Mermaid diagrams
    PRACTICE-QUESTIONS.md    questions with explanations
exam-reviews/                practice test reviews and exam-day cards
docs/
    study-guides/            ultra-fast and fast indexes, flashcards, roadmap
    reference/               quick reference, diagram index, visual guide
    exam-analysis/           topic coverage against the exam guide
simulator/                   exam simulator (static page + question bank)
external/                    SAA-C02 study guide (git submodule, not part of this repository)
scripts/                     link and Mermaid checks, simulator smoke test
index.html                   study site
```

The simulator's question bank, `simulator/questions.js`, is generated from the modules' `PRACTICE-QUESTIONS.md` files by `simulator/build_questions.py`.

## Eight-week plan

| Week | Focus | Modules |
|------|-------|---------|
| 1-2 | Foundations | Fundamentals, IAM, Compute |
| 3-4 | Storage and data | Storage, Databases, Analytics |
| 5-6 | Networking and security | Networking, Security, Application Integration |
| 7 | Remaining services | Migration, Cost Optimization, Monitoring |
| 8 | Practice | Mock exams and weak areas |

Details are in the [study roadmap](docs/study-guides/STUDY-ROADMAP.md).

## Study and exam tips

- Book the exam first. A fixed date keeps the schedule honest.
- Build things in a [free-tier account](https://aws.amazon.com/free/). Hands-on work sticks better than reading.
- Write summaries in your own words, and review them several times over several weeks.
- Take timed mock exams so the pacing is familiar. That's about two minutes per question.
- In the exam, watch for qualifiers such as MOST, LEAST and BEST. Eliminate wrong answers first. Flag uncertain questions and come back to them before you submit.

Official sources worth reading alongside these notes: the [Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), the [Architecture Center](https://aws.amazon.com/architecture/), [Skill Builder](https://skillbuilder.aws/) and the [service FAQs](https://aws.amazon.com/faqs/).

## Contributing

Corrections and additions are welcome. Fork the repository, make your change on a branch, and open a pull request against `master`. [CONTRIBUTING.md](CONTRIBUTING.md) covers the content rules, and [CONTRIBUTORS.md](CONTRIBUTORS.md) lists the people who have helped. To report an error, [open an issue](../../issues/new/choose); security problems go through [SECURITY.md](SECURITY.md). [CHANGELOG.md](CHANGELOG.md) records what changed between releases.

## License and disclaimers

MIT. See [LICENSE](LICENSE) and [NOTICE](NOTICE) for attribution of the original guide.

This guide is written by the community and is not affiliated with, endorsed by or sponsored by Amazon Web Services. AWS and related marks belong to Amazon.com, Inc. or its affiliates.

The content is original or based on public AWS documentation. It contains no real exam questions and no material copied from paid courses or books, in line with the [AWS Certification Program Agreement](https://aws.amazon.com/certification/certification-agreement/). See [CONTENT-POLICY.md](CONTENT-POLICY.md).

The notes are for study only and come with no guarantee of passing. When something here disagrees with the [AWS documentation](https://docs.aws.amazon.com/) or the [official exam guide](https://aws.amazon.com/certification/certified-solutions-architect-associate/), trust the official source.
