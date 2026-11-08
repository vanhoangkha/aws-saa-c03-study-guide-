# Scripts

Maintenance scripts for the study guide. Run them from the repository root.

| Script | What it does | Changes files |
|--------|--------------|---------------|
| `check_links.py` | Checks every relative link and heading anchor in the tracked Markdown files. Exits with 1 if one does not resolve. Runs in CI. | No |
| `validate_mermaid.py` | Looks for common Mermaid syntax problems in the `DIAGRAMS.md` files (quoted subgraph names, unescaped `<` and `>`, mismatched quotes, `style` in sequence diagrams, floating nodes). Exits with 1 if it finds any. | No |
| `fix_diagram_rendering.py` | Repairs malformed node brackets and escaped `<br/>` tags in the `DIAGRAMS.md` files. | Yes |
| `add_disclaimers.py` | Adds the "original practice questions, not exam questions" note to every `PRACTICE-QUESTIONS.md` that lacks it. | Yes |
| `count_stats.py` | Prints the number of practice questions per module. | No |
| `simulator_smoke_test.js` | Loads the simulator in jsdom and runs a full exam, the weak-area mode and a domain quiz. Needs `npm install jsdom`. | No |

The simulator question bank is built by `simulator/build_questions.py`.

## Usage

```bash
python3 scripts/check_links.py
python3 scripts/validate_mermaid.py
node scripts/simulator_smoke_test.js simulator/
```

Review `git diff` after running a script that changes files.
