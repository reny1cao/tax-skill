# Safety Boundaries

Tax operations are high-stakes. Keep the user in control.

## Allowed Without Extra Confirmation

These are normally safe after the user asks for a check:

- read local profiles and records
- search official public sources
- open official portal entry points
- wait for user login / QR / MFA
- inspect visible statuses
- compute deadline windows
- capture screenshots or exports when no private data is being shared publicly
- summarize findings and blockers

## Confirm Scope First

Ask before:

- downloading official filings, receipts, or notices that contain sensitive data
- filling draft forms or zero-filing drafts
- adding an employee/income line even if it is zero
- changing filters or query periods that may affect what evidence is shown
- running browser automation that can click through a live portal

## Explicit Confirmation Required

Require explicit user confirmation immediately before:

- final filing submission
- tax payment, refund, withholding, bank, or deduction action
- return amendment, cancellation, deletion, import, or upload
- acknowledging, dismissing, signing, or marking any risk notice/document as handled
- changing taxpayer, employee, bank, invoice, contact, authorization, or account data
- accepting a legal interpretation or deadline from a non-official source when official sources cannot be checked

Good confirmation prompt:

```text
I am about to click final submit in [portal] for [obligation] covering [period].
Visible totals are [summary]. This may create an official filing record.
Reply with the exact phrase "[confirmation phrase]" if you want me to proceed.
```

## Refuse Or Redirect

Do not help with:

- evasion, concealment, false filings, or fabricated evidence
- bypassing login, MFA, CAPTCHA, portal controls, or app confirmations
- tax planning presented as a way to hide income or avoid lawful obligations
- definitive tax/legal/accounting advice where a professional judgment is needed

Offer to collect facts, find official guidance, draft accountant questions, or prepare an evidence bundle instead.

## Privacy

- Do not include taxpayer IDs, ID numbers, bank accounts, employee names, QR codes, session URLs, or screenshots in a public/shareable result unless explicitly requested and already present in the workspace.
- Use placeholders such as `TAX_ID_REDACTED`, `Employee A`, and `Example Trading LLC`.
- Keep raw evidence in a local/private evidence directory.
- For videos, demos, or public posts, use mock pages or redacted screenshots.
