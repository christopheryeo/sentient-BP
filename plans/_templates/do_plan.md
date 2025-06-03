# AI Version Planning Assistant

## How to Use
Simply tell your AI assistant: "Execute do_plan.md"

## Execution Instructions for AI

1. **Review Roadmap**
   - Check ROADMAP.md for the next planned version and its details
   - Verify the target date and key deliverables

2. **Setup Version Directory**
   - Create a new directory: `plans/1_planning/VX.Y.Z/` (replace with actual version)
   - Copy `plans/_templates/plan_version.md` to this new directory

3. **Initialize Version Planning**
   - Begin executing the copied `plan_version.md` starting with Phase 1
   - For each phase, ask the user the required questions
   - Update files and commit changes after each phase

4. **Update Project Files**
   - Update ROADMAP.md with the new version details
   - Update CHANGELOG.md with the new version section
   - Commit all changes with descriptive messages

## Expected Workflow
1. The AI will guide you through each phase of planning
2. You'll be prompted for necessary information
3. All files will be automatically updated and committed
4. Progress will be tracked in version control

## Notes
- The AI will handle all file operations
- You'll be asked to confirm before any changes are made
- You can pause and resume at any time
