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
1. Comprehensive Planning & Design (Automated)
2. Development Kickoff
3. Iterative Feature Development & Implementation
4. Holistic Review, Testing, Documentation & Finalization

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

The status is automatically updated during phase transitions and includes timestamps for each state change. A central Version Status table in `plans/_reference/CHANGELOG.md` lists all versions and their status—remember to update this table accordingly.

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
        - - [ ] Create function `calculateDiscount(price, discount_rate)` in `utils.js`.
        - - [ ] Add `<div class="user-profile">` inside `<header>` in `index.html`.
        - - [ ] Modify CSS rule `.button` in `style.css` to include `background-color: #007bff;`.
        - - [ ] Define new configuration key `MAX_USERS` in `config.json`.
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

# Phase 3: Iterative Feature Development & Implementation

**Objective**: Implement all features and tasks defined for the version. Code is developed iteratively, with focused commits. Broader documentation updates are deferred to Phase 4.

### 3.1 Iterative Development Cycle
For each key feature or deliverable outlined in `VERSION_PLAN.md` and `ROADMAP.md`:
1.  **Detailed Technical Design (if needed)**:
    *   Flesh out technical specifications for the current feature in `TECH_SPEC.md`. Include specific HTML structure changes, CSS class definitions, JS function logic, etc.
    *   If not done in Phase 1/2, generate granular, actionable sub-tasks for this feature in the "Detailed Tasks" section of `TASKS.md`.
2.  **Code Implementation**:
    *   Implement the code changes as per `TECH_SPEC.md` and `TASKS.md`.
    *   Focus on `index.html` for HTML and CSS (within `<style>` tags), and `src/js/script.js` or `src/js/main.js` if JavaScript is involved.
3.  **Developer Testing**:
    *   Perform unit testing for any JavaScript logic.
    *   (Simulate) Basic functional testing or visual checks for UI changes by describing expected outcomes.
4.  **Code Commits**:
    *   Commit implemented code changes frequently for each significant sub-task or feature part.
    *   Use commit message format: `feat(scope): Description of feature part X` or `fix(scope): Description of fix for Y`. Scope could be the specific component or slide name.
