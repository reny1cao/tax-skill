# Tax Health Check

Use this reference to run a professional, source-backed tax status check for a small business or one-person company. The goal is not to file taxes. The goal is to answer: "Do we have any missed obligations, pending tasks, risk notices, overdue filings, or accountant follow-ups?"

## Research Discipline

- Start from official sources and the user's current portal state, not assumptions.
- Treat a local profile as a routing map, not proof.
- Treat accountant statements as useful context, not portal verification.
- Never generalize a verified zero-filing path into a rule for non-zero filings or other jurisdictions.
- Distinguish obligation existence, deadline, filing status, payment status, and risk/document status.
- If the portal cannot be checked, report "unverified" or "blocked"; do not infer "nothing due."

## Health Check Questions

Answer these seven questions in order:

1. What entity and jurisdiction are being checked?
2. Which tax/fee types and reports are officially expected for this entity?
3. What is the current official deadline window for each expected obligation?
4. Does the official portal show pending tasks, unfiled items, risk notices, unsigned documents, or payments?
5. Do filing records show the target period was actually filed or reported?
6. What evidence supports each conclusion?
7. What still requires user/accountant confirmation?

## Professional Knowledge Map

For a China small company, do not begin with a generic checklist. First establish the entity's actual obligation map from the official portal:

- Tax/fee type determination: query existing `税费种认定信息` or equivalent taxpayer information.
- Expected filings: check `应申报税费种信息`, `本期应申报`, `未申报查询`, or equivalent portal views.
- Filing records: check `申报信息查询`, target-period filing status, and visible receipt/status text.
- Financial reports: check whether financial statements are expected for the quarter/year.
- Portal notices: check pending tasks, reminders, risk notices, unsigned documents, correction notices, and payment notices.

Use local normal rules only after this obligation map is anchored.

## China Small-Company Baseline

The following is a baseline for China workflows and must be refreshed for the user's region, taxpayer type, and official portal.

| Area | What to verify | Official basis to refresh |
|---|---|---|
| Individual income tax withholding | Whether the entity is a withholding agent; monthly filing/payment deadline; target-period withholding declaration status | Individual income tax withholding rules and Natural Person E-Tax portal |
| VAT and surcharges | Whether the taxpayer is monthly or quarterly; whether small-scale taxpayer status applies; target-period VAT/surcharge filing status | Tax/fee type determination plus VAT filing rules |
| Corporate income tax prepayment | Monthly/quarterly prepayment period and filing status for resident enterprise / applicable collection method | Enterprise income tax prepayment rules and portal expected filings |
| Stamp tax | Whether stamp tax is determined as periodic or per-transaction; whether tax-source collection is required before filing | Stamp tax law/implementation rules and local determination |
| Financial statements | Whether quarterly and/or annual financial reports are expected; status of target-period submission | Financial accounting report submission rules and portal prompts |
| Annual filings | Enterprise income tax annual return, financial annual report, or other annual obligations | Official annual rules and portal expected filings |
| Portal notices | Pending tasks, reminders, risk notices, unsigned documents, correction notices, payment notices | Current official portal state |

## Official Sources To Check

Use these as source categories, not permanent truth:

- Annual filing-deadline notices from the State Taxation Administration or local tax bureau, such as `税总办征科函〔2025〕64号` for 2026 filing periods.
- Tax/fee type determination pages in the official e-tax portal.
- `本期应申报`, `未申报查询`, and `申报信息查询` or equivalent official portal views.
- Natural Person E-Tax portal for individual income tax withholding status.
- Enterprise e-tax portal for company tax filings, financial statements, pending tasks, risk notices, and document delivery.
- Official hot questions / operation guides from provincial or municipal tax bureaus when they document portal paths.

## Current Source-Backed Checks

These checks are grounded in official-source patterns and should be reverified live:

