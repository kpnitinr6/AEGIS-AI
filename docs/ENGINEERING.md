# AEGIS AI Engineering Handbook

## Philosophy

Build software that is:

- Reliable
- Understandable
- Testable
- Maintainable
- Scalable

---

## Development Principles

1. Quality over speed.
2. Understand before implementing.
3. One responsibility per module.
4. Every feature must be testable.
5. Every milestone ends with a Git commit.
6. Documentation is part of the product.
7. Never duplicate information (DRY).
8. Prefer readability over cleverness.
9. Refactor instead of patching.
10. Build software we would trust with our own trades.

---

## Git Workflow

Every completed milestone:

git add .
git commit -m "<version> - <description>"

---

## Coding Standards

- Use Python 3.13
- Follow PEP 8
- Keep functions small
- Add type hints
- Write meaningful names
- Avoid magic numbers

## The Commander Rule

Architecture discussions are encouraged.

Complete file contents are mandatory.

If Aris forgets the files, the Commander is authorized to interrupt immediately by asking:

"Content?"

## Types of Aris Sprints

### Implementation Sprint

Objective:
Deliver a working feature.

Deliverables:
- Complete implementation
- Automated tests
- Green test suite
- Commit

### Architecture Sprint

Objective:
Reduce future complexity.

Deliverables:
- Design review
- ADR or documentation update
- Architectural decision
- Implementation plan

Architecture sprints are considered complete even if no production code is written.
