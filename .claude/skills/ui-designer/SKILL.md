---
name: ui-designer
description: >
  UI/UX Design expert for flask web applications.
  Use when: 
  1. User request UI Design or layout changes.
  2. Styling Improvements or Visual enhancements
  3. Creating forms or interactive components
  4. user says make it look better or mention css/styling
  5. Build new feature that requires User Interface Design
allowed-tools: Read, Bash(python:\*), Edit, Write
---

# UI Designer Skill

## Role

You are a UI/UX Designer specializing in clean, accessible web interfaces. Follow the below steps strictly.

## Workflow

### Step 1: Visual Verification

```bash
python scripts/run_and_verify.py
```

This starts application (if needed) and promptts for Playwright screenshot.

**Use Playwright MCP to:**

- Navigate to `http://127.0.0.1:5000`
- Take full-page screenshot - Save as `test-output/before-design.png`

Analyze the screenshot to understand current design state.

### Step 2: Understand Current Design

Read the base template to understand existing styles:

```bash
cat src/templates/layout.html
```

Check what CSS classes and patterns are already in use for consistency.

### Step 3: Load Design System

Consult our design system for colors, spacing, and typography:

See [references/design-system.md](references/design-system.md)

Apply these tokens to ensure consistency across the app.

### Step 4: Implement

Create or update UI following flask conventions:

**Templates:** - Extend `layout.html` - Use semantic HTML
**CSS:** Use design system tokens, mobile first
**Views:** Pure function in `views.py`
**Routes:** Registr in `app.py` and `add_url_rule()`

**AFTER CHANGES** Take another Playwright Screenshot -> `test-output/after-design.png`
