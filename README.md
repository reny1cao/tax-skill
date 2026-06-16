# Tax Skill

[中文](#中文) | [English](#english)

---

## 中文

`tax-skill` 是一个给 Codex 使用的税务运营检查 skill。它帮助一人公司、小微企业、独立开发者、跨境电商卖家检查税务 deadline、官方门户待办、风险提醒和证据记录。

它不是自动报税工具，也不是税务建议工具。它的边界是：查官方来源、引导登录、读取状态、整理证据、在高风险动作前停下来。

### 适合做什么

- 检查这个月或这个季度有没有税务待办
- 核对官方申报 deadline 和节假日顺延
- 打开官方税务门户并提示用户扫码或 MFA
- 查看待办、提醒、风险提示、申报状态和最近申报记录
- 生成可给自己或会计看的检查报告
- 搭建每月/每季度税务检查 workflow

### 不做什么

- 不提供税务、法律或会计建议
- 不判断收入、成本、抵扣、避税或税务筹划
- 不绕过登录、二维码、MFA、验证码或门户控制
- 不自动提交申报、缴款、修改资料、确认风险事项
- 不在公开输出里暴露税号、身份证号、银行账户、员工姓名、二维码或 session URL

### 安装

把 repo clone 到 Codex skills 目录：

```bash
git clone https://github.com/reny1cao/tax-skill.git "${CODEX_HOME:-$HOME/.codex}/skills/tax-skill"
```

如果已经安装过：

```bash
git -C "${CODEX_HOME:-$HOME/.codex}/skills/tax-skill" pull
```

### 使用

在 Codex 里直接调用：

```text
Use $tax-skill to check whether my small business has any tax tasks this month.
```

也可以用中文：

```text
用 $tax-skill 帮我检查这个月公司税务有没有待办或风险提醒。
```

### 推荐私有配置

公开 skill 不应该包含真实公司、税号、员工、登录态或截图。把这些放在自己的工作区，例如：

```text
docs/private/tax-profile.local.md
```

最小配置可以参考：

```markdown
# Tax Profile

## Entity

- legal_name:
- entity_type:
- jurisdiction:
- tax_authority:

## Systems

| purpose | official_url | login_method | required_app | notes |
|---|---|---|---|---|
| individual-withholding | | qr-code | | |
| company-tax | | qr-code | | |

## Filing Calendar

| obligation | cadence | normal_deadline_rule | official_deadline_source |
|---|---|---|---|
| payroll withholding | monthly | day 15 | |
| VAT / sales tax / GST | quarterly | day 15 after quarter | |

## Evidence

- screenshots:
- exports:
- run_logs:
```

完整 schema 见 [`references/config-schema.md`](references/config-schema.md)。

### Deadline helper

这个 repo 带一个只做日期窗口判断的小脚本。它不查法规、不查门户、不判断是否必须申报。

```bash
python3 scripts/deadline_window.py \
  --today 2026-06-16 \
  --deadline "monthly withholding=2026-07-15" \
  --deadline "late filing=2026-06-15" \
  --pretty
```

输出会把 deadline 分为：

- `quiet`: 离 deadline 超过 30 天
- `upcoming`: 8 到 30 天
- `urgent`: 7 天内
- `due_today`: 今天截止
- `overdue`: 已逾期

### 安全边界

以下动作必须停下来等用户明确确认：

- 最终提交申报
- 缴税、扣款、退款或银行支付动作
- 修改、删除、导入、上传申报数据
- 确认、忽略、签收或标记风险提醒/文书
- 修改纳税人、员工、银行、发票、授权或账户信息

安全规则见 [`references/safety-boundaries.md`](references/safety-boundaries.md)。

### 目录结构

```text
tax-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── workflow.md
│   ├── config-schema.md
│   ├── official-source-checks.md
│   ├── safety-boundaries.md
│   ├── output-templates.md
│   └── china-jiangsu-zero-filing.md
└── scripts/
    └── deadline_window.py
```

### 参考文档

- [`SKILL.md`](SKILL.md): skill 入口和核心协议
- [`references/workflow.md`](references/workflow.md): 完整检查流程
- [`references/official-source-checks.md`](references/official-source-checks.md): 官方来源和门户校验规则
- [`references/output-templates.md`](references/output-templates.md): 检查报告模板
- [`references/china-jiangsu-zero-filing.md`](references/china-jiangsu-zero-filing.md): 中国/江苏零申报流程案例，已脱敏

[Back to top](#tax-skill)

---

## English

`tax-skill` is a Codex skill for tax operations checks. It helps one-person companies, small businesses, indie builders, contractors, and ecommerce sellers check filing deadlines, official portal tasks, risk notices, and evidence records.

It is not an auto-filing tool and it does not provide tax advice. Its job is to verify official sources, guide login handoffs, inspect status, collect evidence, and stop before high-risk actions.

### What It Helps With

- Check whether this month or quarter has tax tasks
- Verify official filing deadlines and holiday extensions
- Open official tax portals and guide QR/MFA handoff
- Inspect pending tasks, reminders, risk notices, filing status, and recent records
- Produce an audit-style report for the user or accountant
- Set up a repeatable monthly or quarterly tax-check workflow

### What It Does Not Do

- It does not provide tax, legal, or accounting advice
- It does not decide income classification, deductibility, avoidance, or tax planning
- It does not bypass login, QR codes, MFA, CAPTCHA, or portal controls
- It does not automatically submit filings, make payments, change data, or acknowledge risk notices
- It does not expose taxpayer IDs, identity numbers, bank accounts, employee names, QR codes, or session URLs in public outputs

### Install

Clone the repo into your Codex skills directory:

```bash
git clone https://github.com/reny1cao/tax-skill.git "${CODEX_HOME:-$HOME/.codex}/skills/tax-skill"
```

If already installed:

```bash
git -C "${CODEX_HOME:-$HOME/.codex}/skills/tax-skill" pull
```

### Usage

Call it from Codex:

```text
Use $tax-skill to check whether my small business has any tax tasks this month.
```

Chinese works too:

```text
用 $tax-skill 帮我检查这个月公司税务有没有待办或风险提醒。
```

### Recommended Private Profile

The public skill should not contain real company names, taxpayer IDs, employee names, login state, or screenshots. Keep those in your own workspace, for example:

```text
docs/private/tax-profile.local.md
```

Minimum profile example:

```markdown
# Tax Profile

## Entity

- legal_name:
- entity_type:
- jurisdiction:
- tax_authority:

## Systems

| purpose | official_url | login_method | required_app | notes |
|---|---|---|---|---|
| individual-withholding | | qr-code | | |
| company-tax | | qr-code | | |

## Filing Calendar

| obligation | cadence | normal_deadline_rule | official_deadline_source |
|---|---|---|---|
| payroll withholding | monthly | day 15 | |
| VAT / sales tax / GST | quarterly | day 15 after quarter | |

## Evidence

- screenshots:
- exports:
- run_logs:
```

See the full schema in [`references/config-schema.md`](references/config-schema.md).

### Deadline Helper

This repo includes a small date-window helper. It does not verify laws, portal state, or whether a filing is required.

```bash
python3 scripts/deadline_window.py \
  --today 2026-06-16 \
  --deadline "monthly withholding=2026-07-15" \
  --deadline "late filing=2026-06-15" \
  --pretty
```

It classifies deadlines as:

- `quiet`: more than 30 days away
- `upcoming`: 8 to 30 days away
- `urgent`: within 7 days
- `due_today`: due today
- `overdue`: already past due

### Safety Boundaries

The agent must stop and wait for explicit user confirmation before:

- final filing submission
- tax payment, deduction, refund, or bank/payment actions
- modifying, deleting, importing, or uploading filing data
- acknowledging, dismissing, signing, or marking risk notices/documents as handled
- changing taxpayer, employee, bank, invoice, authorization, or account information

See [`references/safety-boundaries.md`](references/safety-boundaries.md).

### Repository Structure

```text
tax-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── workflow.md
│   ├── config-schema.md
│   ├── official-source-checks.md
│   ├── safety-boundaries.md
│   ├── output-templates.md
│   └── china-jiangsu-zero-filing.md
└── scripts/
    └── deadline_window.py
```

### References

- [`SKILL.md`](SKILL.md): skill entrypoint and core protocol
- [`references/workflow.md`](references/workflow.md): full check workflow
- [`references/official-source-checks.md`](references/official-source-checks.md): official-source and portal verification rules
- [`references/output-templates.md`](references/output-templates.md): report templates
- [`references/china-jiangsu-zero-filing.md`](references/china-jiangsu-zero-filing.md): redacted China/Jiangsu zero-filing case pattern

[Back to top](#tax-skill)
