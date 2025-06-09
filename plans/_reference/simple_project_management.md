# Simple Project Management

This guide outlines a minimal workflow for tracking versions in `ROADMAP.md`,
`CHANGELOG.md`, and per-version `TECH_SPEC.md` files.

## Workflow

1. **Plan versions** in `plans/_reference/ROADMAP.md`.
2. **Start a version** by creating `plans/Versions/VX.Y.Z/TECH_SPEC.md` from the template.
3. **Record updates** in `plans/_reference/CHANGELOG.md` throughout development.
4. **Finish a version** by moving the directory under `plans/Versions/` when complete and
   updating the roadmap.

## Steps

### Plan Versions

Use the roadmap to list upcoming versions, their goals, and target dates. Update it whenever
plans change.

### Start a Version

Copy `plans/_templates/TECH_SPEC.md` to `plans/Versions/VX.Y.Z/TECH_SPEC.md` to begin
working on a version. The `TECH_SPEC.md` contains technical requirements and design notes.

### Record Changes

Keep a running log of changes in the changelog. Include brief descriptions and reference the
version number.

### Complete the Version

When work is finished, move the version directory under `plans/Versions/` and update
`ROADMAP.md` to mark the version as completed.
