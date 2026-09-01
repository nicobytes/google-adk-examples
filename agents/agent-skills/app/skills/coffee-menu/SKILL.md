---
name: coffee-menu
description: >
  Harbor Roast coffee and espresso menu: drink list, sizes, prices, milk options,
  and add-ons. Use when the customer asks about latte, cold brew, espresso,
  cappuccino, prices, sizes (12oz/16oz), or drink customizations.
metadata:
  author: harbor-roast-sample
  version: "1.0"
---

# Coffee menu

## Instructions

1. Call `load_skill` before answering coffee menu or pricing questions.
2. Load only what you need with `load_skill_resource`:
   - **Drink catalog:** `references/drinks.md`
   - **Sizes and prices:** `references/sizes-prices.md`
   - **Milk, shots, syrups:** `references/customizations.md`
3. Use precomputed prices from `sizes-prices.md` first. Do not invent prices.
4. If a promotion might apply, check `promotions` before quoting a discounted price.
5. Food and pastry questions belong in `food-menu`.
