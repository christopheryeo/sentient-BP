# AI Product Version Management - AI Prompts

<!-- 
===========================================
CREATE VERSION TEMPLATE
===========================================
PURPOSE:
This template guides the creation and management of new software versions through a structured, AI-assisted workflow. It ensures consistent version planning, development, and release processes.

KEY FEATURES:
- Automated version lifecycle management
- Integrated learning and reflection system
- Structured documentation generation
- Progress tracking and reporting
- Standardized release procedures

USAGE INSTRUCTIONS:
1. Execute the version creation process by running: "Execute do_plan.md" with your AI assistant
   - This will automatically:
     - Read values from `questions.md` as defaults
     - Create the version directory (e.g., `plans/1_planning/VX.Y.Z/`)
     - Copy and initialize this template
     - Set up all necessary files using values from `questions.md`
2. The AI will execute the workflow phases using the pre-defined values
3. All file operations and documentation will be handled automatically using the configuration from `questions.md`

PHASES:
1. Planning & Design (Automated)
2. Development Kickoff
3. Implementation
4. Testing & QA
5. Deployment Preparation
6. Release & Post-Release
7. Retrospective & Roadmap Update

NOTES:
- All file paths are relative to the project root
- Learning is automatically captured in learn.log
- Progress is tracked across sessions
- Automated validation is performed at key decision points
-->

# AI Product Version Management - AI Prompts

## Slide Style Guidelines

All slide content must adhere to the McKinsey presentation standards defined in `content/Style.md`. Key requirements:

1. **Structure**:
   - Use MECE (Mutually Exclusive, Collectively Exhaustive) organization
   - Follow Pyramid Principle: main point first, then supporting data
   - One key message per slide

2. **Visual Design**:
   - Use specified color palette and typography from Style.md
   - Maintain clean alignment and white space
   - Include source attribution for all data

3. **Content**:
   - All claims must be data-driven
   - Keep text concise and scannable
   - Use consistent heading hierarchy

## Status Tracking

Each version directory tracks progress through these stages in `TASKS.md`:
1. **Planning** (Default)
2. **In Progress** (Starts at Phase 3)
3. **Completed** (After Phase 6)

The status is automatically updated during phase transitions and includes timestamps for each state change.

### Example status section in TASKS.md:
```markdown
# Version Status
- **Current Status**: Planning
- **Created**: 2025-06-04T13:44:17+08:00
- **Last Updated**: 2025-06-04T13:44:17+08:00

## Status History
- 2025-06-04T13:44:17+08:00 - Status set to Planning
```

## Quick Start Guide

### For Users:
1. **Execute this plan**: Simply tell your AI assistant: "Execute create_version.md"
2. **No input required**: The AI will automatically execute all phases using configuration from `questions.md`
3. **Review results**: Check the generated files and logs after completion

### For AI Assistants:
**IMPORTANT**: When executing this file, follow these steps exactly:
1. **Read the entire file first** to understand the full scope
2. **Phase by phase**: Work through each section in order
3. **For each phase**:
   - Read all required information from `questions.md` and `ROADMAP.md`
   - Execute the specified actions automatically
   - Update/create any specified files
   - Document decisions/changes
   - Only proceed to next phase when current phase is complete
4. **After each phase**:
   - Save all changes
   - Commit to version control with a descriptive message
   - Verify all actions completed successfully

### Example Commands:
- "Execute create_version.md" (starts from Phase 1)
- "Continue with Phase 3 of create_version.md" (resumes from specific phase)
- "Show me the current phase progress" (reviews current status)

---

## AI Execution Instructions

### General Guidelines
- **Phased Execution**: Follow the phased approach strictly without pausing
- **File Management**: Update all standard files at each phase automatically
- **Documentation**: All AI interactions will be logged in `run.log` with [AI] prefix (planned feature)
- **Error Handling**: Non-blocking errors are logged; critical errors stop execution

### Commit Message Format
```
type(scope): concise description

Detailed explanation if needed
```
Where type is one of: feat, fix, docs, style, refactor, test, chore

### Required Preconditions
1. `questions.md` must be fully populated in the version directory
2. All required directories must exist and be writable
3. Git must be properly configured

### Error Handling & Logging
- **Single Log File**: All logs will go to `run.log` with timestamps (planned feature)
  - Format: `[TIMESTAMP] [LEVEL] [SOURCE] Message`
  - Levels: INFO, WARN, ERROR, DEBUG
  - Sources: SYSTEM, AI, USER, GIT, etc.
