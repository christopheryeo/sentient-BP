# Sentient.io Presentation - Project Management Guide

## Table of Contents
- [Project Structure](#project-structure)
- [Workflow](#workflow)
- [Documentation Standards](#documentation-standards)
- [Version Control](#version-control)
- [AI Collaboration](#ai-collaboration)
- [Quality Assurance](#quality-assurance)
- [Templates & Examples](#templates--examples)
- [Best Practices](#best-practices)

## Introduction

Welcome to the Sentient.io Interactive Presentation project management guide. This document provides a structured approach to managing our development process, ensuring consistency, quality, and effective collaboration between team members and AI assistants.

## Project Structure

```
sentient-BP/
├── plans/                   # Project management documents
│   ├── 0_backlog/          # Future features and ideas
│   ├── 1_planning/         # Active planning documents
│   ├── 2_inprogress/       # Work in progress
│   ├── 3_completed/        # Completed work
│   ├── _reference/         # Reference materials
│   └── _templates/         # Document templates
├── src/                    # Source code
├── static/                 # Static assets (CSS, images, etc.)
├── templates/              # HTML templates
└── tests/                  # Test files
```

### Plans Directory Organization

The `plans/` directory is central to our project management methodology. It provides a structured way to track ideas, plan upcoming work, manage ongoing tasks, and archive completed efforts. Adhering to a standardized organization within `plans/` ensures clarity and allows for easy replication of our project management processes across different projects.

The standard subdirectories within `plans/` are:

*   **`0_backlog/`**:
    *   **Purpose**: Captures all raw ideas, feature requests, identified bugs, and potential improvements that are not yet scheduled for active development.
    *   **Content**: Typically contains documents like `feature-ideas.md`, `bug-reports.md`, or individual files for larger concepts. Each item should be described with enough detail to be understood later during a planning session.
    *   **File Naming**: Use descriptive kebab-case names (e.g., `user-authentication-enhancement.md`).

*   **`1_planning/`**:
    *   **Purpose**: Holds all documentation related to features or versions that are actively being planned or are slated for near-term development.
    *   **Content**: Organized into version-specific subdirectories (e.g., `V1.0.0/`, `V1.1.0_feature-name/`). Each versioned subdirectory should contain:
        *   `README.md`: An overview of the version/feature, its goals, and key deliverables.
        *   `design.md` or `ui_ux_spec.md`: Detailed design specifications, wireframes, mockups, or user flow diagrams.
        *   `tech-spec.md`: Technical specifications, including architecture, data models, API changes, and impact on existing systems.
        *   Other relevant planning documents (e.g., `requirements.md`, `user-stories.md`).
    *   **Directory Naming**: Use semantic versioning for general releases (e.g., `V1.0.0`, `V1.1.0`, `V2.0.0`). For feature-specific planning that might span multiple minor versions or is a significant standalone piece of work, consider `VMAJOR.MINOR_feature-name/` (e.g., `V1.2_search-implementation/`).
    *   **File Naming**: Use standard names like `README.md`, `design.md`, `tech-spec.md`. For other documents, use descriptive kebab-case.

*   **`2_inprogress/`**:
    *   **Purpose**: Tracks features or versions that are currently under active development. This directory provides a snapshot of ongoing work.
    *   **Content**: Similar to `1_planning/`, it should be organized into version-specific or feature-specific subdirectories. These directories would typically be moved from `1_planning/` once development starts.
        *   The documents within (e.g., `README.md`, `tech-spec.md`) should be updated to reflect the current status, any changes made during development, and progress tracking (e.g., task lists with completed items).
        *   May also include developer notes or logs specific to the ongoing work.
    *   **Note**: It's crucial to keep these documents live and updated throughout the development cycle.

*   **`3_completed/`**:
    *   **Purpose**: Archives all documentation related to features or versions that have been completed, tested, and released (or deployed).
    *   **Content**: Organized into version-specific subdirectories, mirroring the structure from `1_planning/` or `2_inprogress/`. These directories are moved here once a version/feature is finalized.
        *   Documents should reflect the final state of the delivered work.
        *   Should include a `spec.md` or `final_spec.md` that details exactly what was delivered.
        *   May also include a `release_notes.md` specific to that version or a `post_mortem.md` if any valuable lessons were learned.
    *   **Directory Naming**: Follows the same naming convention as `1_planning/` (e.g., `V1.0.0/`).

*   **`_reference/`**:
    *   **Purpose**: Stores general project reference materials that are not tied to a specific version or feature lifecycle but are relevant for the overall project.
    *   **Content**: Examples include:
        *   `ROADMAP.md`: High-level overview of the project's long-term vision and planned major versions/features.
        *   `CHANGELOG.md`: A log of all notable changes made to the project, typically organized by version.
        *   `product_management.md`: This document itself, outlining the project management processes.
        *   `coding_standards.md`, `style_guide.md`, etc.
    *   **File Naming**: Descriptive kebab-case names.

*   **`_templates/`**:
    *   **Purpose**: Contains standardized templates for various documents used in the project management process. This helps maintain consistency and ensures all necessary information is captured.
    *   **Content**: Examples include:
        *   `feature_spec_template.md`
        *   `tech_spec_template.md`
        *   `bug_report_template.md`
        *   `completed_version_readme_template.md`
        *   `wip_readme_template.md`
    *   **File Naming**: Clearly indicate that it's a template, e.g., `template_feature-spec.md` or `feature-spec_template.md`.

This detailed structure, when consistently applied, will significantly improve project organization and knowledge sharing.

## Workflow

1. **Backlog**
   - New features and ideas are added to `0_backlog/`
   - Each idea gets its own markdown file
   - Ideas are reviewed and prioritized regularly

2. **Planning**
   - Selected features move to `1_planning/`
   - Create detailed specifications and designs
   - Get stakeholder approval before implementation

3. **In Progress**
   - Move to `2_inprogress/` when work begins
   - Update documentation as development progresses
   - Regular commits with clear messages

4. **Completed**
   - Move to `3_completed/` when done
   - Include post-implementation review
   - Update feature log

## Documentation Standards

### File Naming
- Use kebab-case for all filenames
- Include version numbers where applicable
- Be descriptive but concise

### Markdown Formatting
- Use ATX-style headers (##)
- Wrap lines at 100 characters
- Use relative links for internal references
- Include tables of contents for long documents

## Version Control

### Branching Strategy
- `main` - Production-ready code
- `develop` - Integration branch
- `feature/` - New features
- `bugfix/` - Bug fixes
- `release/` - Release preparation

### Commit Messages
- Use conventional commits format
- Keep the first line under 50 characters
- Include details in the body if needed
- Reference issue numbers when applicable

## AI Collaboration

### Working with AI
- Be specific in your prompts
- Break down complex tasks
- Review all AI-generated code
- Document AI-assisted work

### Prompt Templates
```
I need help with [specific task]. 
Context: [background information]
Requirements:
- [List requirements]
Constraints:
- [List constraints]
```

## Quality Assurance

### Testing
- Write tests for all new features
- Maintain test coverage above 80%
- Run tests before each commit
- Document test cases

### Code Review
- At least one reviewer required
- Check for:
  - Code quality
  - Performance
  - Security
  - Documentation

## Templates & Examples

### Feature Specification
```markdown
# [Feature Name]

## Overview
[Brief description]

## Requirements
- [ ] Requirement 1
- [ ] Requirement 2

## Design
[Design details]

## Testing
[Test cases]
```

### Bug Report
```markdown
# [Bug Title]

## Description
[What happens vs what should happen]

## Steps to Reproduce
1. Step 1
2. Step 2

## Expected Behavior
[What should happen]

## Environment
- Browser: [e.g., Chrome 95]
- OS: [e.g., macOS 12]
- Device: [e.g., MacBook Pro]
```

## Best Practices

### Code Style
- Follow language-specific style guides
- Use consistent naming conventions
- Keep functions small and focused
- Comment complex logic

### Documentation
- Document public APIs
- Keep READMEs up to date
- Include examples
- Document design decisions

### Performance
- Optimize critical paths
- Lazy load resources
- Minimize dependencies
- Monitor performance metrics

## Glossary

- **Sprint**: A time-boxed development cycle (typically 2 weeks)
- **Epic**: A large body of work that can be broken down into smaller stories
- **User Story**: A requirement expressed from the user's perspective
- **Technical Debt**: The implied cost of additional rework caused by choosing an easy solution now instead of a better approach
- **CI/CD**: Continuous Integration/Continuous Deployment

## Resources

- [Project Board](#)
- [Design System](#)
- [API Documentation](#)
- [Deployment Guide](#)
