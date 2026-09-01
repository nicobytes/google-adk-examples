# agent-skills

Public sample agent for [Skills in ADK agents](https://adk.dev/skills/).

**Harbor Roast Coffee** is a fictional cafe brand. All data is invented for
demonstration. Skills live in folders under `app/skills/` — no runtime skill
binding, no vector RAG. The agent uses **progressive disclosure**:

- **L1** — skill name + description (always visible via `list_skills`)
- **L2** — playbook in each `SKILL.md` body (loaded with `load_skill`)
- **L3** — knowledge in `references/*.md` (loaded with `load_skill_resource`)

This pattern loads only the slice a turn needs, similar to retrieval but with
explicit rules in L2 and predictable routing in L1.

## Project structure

```
agent-skills/
├── app/
│   ├── agent.py          # load_skill_from_dir + SkillToolset
│   ├── prompt.py
│   ├── tools.py          # get_now() for promo dates
│   └── skills/
│       ├── locations/      # addresses, hours, contact
│       ├── coffee-menu/    # drinks, prices, customizations
│       ├── food-menu/      # pastries, allergens (Marina-only items)
│       ├── promotions/     # Status ACTIVE/INACTIVE
│       ├── faqs/
│       └── escalate/       # human handoff (no L3)
├── tests/
└── pyproject.toml
```

## Quick start

```bash
cd agents/agent-skills
agents-cli install
agents-cli playground
uv run pytest tests/unit tests/integration
```

Ask in the playground:

- "Where is the downtown shop?"
- "How much is a 16 oz latte?"
- "Do you have Spring Roast Week promo?"
- "Can I get an almond croissant downtown?"

## Skills as RAG

| Without skills (full KB in prompt) | With skills (this sample) |
|---|---|
| All menu + policies every turn | L1 metadata only at start |
| Rules may not be retrieved | L2 rules load with the skill |
| Chunks by embedding similarity | L3 by explicit file name |

## License

Apache-2.0 (Google LLC sample code). Harbor Roast content is fictional.
