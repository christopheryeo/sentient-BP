# Version Completion Assistant

This file helps you complete the current version by locating and executing the version-specific completion checklist.

## How to Use
1. Run: `Execute finish_plan.md`
2. The assistant will:
   - Find the most recent version in `plans/1_planning/`
   - Locate the `completion_checklist.md` in that version directory
   - Execute the checklist to complete the version

## Pre-Execution Checks
- [ ] Verify you're in the project root directory
- [ ] Ensure you have write permissions to the version directories
- [ ] Make sure all changes are committed before starting

## Execution Steps
1. **Locate Current Version**
   - Find the most recent version directory in `plans/1_planning/`
   - Verify the version number and details

2. **Verify Completion Readiness**
   - Check that all planned features are implemented
   - Ensure all tests are passing
   - Verify documentation is up to date

3. **Execute Completion Checklist**
   - Run the version's `completion_checklist.md`
   - Follow all steps in the checklist
   - Update ROADMAP.md and CHANGELOG.md as needed
   - Move the version directory to `plans/Versions/`

4. **Final Verification**
   - Double-check all documentation updates
   - Verify version directory has been moved
   - Ensure all checklist items are completed

## Notes
- This is a template that will be used by the AI assistant
- The actual version number will be determined at runtime
- The assistant will handle all file operations and version management
