# AI Version Planning Assistant

## How to Use
1. [ ] Run: `Execute do_plan.md`
2. [ ] After completing any task, change its checkbox to `[x]` so progress is updated at every step

## Pre-Execution Validation
1. [ ] **Check Prerequisites**
   - [ ] Verify `plans/_reference/ROADMAP.md` exists and is accessible
   - [ ] Check for required permissions

2. [ ] **Environment Setup**
   - [ ] Create required directories if they don't exist
   - [ ] Verify write permissions
   - [ ] Initialize any required services or connections

## Execution Instructions for AI

1. [ ] **Review Roadmap**
   - [ ] Check `plans/_reference/ROADMAP.md` for the next planned version and its details
   - [ ] Verify the target date and key deliverables

2. [ ] **Setup Version Directory**
   - [ ] Create a new directory: `plans/Versions/VX.Y.Z/` (using semantic versioning)
   - [ ] Create standard files in the new directory:
     - [ ] `VERSION_PLAN.md`: Version overview, goals, and high-level design
     - [ ] `TECH_SPEC.md`: Technical specifications and architecture
   - [ ] Copy templates:
     - [ ] Use `plans/_templates/create_version.md` as the initial content for `VERSION_PLAN.md`

3. [ ] **Initialize Version Planning**
   - [ ] Populate `VERSION_PLAN.md` with version details from `plans/_reference/ROADMAP.md`
   - [ ] Validate all required information is available
   - [ ] If any required fields are missing:
     - [ ] Record detailed error in `VERSION_PLAN.md`
     - [ ] Exit with clear error message
   - [ ] Begin executing `create_version.md` starting with Phase 1
   - [ ] For each phase:
     - [ ] Update relevant standard files
     - [ ] Commit changes with descriptive messages
     - [ ] Record all actions in `VERSION_PLAN.md`

4. [ ] **Update Project Files**
   - [ ] Update `plans/_reference/ROADMAP.md` with new version details and status
   - [ ] Add new version section to `plans/_reference/CHANGELOG.md`
   - [ ] Ensure all standard files are complete and consistent
  - [ ] Document key learnings in `VERSION_PLAN.md`
   - [ ] Commit all changes with descriptive messages following the format:
     ```
     type(scope): concise description

     Detailed explanation if needed
     ```
     Where type is one of: feat, fix, docs, style, refactor, test, chore

5. [ ] **Automated Review & Finalization**
   - [ ] Run automated validation checks on all documentation
   - [ ] Verify consistency across all generated files
   - [ ] Apply automatic fixes for any detected issues
   - [ ] Create final commit with review updates
   - [ ] Mark version as 'Ready for Release' in `plans/_reference/ROADMAP.md`

## Expected Workflow
1. [ ] **Pre-Execution**
   - [ ] Validate environment and prerequisites
   - [ ] Exit with error if validation fails

2. [ ] **Execution**
   - [ ] Create version directory with standard files
   - [ ] Process all phases in sequence (as defined in `create_version.md`):
     - [ ] Comprehensive Planning & Design (Automated)
     - [ ] Development Kickoff
     - [ ] Iterative Feature Development & Implementation
     - [ ] Holistic Review, Testing, Documentation & Finalization
   - [ ] Update all relevant files automatically
   - [ ] Commit changes after each phase

3. [ ] **Post-Execution**
   - [ ] Verify all changes were applied
   - [ ] Update `plans/_reference/ROADMAP.md` and `plans/_reference/CHANGELOG.md`
   - [ ] Record completion status in `VERSION_PLAN.md`

## Error Handling & Logging
- [ ] **Logging**: Important actions are recorded in `VERSION_PLAN.md` with timestamps
  - [ ] Format: `[TIMESTAMP] [LEVEL] [SOURCE] Message`
  - [ ] Levels: INFO, WARN, ERROR, DEBUG
  - [ ] Sources: SYSTEM, AI, USER, etc.
- [ ] **Error Handling**
  - [ ] Non-critical issues: Log as WARN and continue
  - [ ] Critical errors: Log as ERROR and exit with code
  - [ ] Include recovery information in the log

## Unattended Execution
- [ ] **Requirements**
  - [ ] Required environment configuration must be set up
  - [ ] Sufficient permissions for file operations

- [ ] **Outputs**
  - [ ] `VERSION_PLAN.md`: Complete execution notes with timestamps
  - [ ] Commits recorded for all changes

- [ ] **Recovery**
  - [ ] If interrupted, can be restarted and will resume from last successful phase
  - [ ] Previous phase outputs are preserved
  - [ ] Logs contain all necessary information for manual recovery if needed
