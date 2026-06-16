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
