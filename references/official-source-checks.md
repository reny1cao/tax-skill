# Official Source Checks

Use this reference whenever a conclusion depends on current law, deadlines, portal state, or official notices.

## Source Priority

Prefer sources in this order:

1. Official tax authority portal after login.
2. Official tax authority notices, calendars, FAQs, or help pages.
3. Official government gazettes or legal notices.
4. Accountant-provided documents or local records as supporting evidence only.
5. Third-party summaries only as search leads, never as the final source of truth.

## Verification Checklist

For each deadline or portal claim, record:

- source URL or portal name
- agency / issuing authority
- publication or effective date, if visible
- tax period and obligation
- exact deadline date or visible status
- whether a regional or holiday adjustment applies
- checked_at timestamp

If these cannot be verified, say what is missing.

## Deadline Pattern

1. Start from the user's local normal rule.
2. Search the official site for the current year and period.
3. Check regional/local adjustments separately.
4. Check whether the portal itself shows a reminder or task date.
5. Use the latest more-specific official source when sources conflict.
6. Do not rely on model memory for a current deadline.

## Portal Pattern

1. Open only official public entry points.
2. Remove session tokens from any record.
3. Tell the user which login app, QR code, MFA, or delegated authorization is needed.
4. After login, inspect to-do, reminders, risk notices, filing status, and recent filing records.
5. Save evidence before leaving a page when the status matters.

## Instability Pattern

Some tax portals are SPAs behind security checks and can return blank pages, stalled bundles, or 400/404 console errors.

- Capture screenshot/HTML/network notes when possible.
- Retry via reload, new tab, or another official entry point.
- Use a longer wait only when the user is actively present and the deadline is near.
- Never turn "portal failed to load" into "nothing is due."

## China Official Source Examples

Use these as examples, then refresh for the current year and region:

- Natural Person E-Tax portal: https://etax.chinatax.gov.cn/
- State Taxation Administration / local official tax bureau pages under `chinatax.gov.cn`
- Jiangsu Tax Bureau site: https://jiangsu.chinatax.gov.cn/
- Jiangsu E-Tax entry used in prior workflow: https://etax.jiangsu.chinatax.gov.cn:8443/loginb/

As of 2026-06-16, official tax-bureau pages for `税总办征科函〔2025〕64号` state that China's June 2026 filing period ended on 2026-06-15. Treat this as a historical example; check the current official notice before future use.
