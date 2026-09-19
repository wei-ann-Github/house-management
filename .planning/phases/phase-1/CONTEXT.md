# CONTEXT: Phase 1

## Project summary
See: .planning/PROJECT.md — new-house-management
Core value: Make moving and home setup predictable and low-friction by centralizing inventory, budget, vendor tracking, and timeline management.

## Relevant requirements
- INV-01, INV-02, INV-03 — Inventory capture, tagging, CSV export
- BUD-01, BUD-02, BUD-03 — Budget items, summary, paid flags
- TIM-01, TIM-02, TIM-03 — Timeline, reminders, milestone tracking

## Constraints
- MVP uses local storage (JSON or SQLite) to avoid infra complexity
- Photos stored as paths; no image processing in Phase 1
- Python-first implementation

## Acceptance criteria (short)
- Add 10 items, record costs, create milestones, export inventory CSV
- CLI commands available in README for quick verification

---
*Context captured: 2026-09-19*