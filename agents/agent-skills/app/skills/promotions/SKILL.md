---
name: promotions
description: >
  Temporary promotions and discounts at Harbor Roast. Use when the customer
  mentions promo, discount, deal, or Spring Roast Week. Always check Status
  ACTIVE/INACTIVE and dates with get_now before applying a benefit.
metadata:
  author: harbor-roast-sample
  version: "1.0"
---

# Promotions

## Instructions

1. Call `load_skill` and load `references/promotions.md` with `load_skill_resource`.
2. Use `get_now` to compare against validity dates when needed.
3. **Status switch:** only apply a promotion when **Status** is **ACTIVE**.
   If **INACTIVE**, do not offer the benefit even if today's date falls in the
   validity window.
4. Promotions do not permanently change regular menu prices in `coffee-menu`.
5. Unless the promotion says it stacks, do not combine with other discounts.
