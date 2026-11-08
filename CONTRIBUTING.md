# Contributing

Corrections, new questions, diagrams and clearer explanations are all welcome. Everyone taking part is expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Reporting a problem

Open an issue with the "Content error" form. Say which file and section is wrong, what it says now, what it should say, and link the AWS documentation that backs the correction.

For new topics or larger changes, use the "Content request" form first so the scope can be agreed before you write it.

## Making a change

1. Fork the repository and create a branch, for example `fix/s3-object-lock-retention`.
2. Edit the files. Follow the content and style rules below.
3. If you changed a `DIAGRAMS.md`, check the Mermaid syntax:
   ```bash
   python3 scripts/validate_mermaid.py
   python3 scripts/fix_diagram_rendering.py   # optional: repairs broken brackets
   git diff                                   # review what the fixer changed
   ```
4. If you changed a `PRACTICE-QUESTIONS.md`, rebuild the simulator's question bank and commit `simulator/questions.js` with it:
   ```bash
   python3 simulator/build_questions.py
   ```
5. Check that links and heading anchors still resolve:
   ```bash
   python3 scripts/check_links.py
   ```
   The same check, and the question-bank build, run on every pull request.
6. Commit, push and open a pull request against `master`. Fill in the template and link any related issue.

Pull requests are reviewed for technical accuracy, relevance to SAA-C03, consistency with the existing material, and originality. Expect a first review within a week.

## Content rules

- Write original material. Do not copy real exam questions, brain dumps, or text from paid courses and books. See [CONTENT-POLICY.md](CONTENT-POLICY.md).
- Back technical claims with AWS documentation, and link it where a reader might want to check.
- Stay within what SAA-C03 tests. Deep implementation detail belongs in the AWS docs, not here.
- Practice questions need four options (or more for multiple response), the answer, and an explanation of why each wrong option is wrong. In `14-Practice/PRACTICE-QUESTIONS.md`, mark the right option by ending its line with `(correct)`; the simulator build reads that marker.

## Style

- Plain, direct English. State the fact; skip the build-up, the hype and the encouragement.
- No emoji or pictographic icons, in prose, headings, tables or diagrams. Use words: Yes/No in tables, "Correct"/"Wrong" in answer lists.
- Use the official service name on first mention ("Amazon S3"), the short name after ("S3"). Define acronyms on first use.
- `code` formatting for CLI commands, API names and parameters.
- Hyphens for bullet lists, two-space indents for sub-items. Fenced code blocks with a language tag.
- Mermaid for architecture diagrams. Keep node labels short.

A full module (`README.md`) follows this outline:

```markdown
# Module XX: Topic

## Overview
## Key Services
## 1. First service
### What it is
### Key features
### Use cases
### Exam tips
## Summary
## Hands-on practice
```

## Commit messages

```
Type: short summary in the imperative (50 characters or less)

Why the change was needed and what it does, wrapped at 72 characters.

Fixes #123
```

Types: `Add`, `Fix`, `Update`, `Refactor`, `Docs`, `Style`.

## License

By contributing you agree that your work is released under the [MIT License](LICENSE).
