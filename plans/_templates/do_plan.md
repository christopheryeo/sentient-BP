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
     - `README.md`: Version overview and goals
     - `design.md`: Design specifications and UI/UX details
     - `tech-spec.md`: Technical implementation details
     - `status.md`: Tracks progress (Planning/In Progress/Completed)
   - Copy templates:
     - `plans/_templates/create_version.md`
     - `plans/_templates/questions.md`

3. **Initialize Version Planning**
   - Update `status.md` with initial status: 'Planning'
   - Populate `README.md` with version details from ROADMAP.md
   - Validate all required information is in `questions.md`
   - If any required fields are missing:
     - Log detailed error to `version_creation.log`
     - Exit with clear error message
   - Begin executing `create_version.md` starting with Phase 1
   - For each phase:
     - Use answers from `questions.md`
     - Update relevant standard files
     - Update `status.md` when changing phases
     - Commit changes with descriptive messages
     - Log all actions to `version_creation.log`

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

5. **Peer Review & Finalization**
   - Request peer review from team members
   - Address any feedback or issues found
   - Update documentation based on review feedback
   - Update `status.md` with review outcomes
   - Create final commit with review updates
   - Mark version as 'Ready for Release' in ROADMAP.md

## Expected Workflow
1. **Pre-Execution**
   - Validate environment and prerequisites
   - Verify `questions.md` is complete
   - Exit with error if validation fails

2. **Execution**
   - Create version directory with standard files
   - Process all phases in sequence:
     1. Planning & Design
     2. Development Kickoff
     3. Implementation
     4. Testing & QA
     5. Deployment Preparation
     6. Release & Post-Release
     7. Retrospective
   - Update all relevant files automatically
   - Commit changes after each phase

3. **Post-Execution**
   - Verify all changes were applied
   - Update ROADMAP.md and CHANGELOG.md
   - Generate execution summary in `version_summary.md`
   - Log completion status to `version_creation.log`

## Error Handling & Logging
- **Single Log File**: All logs go to `version_creation.log` with timestamps
  - Format: `[TIMESTAMP] [LEVEL] [SOURCE] Message`
  - Levels: INFO, WARN, ERROR, DEBUG
  - Sources: SYSTEM, AI, USER, GIT, etc.
- **Status Tracking**: `status.md` tracks:
  - Current phase and progress
  - Last completed action
  - Next steps
  - Any active issues
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
  - `version_creation.log`: Complete execution log with timestamps
  - `status.md`: Current status and progress
  - Git commits for all changes

- **Recovery**:
  - If interrupted, can be restarted and will resume from last successful phase
  - Previous phase outputs are preserved
  - Logs contain all necessary information for manual recovery if needed
