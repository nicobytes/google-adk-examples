---
name: faqs
description: >
  Frequently asked questions about Harbor Roast coffee and food. Use for common
  questions about caffeine, oat milk, pastry freshness, or what to expect. For
  exact prices use coffee-menu or food-menu.
metadata:
  author: harbor-roast-sample
  version: "1.0"
---

# FAQs

## Instructions

1. Call `load_skill` before answering FAQ-style questions.
2. Load the relevant reference:
   - **Coffee FAQs:** `references/coffee-faqs.md`
   - **Food FAQs:** `references/food-faqs.md`
3. FAQs are complementary: if an exact price is in `coffee-menu` or `food-menu`,
   prefer those skills for pricing.
4. Use `escalate` for medical advice, severe allergy protocols, or unlisted items.
