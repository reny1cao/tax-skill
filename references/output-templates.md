# Output Templates

Use concise reports. Separate verified facts from blockers and assumptions.

## Tax Check Result

```markdown
## Tax Check Result

- checked_at:
- jurisdiction:
- entity:
- target_period:
- obligations_checked:
- deadline:
- deadline_source:
- official_portals_checked:
- status:
- evidence:
- blockers:
- next_actions:
```

## Tax Health Check Report

```markdown
## 税务状态体检报告 / Tax Health Check Report

- checked_at:
- jurisdiction:
- entity_type:
- target_period:
- profile_used:

### 1. Scope

- obligations_expected_from_profile:
- official_obligation_source_checked:
- portals_checked:
- portals_not_checked:

### 2. Deadline Window

| obligation | period | official_deadline | days_left | window | source |
|---|---|---:|---:|---|---|

### 3. Official Portal Status

| portal | checked_items | visible_status | evidence | confidence |
|---|---|---|---|---|

### 4. Findings

- pending_tasks:
- risk_notices:
- unsigned_documents:
- unfiled_or_overdue_items:
- payment_or_refund_items:

### 5. Evidence

- official_deadline_sources:
- screenshots_or_exports:
- visible_status_text:
- checked_by:

### 6. Blockers

- login_or_permission_blockers:
- portal_load_failures:
- items_requiring_accountant_or_user_confirmation:

### 7. Next Actions

- owner:
- accountant_questions:
- next_check_date:
- do_not_do_without_confirmation:
```

## Deadline Window

```markdown
## Deadline Window

- obligation:
- period:
- official_deadline:
- days_until_deadline:
- window: quiet | upcoming | urgent | due_today | overdue
- notify_user: yes/no
- source:
```

## Portal Handoff

```markdown
I opened the official portal: [portal name]

Please use [app/account] to complete [QR/MFA/login confirmation].
I will inspect [pending tasks/reminders/risk notices/filing status] only.
I will not submit, pay, amend, acknowledge, or change account data without a separate confirmation.
```

## Blocked Portal

```markdown
I could not verify the portal status yet.

- portal:
- attempted_entry_points:
- observed_failure:
- evidence:
- deadline_status:
- next_human_action:
```

## Accountant Handoff

```markdown
## Accountant Handoff

- question:
- jurisdiction / entity:
- period:
- official sources checked:
- portal evidence:
- local records:
- unresolved decision:
- deadline:
```

## Final Answer Shape

For ordinary user-facing replies:

1. Start with the result in one sentence.
2. List only the obligations that matter.
3. Mention evidence and blockers.
4. Give the next action with an exact date if time-sensitive.
5. Avoid long legal explanations unless the user asks.
