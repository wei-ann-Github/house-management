# new-house-management

## What This Is

To manage the little things associated with moving a house — tracking renovation costs, buying furniture and fixtures, coordinating moves between properties, and keeping a timeline and task list so nothing is lost in transit.

## Core Value

Make moving and home setup predictable and low-friction by centralizing inventory, budget, vendor tracking, and timeline management so decisions and costs are visible.

## Business Context

- **Customer**: Homeowners and small moving teams
- **Revenue model**: (internal / N/A) — primarily a productivity tool for personal projects
- **Success metric**: Percentage of moves completed on-time and within planned budget

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] INV-01: Capture household inventory (photos, dimensions, category)
- [ ] BUD-01: Record and estimate renovation and purchase costs; simple budget summary
- [ ] TIM-01: Create and visualize a move timeline with milestones and reminders
- [ ] VEND-01: Track vendors and purchase orders (furniture, movers, contractors)

### Out of Scope

- Full-service move booking and payment processing — the tool coordinates, not transacts
- Real-time chat with vendors — communications via recorded notes and links

## Context

- Primary stack: Python (backend scripts / CLI / small web UI)
- User needs: simple, low-effort capture during a busy move window; offline-capable notes
- Known friction: unpredictable vendor lead times, mismatched furniture sizes

## Constraints

- **Timeline**: Target delivery for initial MVP by 2026-12-08
- **Tech**: Python-first; avoid heavy infra for MVP

## Key Decisions

| Decision | Rationale | Outcome |
|---|---|---|
| Python-first CLI/web tool | Fast iteration and scripting for inventory capture | — Pending |

---
*Last updated: 2026-09-19 after initial project creation*
