#!/usr/bin/env python3
"""Validate the bounded, repository-local integrity controls for CMD-0001."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def require(text: str, needle: str, source: str) -> None:
    if needle not in text:
        raise AssertionError(f"{source} is missing required control: {needle}")


def main() -> None:
    candidate = read("candidates/CMD-0001-assumption-validation-register.md")
    wrapper = read("proving/CMD-0001-P4-typed-translation-wrapper.md")
    p6_test = read("proving/CMD-0001-P6-source-revision-coherence-test.md")
    p7_test = read("proving/CMD-0001-P7-counterevidence-quality-test.md")
    p7_score = read("proving/CMD-0001-P7-counterevidence-quality-score.md")
    p7_disposition = read("dispositions/CMD-0001-P7-defer.md")

    # A changed source must not inherit an earlier validation silently.
    for control in (
        "previous_source_revision",
        "validation_basis_revision",
        "source_revision_change",
        "validation_status: valid",
        "validation_basis_revision` equals `source_revision",
    ):
        require(candidate, control, "candidate register")
    require(p6_test, "P6-SOURCE-R1", "P6 test")
    require(p6_test, "P6-SOURCE-R2", "P6 test")
    require(
        p6_test,
        "none of the pre-P6 row rules rejects this",
        "P6 test",
    )

    # Counterevidence must be structured and unsupported alternatives remain leads.
    for control in (
        "explanation`, `basis`, `claim_posture`, and `residue_effect",
        "not_available` requires `residue_effect: lead_only",
        "ungraded string",
    ):
        require(wrapper, control, "P4 wrapper")
    for control in (
        "basis: not_available",
        "claim_posture: unresolved",
        "residue_effect: lead_only",
        "Generic alternatives remain visible",
    ):
        require(p7_score, control, "P7 score")
    require(p7_test, "generic, ungraded alternatives", "P7 test")

    # The bounded repair cannot be mistaken for a stronger disposition.
    for control in (
        "effectiveness",
        "destination acceptance",
        "transfer",
        "graduation",
        "deployment",
    ):
        require(p7_disposition, control, "P7 defer disposition")

    # P7 must remain visible wherever this repository presents current truth.
    for relative_path in ("STATUS.md", "ROADMAP.md", "LANE-STATE.yaml"):
        require(read(relative_path), "P7", relative_path)

    print("CMD-0001 integrity controls: PASS")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"CMD-0001 integrity controls: FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
