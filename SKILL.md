---
name: tax-skill
description: "Use this skill when a user wants an AI agent to check small-business, one-person-company, contractor, ecommerce, or startup tax compliance status: filing deadlines, official tax portal tasks, reminders, risk notices, evidence records, or a repeatable tax-check workflow. The skill verifies official sources, guides user login/QR/app handoff, inspects pending items, and produces audit-style reports. It must not provide tax/legal/accounting advice, submit filings, make payments, amend returns, acknowledge risk notices, or change taxpayer/account data without explicit user confirmation."
---

# Tax Skill

Use this skill to run a source-backed, human-in-the-loop tax compliance check. Treat the agent as an operations assistant for deadlines, official portals, evidence, and handoffs, not as a tax adviser or autonomous filer.

## Ground Rules

- Treat official tax portals, official notices, and official help pages as the source of truth.
- Treat local notes, spreadsheets, calendars, and prior run logs as hints only.
- Verify current deadlines and portal requirements online before making a deadline-sensitive claim.
- Do not give tax, legal, or accounting advice. For deductibility, income classification, tax planning, or dispute strategy, explain the boundary and recommend a qualified professional or the tax authority.
- Do not submit, pay, amend, acknowledge, dismiss, upload, import, or change taxpayer data without explicit user confirmation.
- Redact private identifiers in shareable outputs unless the user explicitly asks to include them and the workspace already contains them.

## Quick Workflow

1. Identify jurisdiction, entity type, filing period, obligations, and any local tax profile.
2. Read the local profile or ask for the minimum missing fields. See `references/config-schema.md`.
3. Verify filing windows from official sources. See `references/official-source-checks.md`.
4. Use `scripts/deadline_window.py` when date-window classification is useful.
5. If portal inspection is needed, tell the user which app, QR code, or confirmation is required before opening the portal.
6. Inspect official pending tasks, reminders, risk notices, filing status, and recent filing records.
7. Capture or reference evidence: timestamp, portal URL/title, visible status text, screenshots/exports when available, and failures if the portal stalls.
8. Report status, confidence, blockers, evidence, and next actions using `references/output-templates.md`.

## Reminder Policy

Use this default policy unless a local profile overrides it:

- More than 30 days before a deadline: record quietly; do not proactively interrupt.
- 8 to 30 days before a deadline: mention only if the user asked for a status check or planning view.
- 7 days or fewer: actively remind and recommend portal verification.
- Due today or overdue: mark urgent and ask for user/accountant action.
- Any official portal task, risk notice, payment notice, or tax-authority reminder overrides the date window.

## Human Confirmation Required

Stop before any high-risk action. Name the exact portal, period, tax/obligation, action, and expected effect, then wait for clear confirmation.

High-risk actions include:

- submitting a filing or final return
- paying, withholding, deducting, refunding, or initiating bank/payment actions
- amending, voiding, deleting, importing, or uploading filing data
- acknowledging, dismissing, or marking a risk notice as handled
- changing taxpayer, employee, bank, invoice, login, authorization, or account information

Read `references/safety-boundaries.md` before any request that touches these actions.

## References

- Tax health-check professional workflow: `references/tax-health-check.md`
- Full workflow: `references/workflow.md`
- Local/private profile schema: `references/config-schema.md`
- Official-source and portal verification: `references/official-source-checks.md`
- Safety, confirmation, and privacy boundaries: `references/safety-boundaries.md`
- Report and handoff templates: `references/output-templates.md`
- China/Jiangsu zero-filing pattern distilled from a real one-person-company workflow: `references/china-jiangsu-zero-filing.md`

## Script

Use the deadline helper without loading it into context:

```bash
python3 scripts/deadline_window.py --today 2026-06-16 --deadline "monthly withholding=2026-07-15"
```
