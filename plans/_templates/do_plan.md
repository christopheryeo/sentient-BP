# AI Version Planning Assistant

## How to Use
1. Pre-populate `questions.md` with required information
2. Run: `Execute do_plan.md`

## Pre-Execution Validation
1. **Check Prerequisites**
   - Verify ROADMAP.md exists and is accessible
   - Ensure git is initialized and configured
   - Check for required permissions in the repository

2. **Load questions.md**
   - Read and parse the YAML configuration from questions.md
   - Use the values as defaults for all operations
   - If questions.md is missing, create it with default values

3. **Environment Setup**
   - Create required directories if they don't exist
   - Verify write permissions
   - Initialize any required services or connections

## Execution Instructions for AI

1. **Review Roadmap**
   - Check ROADMAP.md for the next planned version and its details
   - Verify the target date and key deliverables

2. **Setup Version Directory**
   - Create a new directory: `plans/1_planning/VX.Y.Z/` (using semantic versioning)
  - Create standard files in the new directory:
    - `VERSION_PLAN.md`: Version overview, goals, and high-level design
    - `TECH_SPEC.md`: Technical specifications and architecture
    - `RELEASE_NOTES.md`: Release notes and test results
  - Copy templates:
    - Use `plans/_templates/create_version.md` as the initial content for `VERSION_PLAN.md`
    - `plans/_templates/questions.md`

3. **Initialize Version Planning**
   - Populate `VERSION_PLAN.md` with version details from ROADMAP.md
   - Validate all required information is in `questions.md`
   - If any required fields are missing:
     - Log detailed error to `run.log` (planned feature)
     - Exit with clear error message
   - Begin executing `create_version.md` starting with Phase 1
   - For each phase:
     - Use answers from `questions.md`
     - Update relevant standard files
     - Commit changes with descriptive messages
     - Log all actions to `run.log` (planned feature)

4. **Update Project Files**
   - Update ROADMAP.md with new version details and status
   - Add new version section to CHANGELOG.md
   - Ensure all standard files are complete and consistent
   - Document key learnings in `learn.log`
   - Commit all changes with descriptive messages following the format:
     ```
     type(scope): concise description
     
     Detailed explanation if needed
     ```
     Where type is one of: feat, fix, docs, style, refactor, test, chore

5. **Automated Review & Finalization**
   - Run automated validation checks on all documentation
   - Verify consistency across all generated files
   - Apply automatic fixes for any detected issues
   - Create final commit with review updates
   - Mark version as 'Ready for Release' in ROADMAP.md

## Expected Workflow
1. **Pre-Execution**
   - Validate environment and prerequisites
   - Verify `questions.md` is complete
   - Exit with error if validation fails

2. **Execution**
   - Create version directory with standard files
   - Process all phases in sequence (as defined in `create_version.md`):
     1. Comprehensive Planning & Design (Automated)
     2. Development Kickoff
     3. Iterative Feature Development & Implementation
     4. Holistic Review, Testing, Documentation & Finalization
   - Update all relevant files automatically
   - Commit changes after each phase

3. **Post-Execution**
   - Verify all changes were applied
   - Update ROADMAP.md and CHANGELOG.md
   - Generate execution summary in `RELEASE_NOTES.md`
   - Log completion status to `run.log` (planned feature)

## Error Handling & Logging
- **Single Log File**: All logs will go to `run.log` with timestamps (planned feature)
  - Format: `[TIMESTAMP] [LEVEL] [SOURCE] Message`
  - Levels: INFO, WARN, ERROR, DEBUG
  - Sources: SYSTEM, AI, USER, GIT, etc.
- **Error Handling**:
  - Non-critical issues: Log as WARN and continue
  - Critical errors: Log as ERROR and exit with code
  - Include recovery information in the log

## Unattended Execution
- **Requirements**:
  - `questions.md` must be fully populated before execution
  - Required git configuration must be set up
  - Sufficient permissions for file operations

- **Outputs**:
  - `run.log`: Complete execution log with timestamps (planned feature)
  - Git commits for all changes

- **Recovery**:
  - If interrupted, can be restarted and will resume from last successful phase
  - Previous phase outputs are preserved
  - Logs contain all necessary information for manual recovery if needed
