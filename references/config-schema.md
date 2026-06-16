# Local Tax Profile Schema

Use a private local profile for entity-specific facts. Do not store real taxpayer identifiers inside the public skill.

Recommended paths:

- `docs/private/tax-profile.local.md`
- `docs/domains/tax-filing/profile.local.md`
- `.tax/tax-profile.local.md`

## Minimum Profile

```markdown
# Tax Profile

## Entity

- legal_name:
- public_alias:
- entity_type:
- taxpayer_type:
- jurisdiction:
- tax_authority:
- accountant_or_owner_contact:

## Systems

| purpose | official_url | login_method | required_app | notes |
|---|---|---|---|---|
| individual-withholding | | qr-code | | |
| company-tax | | qr-code | | |
| sales-vat-gst | | password/mfa | | |

## Filing Calendar

| obligation | cadence | normal_deadline_rule | official_deadline_source | portal_purpose |
|---|---|---|---|---|
| payroll or individual withholding | monthly | day 15 | | individual-withholding |
| VAT / sales tax / GST | quarterly | day 15 after quarter | | company-tax |
| corporate income tax prepayment | quarterly | day 15 after quarter | | company-tax |

## Reminder Policy

- quiet_if_more_than_days: 30
- active_reminder_within_days: 7
- official_portal_task_always_alerts: true

## Local Records

| period | obligation | local_status | checked_at | source | evidence |
|---|---|---|---|---|---|

## Evidence

- screenshots:
- exports:
- run_logs:
- redaction_required: true
```

## Field Guidance

- `legal_name` and taxpayer IDs are private; keep them in local profiles, not in shareable skill files.
- `official_url` must be a public entry point, not a session URL with tokens.
- `official_deadline_source` should point to the tax authority calendar, annual notice, or official current-period announcement.
- `local_status` is not proof. It tells the agent where to look next.
- `evidence` should be a path, receipt id, or official confirmation number when available.

## Missing Profile

If no profile exists, ask only for the next blocking field. For example:

- "Which jurisdiction and entity type should I check?"
- "Which obligations matter this period?"
- "Do you have an official portal URL or should I search the tax authority site?"

For deadline-only questions, jurisdiction + obligation + period may be enough.
