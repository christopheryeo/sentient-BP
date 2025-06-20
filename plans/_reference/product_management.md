# Sentient.io Presentation - Project Management Guide

## Table of Contents
- [Starting a New Version](#detailed-steps-for-starting-a-new-version)
- [Project Structure](#project-structure)
- [Workflow](#workflow)
- [Simplified Approach](#simplified-approach)
- [Documentation Standards](#documentation-standards)
- [Version Control](#version-control)
- [AI Collaboration](#ai-collaboration)
- [Quality Assurance](#quality-assurance)
- [Templates & Examples](#templates--examples)
- [Best Practices](#best-practices)

## Version Completion Process

To complete a version and mark it as done, follow these steps:

1. **Run the Completion Process**
   - Execute the completion guide with your AI assistant
   - The assistant will:
   - Locate the current version directory in `plans/Versions/`
    - Guide you through the finalization steps

2. **Automatic Updates**
  - The completion guide will automatically:
    - Update ROADMAP.md to mark the version as completed
    - Update the version's status to **Completed** in `CHANGELOG.md`
    - Record release notes in `CHANGELOG.md`
    - Ensure all documentation is properly updated

3. **Verification**
   - The AI assistant will verify that:
     - All planned features are implemented
     - Documentation is up to date
     - Version numbers are consistent
     - The version status is updated correctly

4. **Completion**
   - Once all steps are completed, the version will be marked as done
   - The version will appear in the "Recent Releases" section of ROADMAP.md
   - The version directory will be in `plans/Versions/` for reference

## Detailed Steps for Starting a New Version

To start the development of the next app version, follow these steps, which involve both manual preparation and AI-assisted automation:

**1. Prerequisites (Manual Setup)**

Before initiating the automated process, you need to prepare two key files:

*   **Update `plans/_reference/ROADMAP.md`**:
    *   Ensure the `ROADMAP.md` file is updated with the details for the new version. This includes:
        *   The new version number (e.g., V0.3.0).
        *   The target date for the version release.
        *   A clear list of key deliverables and objectives for this version.
    *   The AI assistant will read from this file to understand the scope and details of the new version.


**2. Initiating the Process (User Action)**

*   To begin, instruct your AI assistant (e.g., Jules) to: **"Execute `do_plan.md`"**.
*   `do_plan.md` is a master script template located at `plans/_templates/do_plan.md` that orchestrates the setup of the new version.

**3. Automated Setup (AI Execution of `do_plan.md`)**

Upon receiving the instruction, the AI assistant will perform the following automated steps by executing the logic within `do_plan.md`:

*   **Review `ROADMAP.md`**: The AI first checks `plans/_reference/ROADMAP.md` to identify the next planned version, its target date, and key deliverables.
*   **Create Version-Specific Directory**: A new directory for the version will be created in `plans/Versions/`, following a naming convention like `plans/Versions/VX.Y.Z/` (where X.Y.Z is the new version number).
*   **Populate Directory with Standard Planning Files**: The AI will populate this new directory with a minimal set of files needed to manage the version's lifecycle:
    *   `VERSION_PLAN.md`: This is the main guide for the new version. It is created by copying the content from `plans/_templates/create_version.md`.
    *   `TECH_SPEC.md`: For detailing technical specifications, architecture, and requirements.
*   **Implementation Planning**: Tasks are tracked as a numbered checklist directly inside `VERSION_PLAN.md`.
*   **Populate `VERSION_PLAN.md`**: The AI will then populate the `VERSION_PLAN.md` in the new version directory with specific details (like version number, objectives) extracted from `plans/_reference/ROADMAP.md`.

**4. Starting the Development Workflow (AI Execution of `VERSION_PLAN.md`)**

*   Once the setup is complete, the AI assistant will automatically begin executing Phase 1 of the newly created `VERSION_PLAN.md` (which is the content from `plans/_templates/create_version.md`) within the new version's directory (e.g., `plans/Versions/VX.Y.Z/VERSION_PLAN.md`).
*   This `VERSION_PLAN.md` outlines a four-phase workflow for the new version:
    *   Phase 1: Comprehensive Planning & Design
    *   Phase 2: Development Kickoff
    *   Phase 3: Iterative Feature Development & Implementation
    *   Phase 4: Holistic Review, Testing, Documentation & Finalization
*   The AI will follow the instructions within this `VERSION_PLAN.md`, guided by information from `ROADMAP.md` and `TECH_SPEC.md`, to manage the development lifecycle.

**5. Project File Updates (Automated)**

Throughout this process, several key project files are updated automatically:

*   `plans/_reference/ROADMAP.md`:
    *   The status of the new version will be updated to 'In Planning' during Phase 1 of `VERSION_PLAN.md`.
    *   Later, it will be updated with the completion status upon release.
*   `plans/_reference/CHANGELOG.md`: A new section for the version will be added to the `CHANGELOG.md` to document changes as development progresses and upon release.

By following these steps, the development process for a new application version is systematically initiated, leveraging automation to ensure consistency and adherence to the defined project management structure.
---
This guide is based on the information found in `README.md`, `plans/_templates/create_version.md`, and `plans/_templates/do_plan.md`.

## Introduction

Welcome to the Sentient.io Interactive Presentation project management guide. This document provides a structured approach to managing our development process, ensuring consistency, quality, and effective collaboration between team members and AI assistants.

## Simplified Approach

For day-to-day work we rely on two files:

1. **`ROADMAP.md`** – lists features we plan to add.
2. **`CHANGELOG.md`** – records everything that has been implemented.

There are no additional planning documents or version directories. Add future ideas to
`ROADMAP.md` and log completed work in `CHANGELOG.md`.

## Project Structure

```
sentient-BP/
├── content/                 # Core presentation content and assets
│   ├── content.md          # Main content file (Markdown format)
│   ├── source.bundle.html  # Processed HTML bundle with styling
├── plans/                   # Project management documents
│   ├── Versions/           # Version directories
│   │   └── VX.Y.Z/        # Active and completed versions
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
*   **`Versions/`**:
    *   **Purpose**: Contains a directory for each version of the application, regardless of its status (planning, in progress, or completed).
    *   **Content**: Organized into version-specific subdirectories (e.g., `V1.0.0/`, `V1.1.0_feature-name/`). Each subdirectory should contain:
        *   `README.md`: An overview of the version/feature, its goals, and key deliverables.
        *   `TECH_SPEC.md`: Technical specifications, including architecture, data models, API changes, and impact on existing systems.
        *   Other relevant planning documents as needed.
    *   **Directory Naming**: Use semantic versioning for general releases (e.g., `V1.0.0`, `V1.1.0`, `V2.0.0`). For feature-specific planning that might span multiple minor versions or is a significant standalone piece of work, consider `VMAJOR.MINOR_feature-name/` (e.g., `V1.2_search-implementation/`).
    *   **File Naming**: Use standard names like `README.md` and `TECH_SPEC.md`. For other documents, use descriptive kebab-case.

*   **`_reference/`**:
    *   **Purpose**: Stores general project reference materials that are not tied to a specific version or feature lifecycle but are relevant for the overall project.
    *   **Content**: Examples include:
        *   `ROADMAP.md`: High-level overview of the project's long-term vision and planned major versions/features.
        *   `CHANGELOG.md`: A log of all notable changes made to the project, typically organized by version.
        *   `product_management.md`: This document itself, outlining the project management processes.
        *   `content/style.md`, etc.
    *   **File Naming**: Descriptive kebab-case names.

*   **`_templates/`**:
    *   **Purpose**: Contains standardized templates for various documents used in the project management process. This helps maintain consistency and ensures all necessary information is captured.
    *   **Content**: Examples include:
        *   `create_version.md`
        *   `do_plan.md`
    *   **File Naming**: Clearly indicate that it's a template.

This detailed structure, when consistently applied, will significantly improve project organization and knowledge sharing.

## Status Tracking

We track progress with two simple documents:

- `ROADMAP.md` lists features we intend to build.
- `CHANGELOG.md` records what has been completed.

When a feature is finished, its details are added to the changelog and the roadmap can be updated accordingly.

## Version Documentation

Each version directory in `plans/Versions/` should include:

**Directory Naming**: Use semantic versioning (e.g., `V1.0.0`)

        *   `content/style.md`, etc.

    *   **File Naming**: Descriptive kebab-case names.

*   **`_templates/`**:
    *   **Purpose**: Contains standardized templates for various documents used in the project management process. This helps maintain consistency and ensures all necessary information is captured.
    *   **Content**: Examples include:
        *   `create_version.md`
        *   `do_plan.md`
    *   **File Naming**: Clearly indicate that it's a template.

This detailed structure, when consistently applied, will significantly improve project organization and knowledge sharing.
## Workflow

1. Add upcoming features or ideas directly to `ROADMAP.md`.
2. Implement the work.
3. Document completed changes in `CHANGELOG.md`.

## Documentation Standards

### Slide Documentation
All presentations must follow the McKinsey presentation standards defined in `content/Style.md`. This includes:
- Consistent use of the defined color palette and typography
- Adherence to layout and spacing guidelines
- Proper source attribution for all data and visual elements
- Clear, action-oriented slide titles
- MECE (Mutually Exclusive, Collectively Exhaustive) organization
- Data-driven content with proper visualization

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
- **Note on Versioning**: Semantic versioning (MAJOR.MINOR.PATCH) is followed. PATCH versions may include bug fixes or documentation-only releases (e.g., V0.2.2), which are important for project maintenance and clarity, even if they don't introduce new features. MINOR versions typically add new features, and MAJOR versions signify significant changes or milestones.

### Feature and Version Tracking

#### ROADMAP.md
- **Location**: `plans/_reference/ROADMAP.md`
- **Purpose**: Serves as the single source of truth for current and future development plans
- **Contents**:
  - Upcoming versions with status and target dates
  - Current focus with high-level deliverables (detailed tasks are maintained in `VERSION_PLAN.md`)
  - Planned features and improvements
  - Technical debt and future considerations
- **Update Frequency**: During planning meetings and when priorities change
- **Ownership**: Maintained by the product team with input from all stakeholders

#### CHANGELOG.md
- **Location**: `plans/_reference/CHANGELOG.md`
- **Purpose**: Records all notable changes made to the project
- **Format**: Follows [Keep a Changelog](https://keepachangelog.com/) format
- **Contents**:
  - Main app version releases with dates; individual commits are no longer tracked
  - Categorized changes (Added, Changed, Deprecated, Removed, Fixed, Security)
  - Links to relevant issues/PRs
- **Update Frequency**: With each release or significant change
- **Ownership**: Maintained by the development team

#### README.md
- **Location**: Project root directory
- **Purpose**: Serves as the main entry point and high-level project documentation
- **Contents**:
  - Project overview and purpose
  - Quick start guide
  - Key features and screenshots
  - Basic setup instructions
  - Links to detailed documentation
  - Current status and version badge
  - Links to ROADMAP.md and CHANGELOG.md
- **Update Frequency**: When major features are added or significant changes occur
- **Ownership**: Maintained by the core team with input from all contributors

#### Workflow
1. Add ideas to `ROADMAP.md`.
2. Implement the changes.
3. Record what was done in `CHANGELOG.md`.
4. Update the README when major features ship.

## AI Collaboration

### Best Practices for AI Prompts

#### Best Practices for AI Prompts
1. **Be Specific**: Clearly define requirements and constraints
2. **Provide Context**: Include relevant code snippets or file references
3. **Request Explanations**: Ask AI to explain non-obvious implementation choices
4. **Document Assumptions**: Note any assumptions made during implementation
5. **Review Outputs**: Always review and validate AI-generated code

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
- Verify:
  - Code quality and style compliance
  - Performance considerations
  - Security best practices
  - Complete and accurate documentation

## Content Directory Structure

The `content/` directory is the central repository for all presentation content and related assets. It follows this structure:

### 1. content.md
- **Purpose**: Primary content file containing all presentation text and structure
- **Format**: Markdown with custom extensions for presentation-specific elements
- **Sections**:
  - Executive summary
  - Problem statement
  - Solution overview
  - Market analysis
  - Product features
  - Team information
  - Financial projections
  - Roadmap and milestones

### 2. source.bundle.html
- **Purpose**: Processed HTML bundle containing the complete presentation
- **Features**:
  - Responsive design
  - Interactive elements
  - Styled according to McKinsey presentation standards
  - Includes all necessary CSS and JavaScript
- **Structure**:
  - Slide-based layout
  - Consistent header/footer
  - Source attribution
  - Confidentiality notices

### Content Update Workflow
1. Update `content.md` with new content
2. Process through the presentation generator
3. Review `source.bundle.html` for visual fidelity
4. Verify cross-browser compatibility
5. Update version control

### Best Practices for Content Management
1. **Version Control**:
   - Keep content and presentation logic separate
   - Use semantic versioning for major updates
   - Maintain changelog for content updates

2. **Accessibility**:
   - Ensure proper heading hierarchy
   - Include alt text for all images
   - Maintain sufficient color contrast
   - Test with screen readers

3. **Performance**:
   - Optimize images and assets
   - Minimize external dependencies
   - Implement lazy loading where appropriate

## Templates & Examples

### Starting a New Version (do_plan.md)

To begin a new version planning process, simply tell your AI assistant:
```
Execute do_plan.md
```

**Location**: `plans/_templates/do_plan.md`

**What it does**:
- Automatically checks ROADMAP.md for the next version
- Creates and initializes a new version directory
- Guides you through each planning phase
- Updates all necessary files (roadmap, changelog, etc.)
- Handles version control commits

**Requirements**:
- AI assistant with file execution capabilities
- Write access to the repository
- Internet connection (for AI functionality)

### Version Planning Template (create_version.md)

The `create_version.md` template is a comprehensive guide for managing software versions throughout their entire lifecycle. It's designed to be used with AI assistance and follows a four-phase approach from planning to finalization.

#### Location
- Template: `plans/_templates/create_version.md`
- Usage: Copy to `plans/Versions/VX.Y.Z/` when starting a new version

#### Directory Structure Created
When executed, this template will create and manage the following structure:

#### Key Features
- **AI-Assisted Execution**: Can be executed with a single command
- **Phased Approach**: Four phases from planning to finalization
- **Comprehensive Documentation**: Ensures all aspects are documented
- **Version Control Ready**: Includes guidance for Git integration

#### How to Use
1. Copy the template to your version directory
2. Run `Execute create_version.md` with your AI assistant
3. Follow the interactive prompts
4. The AI will handle file creation and updates


### Feature Specification
```markdown
# [Feature Name]

## Version Control

### Commit Messages
- Reference relevant prompt IDs or feature numbers
- Include the version number in the commit message when applicable
- Follow conventional commit message format: `type(scope): description`

### Tags
- Use semantic versioning (e.g., v0.2.3)
- Tag main version releases with corresponding version numbers
- Include release notes in the tag annotation

### Branching Strategy
- `main`: Production-ready code
- `feature/*`: New features or significant changes
- `fix/*`: Bug fixes
- `docs/*`: Documentation updates

### AI-Generated Code
- Document which parts were AI-generated in commit messages
- Include the prompt used in the commit message
- Ensure all AI-generated code is reviewed before merging to main

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
