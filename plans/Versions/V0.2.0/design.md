# V0.2.0 Design Document - Repository Organization

## Version Control Implementation

### 1. Semantic Versioning Scheme
```
MAJOR.MINOR.PATCH
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes and minor updates
```

### 2. Git Tagging Strategy
- Version tags follow the pattern: `V` + `MAJOR.MINOR.PATCH` (e.g., V0.2.0)
- Tags are lightweight and point to specific commits
- Tags are pushed to remote repository for team access

### 3. Commit Message Guidelines
- Use present tense ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Include more detailed description when necessary
- Reference issues or pull requests when applicable

## Repository Structure

### 1. Planning Directories
```
plans/
├── 0_backlog/          # Future feature ideas and proposals
├── 1_planning/         # Currently planned versions
├── 2_in_progress/      # Actively being worked on
└── Versions/        # Completed versions with documentation
```

### 2. Version Documentation
Each version in `Versions/` includes:
- README.md: Overview and goals
- design.md: Implementation details
- tech-spec.md: Technical specifications
