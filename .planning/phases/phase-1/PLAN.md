# PLAN: Phase 1 — MVP: Inventory, Budget, Timeline

**Phase:** 1
**Goal:** Allow users to capture household inventory, record costs, and create a move timeline with exportable checklists.
**Estimated duration:** 2 weeks

## Overview
Tracer-first decomposition: deliver a small end-to-end vertical slice (tracer) that lets a user add items, record a cost, create a timeline milestone, and export inventory as CSV. Verify the tracer before expanding into parallel feature tasks.

## Tracer (end-to-end) — priority 1
- Task T1 (tracer): Minimal CLI/web endpoints
  - Implement a simple Python-backed storage (local JSON or SQLite) with commands:
    - add-item (photo optional path, name, dimensions, category)
    - add-cost (description, amount, category, linked item optional)
    - add-milestone (title, due_date)
    - export-inventory (CSV)
  - Acceptance: Add 10 items, add a cost, create a milestone, and export inventory CSV that contains the 10 items.
  - Estimated: 2–3 days

## Feature tasks (after tracer verified)
- Task T2: Inventory UX/CLI
  - Implement fields, tagging (keep/donate/sell/discard), CSV export, and basic validation.
  - Estimated: 3 days

- Task T3: Budget handling
  - Add estimated/actual cost fields, paid/unpaid flags, budget summary by category.
  - Estimated: 2 days

- Task T4: Timeline editor & reminders
  - Create milestones, mark complete, export checklist; simple local reminders/exportable schedule.
  - Estimated: 3 days

- Task T5: Link vendors (light integration)
  - Allow linking vendor contact notes to budget or inventory items (skeleton for Phase 2).
  - Estimated: 1 day (spike)

- Task T6: Tests & verification
  - Unit tests for storage and export, end-to-end tracer test (scripted CLI run), manual acceptance checklist.
  - Estimated: 2 days

- Task T7: Docs & release
  - README updates showing quickstart and how to run tracer, export CSV.
  - Estimated: 1 day

## Risks & Checkpoints
- Risk: Photo handling increases storage complexity — tracer uses photo path only.
- Checkpoint: After tracer passes verification, split remaining tasks into parallel workstreams.

## Deliverables
- Working tracer: add-item, add-cost, add-milestone, export-inventory
- Tests: tracer end-to-end script and unit tests for storage/export
- Documentation: quickstart README and usage examples

---
*Plan created: 2026-09-19*