# Version Setup Checklist

Follow these steps in order. Mark each step as complete when finished.

1. [ ] **Validate Prerequisites**
   - Confirm `plans/_reference/ROADMAP.md` exists
   - Ensure the environment is ready for file creation
   - Verify you have write permissions

2. [ ] **Create Version Directory**
   - Determine the next version number from ROADMAP
   - Make `plans/Versions/VX.Y.Z/`
   - Copy `plans/_templates/create_version.md` to `VERSION_PLAN.md`
   - Copy `plans/_templates/TECH_SPEC.md` to `TECH_SPEC.md`

3. [ ] **Populate Planning Files**
   - Fill `VERSION_PLAN.md` with version objectives from ROADMAP
   - Add initial technical notes to `TECH_SPEC.md`

4. [ ] **Update Project References**
   - Mark the version as "In Planning" in ROADMAP
   - Add a new section to `plans/_reference/CHANGELOG.md`

5. [ ] **Execute Version Plan Phases**
   - Follow each phase in `VERSION_PLAN.md`
   - Record progress after completing a phase

6. [ ] **Finalize Version Setup**
   - Run automated checks and apply fixes if needed
   - Mark the version "Ready for Release" in ROADMAP
   - Add a final summary of all changes
