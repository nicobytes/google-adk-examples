---
name: food-menu
description: >
  Harbor Roast pastries and food: croissants, muffins, availability by store,
  and allergen notes. Use when the customer asks about food, pastries, almond
  croissant, muffins, gluten, or nuts.
metadata:
  author: harbor-roast-sample
  version: "1.0"
---

# Food menu

## Instructions

1. Call `load_skill` before answering food or pastry questions.
2. Load references as needed:
   - **Pastries and availability by store:** `references/pastries.md`
   - **Allergens and dietary notes:** `references/allergens.md`
3. **Store-specific items:** if a pastry is listed for one location only, do not
   say it is available at the other store.
4. Coffee drink prices are in `coffee-menu`, not here.
