# China / Jiangsu Zero-Filing Pattern

This is a redacted pattern distilled from a real one-person-company workflow in Jiangsu, China. Use it only when the user's jurisdiction and obligations match. Do not copy private company names, taxpayer IDs, employee names, screenshots, or login state into a public output.

## Scope

Typical obligations in the source workflow:

- Monthly individual income tax withholding through the Natural Person E-Tax system.
- Quarterly VAT and surcharges, corporate income tax prepayment, financial statements, and stamp tax through the enterprise e-tax portal.
- Official deadline rules usually start from "day 15" but must be checked against the annual official notice and local adjustments.

## Official Entry Points

- Natural Person E-Tax: https://etax.chinatax.gov.cn/
- Natural Person withholding client path may exist at `/withholding/index.html`, but direct access can go blank or return `400`; prefer the homepage login then `单位办税`.
- Jiangsu Tax Bureau: https://jiangsu.chinatax.gov.cn/
- Jiangsu enterprise e-tax entry used in the source workflow: https://etax.jiangsu.chinatax.gov.cn:8443/loginb/

Always refresh these URLs from official sources if they fail.

## Monthly Individual Withholding Check

1. Open the Natural Person E-Tax homepage.
2. Ask the user to scan/login with the `个人所得税APP` or an authorized account.
3. Enter `单位办税`.
4. Go to `扣缴申报` -> `综合所得申报`.
5. Inspect the target period's declaration status.
6. If doing a zero-filing draft and the facts support zero income:
   - open `正常工资薪金所得`
   - add/select the existing verified employee
   - save a zero salary/income row
   - check `附表填写`
   - open `申报表报送` and capture the pre-submit summary
   - stop before final `报送` unless the user explicitly confirms
7. Capture success evidence only after the portal shows an official success/status page.

Common dialog meanings:

- `未填写专项附加扣除`: confirm only if the user says no relevant deductions are needed.
- `未填写三险一金`: continue only if the zero-filing facts support it.
- `是否确认报送`: final filing confirmation; do not click without explicit confirmation.

## Enterprise Portal Check

1. Open the Jiangsu enterprise e-tax official entry.
2. Ask the user to scan/login with `江苏税务APP` / `电子税务局APP` if prompted.
3. On the homepage, inspect:
   - `我的待办`
   - `本期应申报`
   - `待签收文书`
   - `风险疑点`
   - `其它`
   - `我的提醒` / `风险提示`
4. Treat any pending task, document to sign, risk prompt, or payment notice as an override that requires user attention even when the deadline window is quiet.

## Stamp Tax Zero-Filing Lesson

For the source workflow, the successful path was:

`我的待办` -> `财产和行为税税源采集及合并申报` -> `填写申报表` -> stamp-tax card -> `税源采集` -> `一键零申报`

The key lesson is procedural, not jurisdiction-universal:

- A zero-filing control may live inside a tax-source/detail page, not the outer combined filing page.
- `全选` + `提交申报` can fail if source collection has not been completed.
- Final submission still requires user confirmation.

## Reminder Rule From The Source Workflow

- More than 30 days before deadline: do not bother the user proactively.
- Within 7 days, due today, overdue, or any official portal task/risk notice: actively notify.
- Local history is never enough; check the official portal or official notice.

## Known Portal Failure Modes

- Natural Person direct withholding URL can show a blank page or `400`.
- Enterprise portal SPA bundles can stall on deadline days.
- SSO may send the browser to a national unified login page.

When this happens, capture the failure, retry via official entry points, and report the blocker. Do not claim "no tasks" from a blank portal.

## Optional Local Fast Lane

If a user's workspace contains a vetted script similar to `scripts/tax-filing/fast-lane.sh`, respect its stages:

- `status`: read-only portal state check.
- `prefill`: may save a draft and must stop before final submit.
- `submit`: requires a typed explicit confirmation phrase immediately before the final click.

Do not package private automation scripts in the public skill unless they contain no private data and have been reviewed for safety.