- Filing deadlines: annual official notices define current monthly/quarterly filing periods; do not rely on a generic "15th" rule without checking holidays and local adjustments.
- VAT: for taxpayers using a one-month or one-quarter period, filing/payment is generally within 15 days after period end; small-scale taxpayers may be monthly or quarterly, and the portal/tax determination decides the actual cadence.
- Individual withholding: withholding agents generally file/pay by the 15th day of the following month and submit withholding declarations.
- Corporate income tax prepayment: resident enterprises using monthly/quarterly prepayment generally file within 15 days after month/quarter end; annual return is generally within five months after year end.
- Stamp tax: periodic or per-transaction status depends on tax-source determination; tax-source collection can be a precondition for filing.
- Financial statements: many portal workflows expect quarterly and annual financial reports; portal prompts and registered accounting-system information determine the actual report set.
- Unsigned documents and risk notices are not "just messages"; record them and hand off before signing, acknowledging, dismissing, or marking handled.

## Portal Checklist

Run only read-only checks unless the user explicitly authorizes more.

### Enterprise E-Tax Portal

- taxpayer identity / entity selected
- taxpayer status and tax/fee type determination
- `本期应申报` / expected current filings
- `未申报查询` / unfiled items
- `申报信息查询` / submitted filings for target period
- financial statement submission status
- `我的待办`
- reminders / messages / risk prompts
- `待签收文书` / electronic document delivery
- payment/refund notices visible without initiating payment

### Natural Person E-Tax / Withholding

- correct withholding entity selected
- target period selected
- comprehensive income / wage-salary withholding status
- visible declaration status, totals, and person-count summary
- submitted declaration record / receipt if available
- dialogs about deductions, social insurance, final submission, or corrections

## Evidence Standards

For each conclusion, collect at least one evidence handle:

- portal name and public entry URL
- checked_at timestamp and timezone
- visible status text
- target period and obligation
- screenshot/export path if available
- official notice URL for deadline conclusions
- blocker evidence if status could not be verified

The final report must separate:

- verified facts
- local assumptions
- portal blockers
- accountant/user decisions

## Accountant Handoff

When a question requires professional judgment, create a concrete handoff instead of guessing:

- "Portal shows [notice title/status] for [period]. Does this require signing or correction?"
- "Filing record for [obligation/period] was not found in [portal path]. Did the accountant file through another channel?"
- "Tax/fee type determination shows [obligation]. Should this entity remain on this cadence?"
- "This appears to be a non-zero filing or payment situation. Please confirm treatment before any submission."

## Hard Stops

Stop before:

- final filing submission
- payment, withholding, refund, bank, or tripartite agreement actions
- correcting, voiding, importing, uploading, or deleting declarations
- signing/acknowledging/dismissing risk notices or tax documents
- changing taxpayer, employee, bank, invoice, authorization, or account data

## Source Links

Refresh these when using the workflow:

- 2026 annual filing deadline notice example: https://beijing.chinatax.gov.cn/bjswj/c104846/202512/eae656e3c28c4aff82de98093c977f00.shtml
- VAT small-scale filing guide example: https://shanghai.chinatax.gov.cn/bsfw/bszn/znnssb/201911/t448970.html
- Individual withholding filing rule example: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html
- Corporate income tax filing guide example: https://guangdong.chinatax.gov.cn/gdsw/fssw_nsrxt_kjxz/2025-10/09/content_145b9db929fb4054bcca80d26ab8a3ee.shtml
- Stamp tax tax-source and zero-filing FAQ example: https://guangdong.chinatax.gov.cn/gdsw/zssw_rdwd/2021-07/14/content_42528abc02d9437685d59683a362de31.shtml
- Stamp tax period rule example: https://fgk.chinatax.gov.cn/zcfgk/c100012/c5196761/content.html
- Tax/fee type determination query example: https://shanghai.chinatax.gov.cn/zcfw/rdwd/202412/t474471.html
- Filing info query example: https://tianjin.chinatax.gov.cn/nsrxt/11200000000/0500/050011/20241202145745551.shtml
- Unfiled / overdue query example: https://beijing.chinatax.gov.cn/bjswj/c106602/202410/bc3d37e1ee3c49d7942f4b8a5032fe75.shtml
- Pending tasks for overdue filing / penalties example: https://guangdong.chinatax.gov.cn/gdsw/yjsw_xzfw/2020-06/24/content_c2f7a05676504f77bf55bae463b579db.shtml
- Document delivery / unsigned document example: https://jiangsu.chinatax.gov.cn/art/2024/9/23/art_8353_472998.html
- Financial statement submission guide example: https://shanghai.chinatax.gov.cn/jstax/ztzl/yshj/sycz/202512/t478541.html
