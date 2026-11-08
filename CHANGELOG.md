# Changelog

Notable changes to this study guide. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.0.0] - 2026-11-08

First release of this repository, based on the MIT-licensed study guide by ChathurangaVKD (see [LICENSE](LICENSE)).

### Added
- `external/aws-saa-c02-study-guide`: the rdurelli study guide as a git submodule. It has no license, so it is linked rather than copied.
- Original sections for topics only that guide covered: EC2 Hibernate and Amazon WorkSpaces (03), Data Lifecycle Manager (04), Amazon SWF (08), OpsWorks retirement (09), Elastic Transcoder end of support and MediaConvert (11).
- `scripts/check_links.py` and a `Checks` workflow that verifies links, heading anchors and the simulator build on every push and pull request.
- `docs/REFERENCES.md`: official AWS sources for the exam in one place (exam guide, Well-Architected pillars, 22 decision guides, whitepapers, documentation and FAQs for every module, pricing, quotas, hands-on labs) plus the community guides this repository builds on. `scripts/check_external_links.py` and a monthly workflow keep the links working.
- Repository standards: issue forms, pull request checklist, CODEOWNERS, Dependabot for GitHub Actions, `.editorconfig`, `.gitattributes` (LF line endings), and a NOTICE file with attribution and trademark notices.

### Changed
- Removed the bundled copy of the AWS exam guides PDF; the guides are linked from the AWS documentation instead.
- Removed emoji, icons and promotional or motivational filler from all pages, the study site and the simulator. Table cells that held only an icon now say Yes, No, Partial or Low/Medium/High.
- In `14-Practice/PRACTICE-QUESTIONS.md` the correct option is marked with `(correct)`; the simulator build reads that marker.
- Rewrote README, CONTRIBUTING, the docs and exam-review indexes, and the scripts guide.
- GitHub Pages builds from `master` and publishes under `/aws-saa-c03-study-guide-/`.

### Fixed
- Rewrote the QuickSight pricing notes for Amazon Quick Sight (part of Amazon Quick): pricing model by role, Pro roles, SPICE and session capacity, without dated dollar figures.
- Second fact-check pass against current AWS documentation: EventBridge 1 MB events, 400 Gbps Direct Connect, 5 Gbps VPN tunnels, Database Savings Plans, six Trusted Advisor categories, Inspector pricing, CloudFront 1 TB free tier, trusted key groups, WAF rate-based windows, EBS quotas, OpenSearch naming, Amazon Q Developer in chat applications, and SQL Server read replicas (15).
- Reviewed every module, practice test review, flashcard set and reinforcement question against current AWS documentation and corrected about 470 technical errors, including:
  - Exam facts: domain weights 30/26/24/20, scaled passing score 720.
  - Quotas: 15 RDS read replicas, NAT gateway 100 Gbps and 55,000 connections per destination, SQS 1 MiB messages, KMS request quotas and rotation periods.
  - Behaviour: S3 lifecycle minimum durations, multipart thresholds, NLB client IP preservation, ALB rule priority, cross-account policy evaluation, Multi-AZ DB clusters, Aurora Global Database.
  - Pricing: Savings Plans and Reserved Instance discounts, free Glacier Bulk retrievals, Redshift RA3 storage, Transit Gateway charges.
  - Answer keys that were wrong or ambiguous, and CLI commands, JSON policies and CloudFormation snippets that would not run.
  - Status notes for retired or closed services (Snow Family devices, Migration Hub, QLDB, App Mesh, S3 Select, CloudTrail Lake and others).
- 17 dead or redirected AWS documentation links in the modules and reviews.
- Broken Mermaid state diagram in `13-Cost-Optimization/DIAGRAMS.md` and two dead anchors in the flashcards table of contents.

### Security
- GitHub Actions are pinned to commit SHAs, checkouts do not keep credentials, and the Pages deploy token is scoped to the deploy job only.
- SECURITY.md points to GitHub private vulnerability reporting.

## [1.x] - 2026-01-02

Releases of the original guide: the 14 modules, quick-learning guides, flashcards, diagrams, practice questions and the exam simulator. Their history is in the original repository.
