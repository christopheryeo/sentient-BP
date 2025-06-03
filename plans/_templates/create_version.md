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
- Manual review is required at key decision points
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

Each version directory includes a `status.md` file that tracks progress through these stages:
1. **Planning** (Default)
2. **In Progress** (Starts at Phase 3)
3. **Completed** (After Phase 6)

The status is automatically updated during phase transitions and includes timestamps for each state change.

### Example status.md:
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
2. **Follow along**: The AI will guide you through each phase, asking questions and executing tasks
3. **Provide input**: Just answer the questions when prompted - the AI will handle the rest

### For AI Assistants:
**IMPORTANT**: When executing this file, follow these steps exactly:
1. **Read the entire file first** to understand the full scope
2. **Phase by phase**: Work through each section in order
3. **For each phase**:
   - Ask the user the listed questions
   - Update this file with their answers (replace placeholders in square brackets)
   - Execute the specified actions
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
- **Documentation**: All AI interactions are logged in `version_creation.log` with [AI] prefix
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

### File Management
1. **Initial Setup**
   - Copy this file from `plans/_templates/` to your version directory (e.g., `plans/1_planning/VX.Y.Z/`)
   - Rename it to match your version (e.g., `V1.0.0_plan.md`)

### Execution Rules for AI
1. **Phased Execution**
   - Process one phase at a time
   - Never skip ahead or combine phases
   - Verify completion of each phase before proceeding

2. **User Interaction**
   - Ask one question at a time
   - Wait for and carefully record user responses
   - Confirm understanding before proceeding

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
  4. Wait for user input before proceeding

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
  - `README.md`: Version overview and goals (from ROADMAP.md)
  - `design.md`: Design specifications and UI/UX details
  - `tech-spec.md`: Technical implementation details
  - `status.md`: Tracks progress (Planning/In Progress/Completed)
  - `risks.md`: Risk assessment and mitigation plans
  - `dependencies.md`: Technical dependencies and requirements
- Initialize `status.md` with initial status: 'Planning'

### 1.3 Risk Assessment & Mitigation
1. **Risk Identification**
   - Technical risks (new technologies, complexity)
   - Resource risks (team availability, dependencies)
   - Timeline risks (dependencies, external factors)
   - Quality risks (testing coverage, technical debt)

2. **Risk Mitigation**
   - Document each risk in `risks.md`
   - Assign risk owners
   - Define mitigation strategies
   - Set review dates for high-priority risks

3. **Dependency Management**
   - List all technical dependencies in `dependencies.md`
   - Verify version compatibility
   - Document upgrade paths if needed
   - Check for security vulnerabilities

### 1.4 Validation
- Verify all required information is present in ROADMAP.md
- Check for version conflicts
- Validate technical requirements
- Confirm risk assessment is complete
- Verify dependency validation is documented

## File Structure & Setup
1. Create version directory: `plans/1_planning/VX.Y.Z/`
2. Initialize directory structure:
   ```
   plans/1_planning/VX.Y.Z/
   ├── comms/
   ├── design/
   │   ├── architecture.md
   │   ├── api.md
   │   └── constraints.md
   ├── docs/
   ├── requirements.md
   ├── tasks.md
   └── risks.md
   ```

## File Updates (Automated)
1. `README.md` - Version overview and objectives
2. `ROADMAP.md` - Update version status and details
3. `CHANGELOG.md` - Add new version section
4. `design/architecture.md` - System design documentation
5. `design/api.md` - API specifications
6. `requirements.md` - Feature and requirement details
7. `risks.md` - Risk assessment and mitigation

## Actions (Automated)
1. Set up version control branch
2. Initialize all documentation files
3. Conduct automated technical analysis
4. Generate initial task list
5. Prepare for development kickoff

*Note: This combined phase is fully automated. The AI will gather all required information from `questions.md` and ROADMAP.md without requiring user input. Values from `questions.md` will be used as defaults throughout the process.*

---

# Phase 2: Development Kickoff

