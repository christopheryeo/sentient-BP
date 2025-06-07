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
4. Code Review & Documentation
5. Final Verification
6. Implementation Review

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

## Slide Architecture Overview

**IMPORTANT**: Understanding the current architecture is critical to successful implementation.

- **Current Implementation**: Slides are implemented in HTML format directly in `index.html`
- **Navigation System**: Uses ID-based navigation with JavaScript function `scrollToSlide()`
- **Important Note**: Do NOT add slides to the JavaScript array in `script.js` as this is not the active implementation

### Known Technical Issues

Be aware that this project has two different slide implementation approaches:

1. **Active Implementation**: Static HTML structure in `index.html`
2. **Inactive Implementation**: Dynamic JavaScript generation in `script.js`

This architectural inconsistency should be addressed in a future refactoring. Until then, all slide changes must be made in `index.html`.

**Future Recommendation**: Consolidate to a single implementation approach.

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
  - `VERSION_PLAN.md`: Version overview, goals (from ROADMAP.md), and high-level progress checkboxes (e.g., for planning, design, implementation, verification). Initialize with checkboxes for key sections like 'Overall Planning', 'Technical Design', 'UX Design', 'Implementation Milestones', 'Testing', 'Documentation'.
  - `TECH_SPEC.md`: Technical specifications including design, architecture, API documentation, and implementation details
  - `TASKS.md`: Tracks progress through the 6 high-level phases (Planning & Design, Development Kickoff, Implementation, Code Review & Documentation, Final Verification, Implementation Review). It will show the status of each phase.
  - `completion_checklist.md`: A dynamic checklist of key milestones and deliverables for the version. Initialized with high-level items.
- Initialize `TASKS.md` to list the 6 standard phases, with the 'Planning & Design' phase marked as 'In Progress' and others as 'To Do'.
- Initialize `completion_checklist.md` with top-level checklist items such as: '[ ] Overall Planning Complete', '[ ] Design Phase Finalized', '[ ] All Core Features Implemented', '[ ] Testing Phase Passed', '[ ] Documentation Complete', '[ ] Final Review Approved'.
- Initialize `VERSION_PLAN.md` with unchecked checkboxes for all defined high-level sections.

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
├── docs/               # Additional documentation and assets
├── learn.log            # Learnings and insights from execution
└── run.log              # (Planned) Errors and AI decisions
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

6. **learn.log**
   - Records learnings and insights from execution
   - Used throughout the version creation process
   - Captures key insights for continuous improvement
7. **run.log** (Planned)
   - Will log errors and AI decisions
   - Implementation details to be determined in future updates

## Actions (Automated)
1. Set up version control branch
2. Initialize consolidated documentation structure
3. Conduct automated technical analysis
4. Generate initial task list for `TASKS.md` based on the granular outputs of the code investigation and Code Impact Analysis.
      - Each task should represent a single, distinct coding action that can be independently implemented and verified. Examples include:
        - "Create function `calculateDiscount(price, discount_rate)` in `utils.js`."
        - "Add `<div class="user-profile">` inside `<header>` in `index.html`.""
        - "Modify CSS rule `.button` in `style.css` to include `background-color: #007bff;`."
        - "Define new configuration key `MAX_USERS` in `config.json`."
      - Tasks should be clearly phrased, indicating the action, the target (e.g., file, function, class), and specifics of the change.
      - These tasks will populate the implementation phase sections of `TASKS.md`.
5. Execute Task 1: Code Impact Analysis
   - Analyze codebase to identify all required changes at a granular level. This includes, but is not limited to:
     - Specific functions/methods to be created, modified, or deleted.
     - Precise HTML structural changes (e.g., new elements, attribute changes on existing elements).
     - Detailed CSS changes (e.g., new classes, properties for existing classes, selectors).
     - Any configuration file adjustments.
     - Individual data transformations or manipulations.
   - The output of this analysis should be a list of discrete, actionable coding steps.
   - Update `TASKS.md` by creating entries for each of these granular, step-by-step implementation tasks, following the formatting guidance detailed above (under "Generate initial task list...").
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
   - Review and update checkboxes in `VERSION_PLAN.md` to reflect completion of initial planning, requirements gathering, and design specifications.

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
3. Review and update `completion_checklist.md`: Refine checklist items based on detailed planning, add sub-tasks if necessary, and mark any pre-development milestones (e.g., 'Detailed Requirements Documented', 'Resource Allocation Confirmed').

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

### 3.0 Slide Implementation Guidelines

#### Adding a New Slide
1. In `index.html`, locate the position where the slide should be added
2. Create a new div with the pattern: `<div id="slideX" class="slide">`
3. Ensure ID numbers are sequential (check existing IDs to determine next available number)
4. Update all subsequent slide IDs and slide numbers to maintain sequential order
5. Add a navigation button in the `.slide-nav` section
6. Add slide content following the established pattern
7. Use relative image paths (e.g., `static/images/example.png`), not absolute paths

#### Implementation Verification
When modifying the HTML app, ensure:
- Slide IDs are sequential and unique
- Slide numbers in headers match their IDs
- Navigation buttons are added for new slides
- All image paths use relative URLs (e.g., `static/images/example.png`)
- Content follows the design guidelines from Style.md

### 3.1 AI Task Alignment Review
**Purpose**: Ensure all tasks align with technical specifications and version plan before execution.

