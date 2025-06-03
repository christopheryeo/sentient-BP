# AI Product Version Management - AI Prompts

## Quick Start Guide

### For Users:
1. **Execute this plan**: Simply tell your AI assistant: "Execute plan_version.md"
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
- "Execute plan_version.md" (starts from Phase 1)
- "Continue with Phase 3 of plan_version.md" (resumes from specific phase)
- "Show me the current phase progress" (reviews current status)

---

## AI Execution Instructions

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

# Phase 1: Version Planning

## Questions for the User:
1. What is the version number for this release? (e.g., 1.0.0)
   - *Check ROADMAP.md for the next planned version number*
2. What is the target release date?
   - *Reference the target date from ROADMAP.md*
3. What are the key objectives for this version?
   - *Review the 'Key Deliverables' section in ROADMAP.md*
4. Who are the key stakeholders for this release?
   - *Check previous versions in ROADMAP.md for stakeholder patterns*

## File Updates:
1. Create version directory: `plans/1_planning/VX.Y.Z/`
2. Create `README.md` with version overview
3. Update `ROADMAP.md` with new version details:
   - Move current version from 'Upcoming Versions' to 'Recent Releases'
   - Add new version to 'Upcoming Versions' if not already present
   - Update target dates and status as needed
4. Update `CHANGELOG.md` with new version section

## Actions:
1. Create directory structure:
   ```
   plans/1_planning/VX.Y.Z/
   ├── comms/
   ├── design/
   └── docs/
   ```
2. Initialize version-specific files
3. Set up version control branch

---

# Phase 2: Requirements Gathering

## Questions:
1. What are the main features to be included?
   - Company Facts Slide, as per roadmap. No additional features.
2. Are there any technical constraints or dependencies?
   - None.
3. What are the success criteria for this version?
   - Rely on overall project success metrics. No specific OKRs/KPIs for this slide.

## File Updates:
1. Create `requirements.md` in version directory
2. Update `tasks.md` with initial task breakdown
3. Document technical constraints in `design/constraints.md`

## Actions:
1. Document all requirements
2. Create initial task list
3. Set up tracking for requirements

**Phase 2 completed on 2024-07-26. Requirements gathered and documented in `requirements.md`, `tasks.md`, and `design/constraints.md`.**
---

# Phase 3: Technical Design

## Questions:
1. What are the key technical components needed?
2. Are there any architectural decisions to be made?
3. What are the potential technical risks?

## File Updates:
1. Create `design/architecture.md` with system design
2. Document API specifications in `design/api.md`
3. Create `risks.md` with risk assessment

## Actions:
1. Document system architecture
2. Define API contracts
3. Perform risk assessment
4. Review technical approach with team

---

# Phase 4: Development Kickoff

## Questions:
1. What are the development milestones?
2. Who is responsible for each component?
3. What are the coding standards and practices?

## File Updates:
1. Update `tasks.md` with assigned owners
2. Create `development_guide.md` with standards
3. Document test strategy in `testing/strategy.md`
4. For complex features, create a feature plan using `wip_template.md` in the `plans/1_planning/` directory

## Actions:
1. Set up development environment
2. Initialize codebase structure
3. Conduct kickoff meeting
4. Share development guidelines

---

# Phase 5: Implementation

## Questions:
1. What is the progress against milestones?
2. Are there any blocking issues?
3. Are there any changes to requirements?

## File Updates:
1. Update task progress in `tasks.md`
2. Document technical decisions in `decisions/`
3. Update `risks.md` with new findings

## Actions:
1. Implement features
2. Write unit and integration tests
3. Conduct code reviews
4. Update documentation

---

# Phase 6: Testing & QA

## Questions:
1. What are the test cases?
2. What are the acceptance criteria?
3. Are there any critical bugs?

## File Updates:
1. Create `testing/test_cases.md`
2. Document bug reports in `issues/`
3. Update `CHANGELOG.md` with fixes

## Actions:
1. Execute test cases
2. Report and track bugs
3. Perform regression testing
4. Update documentation

---

# Phase 7: Documentation

## Questions:
1. What documentation needs to be created/updated?
2. Who are the documentation stakeholders?
3. What format is required for final delivery?

## File Updates:
1. Create `docs/user_guide.md`
2. Update `README.md` with usage instructions
3. Prepare release notes in `RELEASE_NOTES.md`

## Actions:
1. Write user documentation
2. Prepare API documentation
3. Create deployment guides
4. Review documentation with stakeholders

---

# Phase 8: Pre-Release

## Questions:
1. Is all testing complete?
2. Are all features implemented and working?
3. Are there any open critical issues?

## File Updates:
1. Finalize `CHANGELOG.md`
2. Update version numbers in all files
3. Create release branch

## Actions:
1. Perform final testing
2. Update all dependencies
3. Prepare release artifacts
4. Get final approvals

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
