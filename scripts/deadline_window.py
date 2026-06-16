#!/usr/bin/env python3
"""Classify tax deadlines into reminder windows.

This helper performs date arithmetic only. It does not verify laws, portal
state, extensions, or whether a filing is actually required.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys


def parse_date(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid ISO date: {value}") from exc


def parse_deadline(value: str) -> tuple[str, dt.date]:
    if "=" in value:
        label, raw_date = value.split("=", 1)
        label = label.strip() or raw_date.strip()
    else:
        label = value.strip()
        raw_date = value
    return label, parse_date(raw_date.strip())


def classify(days: int, urgent_days: int, quiet_days: int, notify_upcoming: bool) -> tuple[str, bool]:
    if days < 0:
        return "overdue", True
    if days == 0:
        return "due_today", True
    if days <= urgent_days:
        return "urgent", True
    if days <= quiet_days:
        return "upcoming", notify_upcoming
    return "quiet", False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--today",
        type=parse_date,
        default=dt.date.today(),
        help="Today's date in YYYY-MM-DD format. Defaults to local today.",
    )
    parser.add_argument(
        "--deadline",
        action="append",
        required=True,
        help="Deadline as YYYY-MM-DD or label=YYYY-MM-DD. Repeatable.",
    )
    parser.add_argument(
        "--urgent-days",
        type=int,
        default=7,
        help="Notify when the deadline is this many days away or closer. Default: 7.",
    )
    parser.add_argument(
        "--quiet-days",
        type=int,
        default=30,
        help="Deadlines beyond this many days are quiet. Default: 30.",
    )
    parser.add_argument(
        "--notify-upcoming",
        action="store_true",
        help="Set notify=true for deadlines between urgent-days and quiet-days.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output.",
    )
    args = parser.parse_args()

    if args.urgent_days < 0 or args.quiet_days < 0:
        parser.error("--urgent-days and --quiet-days must be non-negative")
    if args.urgent_days > args.quiet_days:
        parser.error("--urgent-days cannot be greater than --quiet-days")

    results = []
    for item in args.deadline:
        label, deadline = parse_deadline(item)
        days = (deadline - args.today).days
        window, notify = classify(days, args.urgent_days, args.quiet_days, args.notify_upcoming)
        results.append(
            {
                "label": label,
                "today": args.today.isoformat(),
                "deadline": deadline.isoformat(),
                "days_until_deadline": days,
                "window": window,
                "notify": notify,
            }
        )

    payload = {"deadlines": results}
    indent = 2 if args.pretty else None
    print(json.dumps(payload, ensure_ascii=False, indent=indent))
    return 0


if __name__ == "__main__":
    sys.exit(main())