**AI Review Process**:
1. **Input Analysis**:
   - [ ] Load and analyze `TECH_SPEC.md` for technical requirements
   - [ ] Load and analyze `VERSION_PLAN.md` for project objectives
   - [ ] Review all tasks in `TASKS.md`

2. **Alignment Check**:
   - [ ] Verify each task maps to specific technical requirements
   - [ ] Ensure all technical requirements have corresponding tasks
   - [ ] Confirm tasks support version objectives
   - [ ] Identify any gaps or misalignments

3. **Output**:
   - [ ] Document alignment findings in `TASKS.md` under a new 'Alignment Review' section
   - [ ] Flag any misalignments or missing requirements
   - [ ] Provide recommendations for task adjustments

**File Updates**:
- [ ] Update `TASKS.md` with alignment review findings
- [ ] Append review summary to `learn.log`

**Next Steps**:
- [ ] Review AI findings
- [ ] Update tasks if needed
- [ ] Proceed with implementation once aligned

### 3.2 Automated Task Execution
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
   - Update `VERSION_PLAN.md` by marking relevant high-level checkboxes as implementation milestones are achieved (e.g., 'Technical Design Finalized', 'Core Feature X Implemented').
   - Update `TASKS.md` to reflect the current phase's progress (e.g., mark 'Implementation' as 'In Progress', and upon completion of Phase 2, mark 'Development Kickoff' as 'Completed'). Ensure phase start/completion dates are noted.
   - Update `TECH_SPEC.md` with technical specifications
   - Keep `RELEASE_NOTES.md` current with version highlights
   - Update `completion_checklist.md` by marking items as 'In Progress' or '[x]' upon achievement of major implementation milestones (e.g., '[x] Core Feature X Implemented', '[ ] API for Y Developed - In Progress'). Add new items as they emerge.

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

# Phase 4: Code Review & Documentation

## Learning from Previous Phases:
```
[Previous phases' learnings will be automatically inserted here from learn.log]
```

## Information from Previous Phases:
- Implementation status
- Known issues and risks
- Documentation requirements

## Code Quality Check
1. **Code Review**
   - [ ] Verify all changes follow project standards
   - [ ] Ensure consistent coding style
   - [ ] Check for any remaining TODOs or FIXMEs

2. **Documentation**
   - [ ] Update inline code comments
   - [ ] Ensure all new features are documented
   - [ ] Update README if needed

## File Updates (Automated):
1. Update documentation in `docs/`
2. Update inline code comments
3. Update `VERSION_PLAN.md` by marking checkboxes for completed code reviews and documentation milestones.
4. Update `completion_checklist.md` to reflect the status of code reviews, testing progress, and documentation tasks (e.g., '[x] Peer Review for Module Z Complete', '[ ] Technical Documentation Drafted').
5. Append Phase 4 learnings to `learn.log`

---

# Phase 5: Final Verification

## Learning from Previous Phases:
```
[Previous phases' learnings will be automatically inserted here from learn.log]
```

## Code Consistency Check
1. **HTML Structure**
   - [ ] Verify all slide IDs are sequential
   - [ ] Check all navigation buttons work correctly
   - [ ] Ensure all image paths are relative

2. **Documentation**
   - [ ] Update CHANGELOG.md with changes
   - [ ] Ensure all new features are documented

## File Updates (Automated):
1. Update CHANGELOG.md
2. Finalize all documentation
3. Update `VERSION_PLAN.md` by marking relevant checkboxes upon successful final verification and test completion.
4. Update `completion_checklist.md` with the status of all final verification tasks, test results, and approvals (e.g., '[x] All Critical Tests Passed', '[ ] User Acceptance Testing Sign-off').
5. Append Phase 5 learnings to `learn.log`

## Learning & Reflection (Automated):
```
# Phase 5 Learnings - [Date]

## What Went Well
- Code review process effective
- Documentation complete and up-to-date
- Consistent coding style maintained

## Challenges Faced
- Some areas needed additional documentation
- Minor inconsistencies identified and fixed

## Key Insights
- Regular code reviews improve quality
- Good documentation saves time in the long run
```

---

# Phase 6: Implementation Review

## Learning from Previous Phases:
```
[Previous phases' learnings will be automatically inserted here from learn.log]
```

## Review Process
1. **Code Review**
   - Verify all changes meet requirements
   - Ensure consistent style and patterns
   - Check for any remaining issues

2. **Documentation Review**
   - Verify all features are documented
   - Update any outdated documentation
   - Ensure README is up to date

## Final Steps:
1. Update `ROADMAP.md` with completed items
2. Document any remaining technical debt
3. Ensure all high-level objectives in `VERSION_PLAN.md` are checked off as complete.
4. Conduct a final review of `completion_checklist.md` to ensure all items are marked complete, verifying all version objectives and deliverables have been met.
5. Plan next steps for future development

## Learning & Reflection (Automated):
```
# Final Implementation Review - [Date]

## What Went Well
- Successful implementation of all features
- Code quality maintained throughout
- Documentation kept up to date

## Challenges Faced
- Some areas required additional refinement
- Learning curve with certain aspects

## Key Insights
- Regular check-ins maintain momentum
- Documentation is crucial for future maintenance
- Clear requirements lead to better outcomes
```

---

## Version Control
- Keep this file in sync with your project's documentation standards
- Update prompts as your development process evolves
- Include version number and last updated date

*Last Updated: 2025-06-03*