### 2.1 Milestone Review
1. **Automatic Processing**
   - Extract milestones from ROADMAP.md
   - Update `README.md` with milestone details
   - Set initial status in `status.md`
   - Populate `tech-spec.md` with technical requirements
   - Update `design.md` with UI/UX specifications from `questions.md`

2. **Validation**
   - Ensure all milestones have owners and target dates
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

## Questions for User Confirmation:
1. **Milestone Review**
   - Current milestones: [Auto-populated from Phase 1]
   - Any changes needed? [ ] Yes [ ] No
   - If yes, please specify:

2. **Team Assignments**
   - Based on previous assignments: [Auto-populated from similar past versions]
   - Any changes to component ownership? [ ] Yes [ ] No
   - If yes, please specify:

3. **Development Standards**
   - Current standards: [Auto-populated from organization defaults]
   - Any exceptions needed? [ ] Yes [ ] No
   - If yes, please specify:

## File Updates (Automated):
1. Update `tasks.md` with assigned owners
2. Sync `development_guide.md` with latest standards
3. Generate initial `testing/strategy.md` based on requirements
4. Create feature plans for complex items
5. Append Phase 1 learnings to `learn.log`

## Learning & Reflection (Automated):
```
# Phase 2 Learnings - [Date]

## What Went Well
- Successful setup of development environment
- Clear task assignments established
- Development standards documented

## Challenges Faced
- Potential delays in environment setup
- Need for clarification on some task assignments

## Key Insights
- Early environment setup prevents later delays
- Clear ownership improves accountability
```

---

# Phase 3: Implementation

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
- Open tasks and owners
- Known issues and risks

## Questions for User Confirmation:
1. **Progress Update**
   - Current status: [Auto-calculated % complete]
   - Any blocking issues? [ ] Yes [ ] No
   - If yes, please describe:

2. **Requirements**
   - Current requirements: [From Phase 1]
   - Any changes needed? [ ] Yes [ ] No
   - If yes, please specify:

## File Updates (Automated):
1. Update `tasks.md` with progress
2. Log technical decisions in `decisions/`
3. Update `risks.md` with new findings
4. Append Phase 3 learnings to `learn.log`

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

## Questions for User Confirmation:
1. **Test Results Review**
   - Current coverage: [Auto-calculated %]
   - Any critical issues found? [ ] Yes [ ] No
   - If yes, please reference issue numbers:

2. **Quality Gates**
   - Current status: [Pass/Warning/Fail]
   - Any quality concerns? [ ] Yes [ ] No
   - If yes, please describe:

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

## Questions for User Confirmation:
1. **Deployment Readiness**
   - All pre-deployment checks: [Auto-validated status]
   - Any deployment concerns? [ ] Yes [ ] No
   - If yes, please describe:

2. **Documentation**
   - All documentation updates: [Auto-validated status]
   - Any missing items? [ ] Yes [ ] No
   - If yes, please specify:

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
   - Update `status.md` to 'Completed'
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
```

---

# Phase 9: Release

## Questions:
1. What is the release process?
2. Who needs to be notified?
3. What is the rollback plan?

## File Updates:
1. Tag release in version control
2. Update production documentation
3. Archive release artifacts

## Actions:
1. Deploy to production
2. Verify deployment
3. Send release notifications
4. Update issue tracker

---

# Phase 10: Post-Release

## Questions:
1. Is the release stable in production?
   - *Check monitoring dashboards and error logs*
2. What were the key learnings?
   - Document any deviations from the original roadmap
3. What improvements can be made for next time?
   - Update ROADMAP.md with any timeline adjustments
   - Document any roadmap items that need to be reprioritized

## ROADMAP.md Integration Tasks:
1. Move the completed version from 'Upcoming Versions' to 'Recent Releases'
2. Update the status to 'Completed' with the actual release date
3. Add a brief summary of what was delivered
4. Cross-reference the CHANGELOG.md for detailed changes
5. Review and update future version timelines if needed

## File Updates:
1. Create `retrospective.md`
2. Update `ROADMAP.md` with next steps
3. Archive project documentation

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
