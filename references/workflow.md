# Tax Compliance Workflow

Use this reference for the full operating flow after `SKILL.md` triggers.

## Decision Tree

- Status check: run intake, verify official deadlines, inspect portals if the user can log in, then report.
- Reminder setup: define obligations, official deadline sources, reminder windows, and evidence location. Do not invent recurring automation unless the user asks for it.
- Direct submit request: switch to safety mode, explain that final filing requires explicit confirmation, and inspect/pre-fill only when the user authorizes that scope.
- Tax advice request: do not answer as an adviser. Help collect facts, official links, and questions for a qualified accountant or tax authority.

## Intake

Collect only the minimum needed:

- jurisdiction: country, state/province/city if relevant
- entity type: individual, sole proprietor, LLC/company, small-scale taxpayer, employer/withholding agent, ecommerce seller, etc.
- obligations: income tax, payroll/withholding, VAT/sales tax/GST, corporate tax prepayment, stamp tax, annual report, local taxes
- target period: month, quarter, year, or filing event
- local profile path, if one exists
- evidence directory or preferred record format

If the user says "check my taxes" and a workspace has a profile, read it first. Ask questions only for missing fields that block official verification.

## Deadline Check

1. Read local normal rules as hints.
2. Find the official annual calendar or current-period notice from the tax authority.
3. Check for weekend, holiday, disaster, regional, or portal outage extensions.
4. Compute days until deadline with `scripts/deadline_window.py` or equivalent manual math.
5. Apply the reminder policy from `SKILL.md` or the local profile.
6. Separate "verified current" from "local historical rule" in the final answer.

## Portal Check

Before opening or automating a portal:

- tell the user which app, QR code, account, or confirmation may be needed
- state that the agent will inspect/read and capture evidence only
- state that submit/pay/risk-confirm actions require a separate confirmation

Inspect:

- pending tasks / to-do list
- reminders / notices / messages
- risk alerts / doubts / warnings
- filing status by obligation and period
- payment status if visible without initiating payment
- recent filing records covering the target period
- exported forms or receipts when safe and useful

## Evidence

For each check, capture enough evidence for a user/accountant to continue:

- checked_at timestamp and timezone
- official source URL, page title, or notice identifier
- visible status text, not just a paraphrase
- screenshot/export path when available
- portal failures: blank page, slow bundle, failed request, timeout, or login blocker
- actions not taken because confirmation was missing

## Portal Failure Handling

Do not infer success from an unreachable portal.

When a portal stalls or goes blank:

1. Save a screenshot or HTML/network note if possible.
2. Retry with reload, a new tab, or a documented alternate official entry point.
3. Wait long enough for known slow portals when the user is actively trying to file.
4. If still blocked, report the exact blocker and next human action.
5. Keep "deadline verified" and "portal status verified" as separate conclusions.

## Completion Criteria

A tax check is complete only when the answer states:

- what was checked
- where it was checked
- what official source or portal showed
- which period/obligation the result covers
- what remains unverified or blocked
- what the user should do next, if anything
