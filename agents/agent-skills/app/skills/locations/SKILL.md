---
name: locations
description: >
  Harbor Roast store locations, addresses, hours, and contact channels. Use when
  the customer asks where a shop is, opening hours, phone, email, or which
  neighborhood a cafe is in (Downtown Pier District or Marina).
metadata:
  author: harbor-roast-sample
  version: "1.0"
---

# Locations and hours

## Instructions

1. Call `load_skill` before answering location or hours questions.
2. Load only the reference you need with `load_skill_resource`:
   - **Addresses and neighborhoods:** `references/addresses.md`
   - **Opening hours:** `references/hours.md`
   - **Phone, email, social:** `references/contact.md`
3. Answer only from the loaded reference. Do not invent addresses or hours.
4. If the customer asks about menu availability at a specific store, use
   `food-menu` or `coffee-menu` after confirming the location.
5. For holiday hours or exceptions not listed, use `escalate`.