- **Status Tracking**: `TASKS.md` tracks:
  - Current phase and progress
  - Last completed action
  - Next steps
  - Any active issues
- **Error Handling**:
  - Non-critical issues: Log as WARN and continue
  - Critical errors: Log as ERROR and exit with code
  - Include recovery information in the log

### File Management
1. **Initial Setup**
   - Copy this template from `plans/_templates/create_version.md` to your version directory (e.g., `plans/1_planning/VX.Y.Z/`)
   - Create a new file named `VERSION_PLAN.md` in the version directory with the version-specific content

### Execution Rules for AI
1. **Phased Execution**
   - Process one phase at a time
   - Never skip ahead or combine phases
   - Verify completion of each phase before proceeding

2. **Configuration Processing**:
   - Read all configuration from `questions.md`
   - Use default values when specific values are not provided
   - Log all decisions and parameter values used

3. **File Operations**
   - Always work in the correct version directory
   - Create/update files as specified in each phase
   - Preserve existing content unless instructed otherwise

4. **Documentation**
   - Update this file with all decisions and changes
   - Use clear, consistent formatting
   - Add timestamps for important actions

5. **Version Control**
   - Commit after each significant change
   - Use descriptive commit messages
   - Include phase number and key actions in messages

### Error Handling
- If an error occurs:
  1. Stop execution
  2. Clearly describe the issue
  3. Suggest solutions
  4. Log critical errors and exit with appropriate error code
- For non-critical issues, log them and continue with the next phase

### Progress Tracking
- After completing each phase:
  1. Mark the phase as complete
  2. Summarize what was accomplished
  3. List any pending items or follow-ups
  4. Save all changes

## Version Control Best Practices
- Commit after each phase completion
- Use semantic versioning for tags
- Include detailed commit messages with:
  - Phase number and name
  - Key changes made
  - Any issues resolved
- Push changes to remote repository regularly

---

# Phase 1: Comprehensive Planning & Design (Automated)

### 1.1 Version Information Extraction
1. **Automatic Extraction**
   - Read version details from ROADMAP.md
   - Parse target date and key deliverables
   - Verify version number is unique
   - Update ROADMAP.md status to 'In Planning'

2. **Validation**
   - Check for required fields in ROADMAP.md
   - Verify version format (semantic versioning)
   - Log any warnings or issues

3. **Default Values**
   - If target date not specified, set to 30 days from today
   - If no deliverables specified, use 'General Improvements'
   - If no stakeholders listed, default to project maintainers

### 1.2 Standard Files Setup
- Ensure all standard files exist in version directory:
  - `VERSION_PLAN.md`: Version overview and goals (from ROADMAP.md)
  - `TECH_SPEC.md`: Technical specifications including design, architecture, API documentation, and implementation details
  - `TASKS.md`: Tracks progress (Planning/In Progress/Completed) and tasks
- Initialize status in `TASKS.md` with initial status: 'Planning'

### 1.3 Validation
- Verify all required information is present in ROADMAP.md
- Check for version conflicts
- Validate technical requirements
- Verify dependency validation is documented

## File Structure

```
plans/1_planning/VX.Y.Z/
├── VERSION_PLAN.md       # Version overview, goals, and high-level design
├── TASKS.md             # Task list, status tracking, and deployment checklist
├── TECH_SPEC.md         # Technical specs, architecture, and requirements
├── RELEASE_NOTES.md     # Release notes and test results
└── docs/               # Additional documentation and assets
```

### File Descriptions:
1. **VERSION_PLAN.md**
   - Version overview and objectives
   - High-level design decisions
   - Scope and success criteria
   - Links to related resources

2. **TASKS.md**
   - Task list with status tracking
   - Current version status and progress
   - Deployment checklist
   - Rollback procedures

3. **TECH_SPEC.md**
   - Technical requirements and specifications
   - System architecture
   - API specifications
   - Design constraints
   - Dependencies

4. **RELEASE_NOTES.md**
   - Release summary
   - New features and changes
   - Known issues
   - Test results summary
   - Upgrade instructions

