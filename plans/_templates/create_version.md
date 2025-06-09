# Create New Version Checklist

## 1. Preparation
- [ ] Run `Execute do_plan.md` with the AI assistant
- [ ] Create directory `plans/Versions/VX.Y.Z/`
- [ ] Copy this file into the new directory
- [ ] Initialize `VERSION_PLAN.md` and `TECH_SPEC.md`
- [ ] Ensure ROADMAP.md status is set to "In Planning"

## 2. Slide Style Compliance
- [ ] Organize content using MECE and Pyramid Principle
- [ ] Apply color palette and typography from `content/Style.md`
- [ ] Maintain alignment and whitespace
- [ ] Attribute all data sources

## 3. Slide Architecture Awareness
- [ ] Edit slides directly in `index.html`
- [ ] Use `scrollToSlide()` for navigation IDs
- [ ] Avoid editing the slide array in `script.js`

## 4. Phase Workflow

### 4.1 Phase 1: Comprehensive Planning & Design
- [ ] Extract version details from `ROADMAP.md`
- [ ] Validate version number and required fields
- [ ] Fill in default values when missing
- [ ] Set up standard files with initial checkboxes
- [ ] Document Code Impact Analysis in `TECH_SPEC.md`

### 4.2 Phase 2: Development Kickoff
- [ ] Review milestones and targets
- [ ] Populate `VERSION_PLAN.md` and `TECH_SPEC.md`
- [ ] Verify dependencies and resources
- [ ] Record Phase 1 learnings in `learn.log`
- [ ] Update status checkboxes

### 4.3 Phase 3: Iterative Feature Development & Implementation
- [ ] Detail technical design for each feature
- [ ] Implement code changes in HTML/CSS/JS
- [ ] Perform developer testing
- [ ] Commit frequently using `feat(scope): description`
- [ ] Mark feature progress in `VERSION_PLAN.md`
- [ ] Log key learnings in `learn.log`

### 4.4 Phase 4: Holistic Review, Testing, Documentation & Finalization
- [ ] Run automated code checks and peer review
- [ ] Conduct integration, UI and accessibility testing
- [ ] Update `VERSION_PLAN.md`, `CHANGELOG.md` and other docs
- [ ] Perform final sanity check and update `ROADMAP.md`
- [ ] Commit with `docs:` or `chore:` message
- [ ] Summarize final learnings

## 5. Final Reminders
- [ ] Keep this checklist in sync with project standards
- [ ] Update version number and last updated date

*Last Updated: 2025-06-03*