5.  **Update Task Status**:
    *   Mark corresponding detailed tasks in `TASKS.md` by checking their checkbox (e.g., changing `[ ]` to `[x]`) as they are completed.
    *   Update relevant checkboxes for specific implemented features in `VERSION_PLAN.md` (e.g., under a feature's milestone).

### 3.2 Status Tracking during Implementation
-   The overall status for this **Phase 3** in `TASKS.md` (under "Phase Progress") remains 'In Progress' until all coding for all features of the version is complete.
-   The overall version status in `TASKS.md` (e.g., "Overall: In Progress (VX.Y.Z)") remains as is.

### 3.3 File Updates (During this Phase - Minimal)
-   **`TECH_SPEC.md`**: Updated iteratively with technical details as each feature is tackled.
-   **`TASKS.md`**: Detailed tasks for features are added/updated; individual tasks are marked 'DONE'.
-   **`VERSION_PLAN.md`**: Checkboxes for specific feature implementation milestones are marked.
-   **Code files** (e.g., `index.html`, `src/js/script.js`): Modified with new code.
-   **`learn.log`**: AI can log *brief, critical* learnings related to specific implementation challenges immediately, but phase-wide reflections are deferred.
-   **Deferred Documentation**: Updates to `CHANGELOG.md`—including the Version Status table, overall phase progress in `TASKS.md`, `completion_checklist.md` (for phase completion), and comprehensive `learn.log` entries are deferred to Phase 4.

## Learning & Reflection (Automated - Iterative during this Phase)
```
# Phase 3 Learnings (Feature: [Feature Name]) - [Date]

## What Went Well
- [Specific to the feature just implemented]

## Challenges Faced
- [Specific to the feature just implemented]

## Key Insights
- [Specific to the feature just implemented]
```
*(This learning log entry is a template to be used *multiple times* within Phase 3 by the AI, once per major feature implemented. The comprehensive Phase 3 learning summary will be part of Phase 4's batched documentation.)*

---

# Phase 4: Holistic Review, Testing, Documentation & Finalization

**Objective**: Ensure all implemented code is reviewed, comprehensively tested, all documentation is updated in a batch, and the version is prepared for release. This phase begins only after ALL coding for the version is complete.

### 4.1 Code Review (All Features)
1.  **Automated Checks**:
    *   Run linters for HTML, CSS, JavaScript (if available and configured).
    *   Perform static analysis if tools are available.
2.  **Conceptual Peer Review (Simulated)**:
    *   Describe verification of coding standards, consistency, and best practices across all implemented changes.
    *   Check for any remaining TODOs or FIXMEs in the codebase.

### 4.2 Comprehensive Testing (All Features)
1.  **Integration Testing (Simulated)**:
    *   Describe how different implemented features interact (if applicable).
2.  **UI Testing (Simulated for Visuals & Functionality)**:
    *   Verify overall layout and responsiveness of all changed sections.
    *   Check UI consistency and adherence to `content/Style.md`.
    *   Confirm functionality of interactive elements.
3.  **Accessibility Testing (Simulated)**:
    *   Review against WCAG AA criteria (e.g., keyboard navigation, ARIA roles, color contrast for all new elements).
4.  **Cross-Browser Compatibility Testing (Simulated)**:
    *   Describe checks on major browsers (Chrome, Firefox, Safari, Edge).

### 4.3 Batch Documentation Update
1.  **`VERSION_PLAN.md`**:
    *   Mark all main progress checkboxes (e.g., '[x] Implementation Milestones', '[x] Testing', '[x] Documentation') as complete.
    *   Ensure all feature-specific milestones are checked.
2.  **`TASKS.md`**:
    *   Mark **Phase 3: Iterative Feature Development & Implementation** as 'Completed' with end date.
    *   Mark this **Phase 4: Holistic Review, Testing, Documentation & Finalization** as 'In Progress', then 'Completed' with dates.
    *   Update the overall version status (e.g., to 'Verification Complete' or 'Ready for Release').
3.  **`completion_checklist.md`**:
    *   Mark all high-level items (e.g., '[x] All Core Features Implemented', '[x] Testing Phase Passed', '[x] Documentation Complete', '[x] Final Review Approved') as complete.
4.  **`CHANGELOG.md`**:
    *   Update the Version Status table and add a comprehensive entry for the version, detailing all new features, changes, and fixes.
5.  **`RELEASE_NOTES.md`**:
    *   Draft or finalize release notes, including new features, known issues (if any), and test results summary.
6.  **`learn.log`**:
    *   Append a consolidated summary of learnings from the entire Phase 3 (all features) and from this Phase 4.
    *   Example structure for consolidated Phase 3 learnings:
        ```
        # Phase 3 Consolidated Learnings (All Features) - [Date]
        ## Overall What Went Well
        - ...
        ## Overall Challenges Faced
        - ...
        ## Overall Key Insights
        - ...
        ```
7.  **Other Documentation**:
    *   Update `docs/` with any new diagrams or supporting materials.
    *   Ensure `README.md` is up to date if any high-level changes occurred.

### 4.4 Final Verification & Roadmap Update
1.  **Final Sanity Check**: Review all generated files and documentation for consistency and completeness.
2.  **`ROADMAP.md`**: Update the status of the current version to 'Completed' or 'Ready for Release'. Mark all key deliverables for the version as complete.

### 4.5 Final Commit
-   Commit all documentation changes and any minor code fixes from this phase with a message like: `docs: Finalize all documentation and review for VX.Y.Z` or `chore: Complete VX.Y.Z, ready for release`.

## Learning & Reflection (Automated - End of Phase 4)
```
# Phase 4 Learnings (Holistic Review & Documentation) - [Date]

## What Went Well
- Batching documentation updates after all code was complete allowed for a more focused coding phase.
- Comprehensive review caught [example issue].
- Testing process covered [example areas].

## Challenges Faced
- Ensuring all commit messages during Phase 3 were sufficiently descriptive for later CHANGELOG generation.
- Consolidating learnings from multiple small features into a coherent summary required careful tracking.

## Key Insights
- This new workflow (code-first, document-batch) improves developer flow during implementation.
- A good commit message discipline during Phase 3 is crucial for this new workflow.
- Templates for batched documentation (e.g., for consolidated learn.log) can be helpful.
```

---

## Version Control
- Keep this file in sync with your project's documentation standards
- Update prompts as your development process evolves
- Include version number and last updated date

*Last Updated: 2025-06-03*