5. **docs/**
   - Additional supporting documentation
   - Design assets
   - Meeting notes
   - Reference materials

## Actions (Automated)
1. Set up version control branch
2. Initialize consolidated documentation structure
3. Conduct automated technical analysis
4. Generate initial task list starting with code investigation
5. Execute Task 1: Code Impact Analysis
   - Analyze codebase for required changes
   - Update `TASKS.md` with specific implementation tasks
6. Track progress in `TASKS.md`
7. Prepare for development kickoff

*Note: This combined phase is fully automated. The AI will gather all required information from `questions.md` and ROADMAP.md without requiring user input. Values from `questions.md` will be used as defaults throughout the process.*

---

# Phase 2: Development Kickoff

### 2.1 Milestone Review
1. **Automatic Processing**
   - Extract milestones from ROADMAP.md
   - Update `VERSION_PLAN.md` with milestone details
   - Set initial status in `TASKS.md`
   - Populate `TECH_SPEC.md` with technical requirements
   - Update `TECH_SPEC.md` with UI/UX specifications from `questions.md`

2. **Validation**
   - Ensure all milestones have target dates
   - Verify dependencies between milestones
   - Check for resource conflicts

3. **Default Behavior**
   - If no milestones defined, create default development phases
   - Use team members from `questions.md` or default to project team
   - Set reasonable default priorities if not specified

## Learning from Previous Phases:
```
[Previous phase learnings will be automatically inserted here from learn.log]
```

## Information from Previous Phases:
- Key objectives and milestones (from Phase 1)
- Technical requirements and constraints (from Phase 1)
- System architecture (from Phase 1)

## Automatic Verification Checks:
1. **Milestone Review**
   - Verify milestones from Phase 1 are complete and well-defined
   - Log any incomplete or unclear milestones as WARN

2. **Task Status**
   - Verify all tasks have proper status in TASKS.md
   - Log any tasks without status as WARN

3. **Development Standards**
   - Verify development standards are documented in TECH_SPEC.md
   - Log any missing or unclear standards as WARN

## File Updates (Automated):
1. Update `tasks.md` with current status
2. Append Phase 1 learnings to `learn.log`

## Learning & Reflection (Automated):
```
# Phase 2 Learnings - [Date]

## What Went Well
- Successful setup of development environment
- Clear task status tracking established
- Development standards documented

## Challenges Faced
- Potential delays in environment setup
- Need for clarification on some task statuses

## Key Insights
- Early environment setup prevents later delays
- Clear status tracking improves visibility
```

---

# Phase 3: Implementation

### 3.1 Automated Task Execution
1. **Initial Code Analysis**
   - [ ] Perform comprehensive analysis of the codebase
   - [ ] Identify all necessary changes and modifications
   - [ ] Document analysis results including:
     - Files requiring modification
     - Specific changes needed
     - Dependencies and impacts

2. **Task Generation**
   - [ ] Generate specific implementation tasks based on analysis
   - [ ] Reference requirements and specifications from `TECH_SPEC.md` for each task
   - [ ] Organize tasks in logical execution order
   - [ ] Document task dependencies and relationships

3. **Task Execution**
   - [ ] Execute tasks in the predefined sequence
   - [ ] Update task status upon completion
   - [ ] Verify code changes against requirements and design

4. **Code Updates & Testing**
   - [ ] Apply code changes based on the analysis
   - [ ] Run automated tests to verify changes
   - [ ] Commit changes with descriptive messages

## Status Update: In Progress
- Updating status to **In Progress**
- Recording transition timestamp
- Updating status history

## Learning from Previous Phases:
```
[Previous phases' learnings will be automatically inserted here from learn.log]
```

## Information from Previous Phases:
- Current milestone progress
- Open tasks and their status
- Known issues and risks

## Automatic Verification Checks:
1. **Implementation Status Check**
   - Verify implementation progress in TASKS.md
   - Log any blocking issues as WARN with details

2. **Requirements Validation**
   - Verify all requirements from Phase 1 are properly documented in TECH_SPEC.md
   - Log any missing or ambiguous requirements as WARN

## File Updates (Automated):
1. **Core Documentation**
   - Update `VERSION_PLAN.md` with version overview and objectives
   - Maintain `TASKS.md` with current task status and assignments
   - Update `TECH_SPEC.md` with technical specifications
   - Keep `RELEASE_NOTES.md` current with version highlights

2. **Supporting Documentation**
   - Store additional documentation in `docs/` directory
   - Maintain version configuration in `questions.md`
   - Update CI/CD workflows in `.github/workflows/` if configured
   - Keep version control files (`.gitignore`, `CHANGELOG.md`) up to date
   - Append Phase 3 learnings to `learn.log`

Note: Only the files and directories listed in Q1 of code_verification.md should be created or modified.

## Learning & Reflection (Automated):
```
# Phase 3 Learnings - [Date]

## What Went Well
- Progress tracking system effective
- Technical decisions well-documented
- Risk identification proactive

## Challenges Faced
- Some tasks took longer than estimated
- Technical debt identified in certain areas

## Key Insights
- Regular progress updates improve accuracy
- Early risk identification prevents major issues
```

---

# Phase 4: Testing & QA

## Learning from Previous Phases:
```
[Previous phases' learnings will be automatically inserted here from learn.log]
```

## Information from Previous Phases:
- Test strategy and coverage goals
- Known issues and risks
- Quality metrics

## Automatic Verification Checks:
1. Design Alignment Check
   - Verify design matches requirements in TECH_SPEC.md
   - Log any discrepancies as WARN
2. Dependencies Documentation Check
   - Ensure all dependencies are documented in TECH_SPEC.md
   - Log any missing dependencies as WARN

## File Updates (Automated):
1. Update test results in `testing/results/`
2. Sync issues with tracking system
3. Update quality dashboards
4. Append Phase 4 learnings to `learn.log`

## Learning & Reflection (Automated):
```
# Phase 4 Learnings - [Date]

## What Went Well
- Comprehensive test coverage achieved
- Effective bug tracking and triage
- Clear quality metrics established

## Challenges Faced
- Some edge cases not initially considered
- Performance bottlenecks identified

## Key Insights
- Early testing prevents costly fixes later
- Clear metrics improve quality assessment
```

---

# Phase 5: Deployment Preparation

## Learning from Previous Phases:
```
[Previous phases' learnings will be automatically inserted here from learn.log]
```

## Information from Previous Phases:
- Deployment requirements
- Known risks and mitigations
- Rollback procedures

## Automatic Verification Checks:
1. Deployment Checklist Check
   - Verify deployment checklist is complete in TASKS.md
   - Log any incomplete items as WARN
2. Rollback Verification Check
   - Confirm rollback procedures are tested and documented
   - Log any untested rollback procedures as WARN

## File Updates (Automated):
1. Generate deployment checklist
2. Update release documentation
3. Prepare rollback procedures
4. Append Phase 5 learnings to `learn.log`

## Learning & Reflection (Automated):
```
# Phase 5 Learnings - [Date]

## What Went Well
- Comprehensive deployment checklist created
- Clear rollback procedures established
- Documentation complete and up-to-date

## Challenges Faced
- Some deployment dependencies identified late
- Need for additional environment validation

## Key Insights
- Detailed checklists prevent deployment issues
- Clear rollback procedures reduce risk
```

---

# Phase 6: Release & Post-Release

### 6.1 Release Execution
1. **Automated Deployment**
   - Run pre-deployment checks
   - Execute deployment scripts
   - Verify deployment status
   - Rollback on failure with detailed logs

2. **Documentation Updates**
   - Update status in `TASKS.md` to 'Completed'
   - Finalize all version documentation
   - Update ROADMAP.md with completion status
   - Generate CHANGELOG.md entry
   - Create release notes in `release_notes.md`

3. **Post-Release**
   - Archive project files
   - Update any dependent documentation
   - Generate final reports
   - Log deployment details

## File Updates (Automated):
1. Update release documentation
2. Log post-release issues
3. Update ROADMAP.md with release details
4. Append final learnings to `learn.log`

## Learning & Reflection (Automated):
```
# Phase 6 Learnings - [Date]

## What Went Well
- Successful production deployment
- Effective monitoring in place
- Clear support procedures followed

## Challenges Faced
- Minor post-release issues identified
- Need for additional monitoring metrics

## Key Insights
- Continuous monitoring is crucial post-release
- Clear support procedures improve user experience
- Documented learnings improve future releases
5. Review and update future version timelines if needed

## File Updates:
1. Update `ROADMAP.md` with next steps

## Actions:
1. Monitor production
2. Conduct retrospective
3. Document lessons learned
4. Plan next steps

---

## Version Control
- Keep this file in sync with your project's documentation standards
- Update prompts as your development process evolves
- Include version number and last updated date

*Last Updated: 2025-06-03*
