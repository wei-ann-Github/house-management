# VERIFICATION: Phase 1 — Acceptance & Tests

## Tracer acceptance
- [ ] Able to run tracer script that:
  - adds 10 distinct inventory items
  - adds at least one cost linked to an item
  - creates at least one milestone with a due date
  - exports inventory as CSV containing the added items

## Automated tests
- Unit tests for storage layer (CRUD for items, costs, milestones)
- Test for CSV export format and content

## Manual checks
- [ ] Quickstart README reproduces the tracer steps
- [ ] Timeline displays upcoming milestones (CLI listing or simple web view)

## Exit criteria
- All tracer acceptance checks pass
- CI runs unit tests and they succeed

---
*Verification defined: 2026-09-19*