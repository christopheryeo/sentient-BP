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
├── content/                 # Core presentation content and assets
│   ├── content.md          # Main content file (Markdown format)
│   ├── source.bundle.html  # Processed HTML bundle with styling
│   └── McKinsey Slide Layout Deep Dive.pdf  # Design reference
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
        *   `prompt.md`: Documentation of all AI prompts used for implementation (see [AI Collaboration](#ai-collaboration) for details).
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
        *   `wip_readme_template.md`
        *   `CHANGELOG_TEMPLATE.md`
        *   `ROADMAP_TEMPLATE.md`
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
   - Move to `3_completed/` when done. This signifies the completion of a defined scope of work, which could be a feature release, a bugfix release, or a documentation-only release (e.g., V0.2.2).
   - Include post-implementation review, if applicable (e.g., for feature releases).
   - Update `plans/_reference/CHANGELOG.md` with all changes, clearly stating the nature of the release.
   - Ensure all changes are properly documented in the changelog, following the Keep a Changelog format.

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
- **Note on Versioning**: Semantic versioning (MAJOR.MINOR.PATCH) is followed. PATCH versions may include bug fixes or documentation-only releases (e.g., V0.2.2), which are important for project maintenance and clarity, even if they don't introduce new features. MINOR versions typically add new features, and MAJOR versions signify significant changes or milestones.

### Feature and Version Tracking

#### ROADMAP.md
- **Location**: `plans/_reference/ROADMAP.md`
- **Purpose**: Serves as the single source of truth for current and future development plans
- **Contents**:
  - Upcoming versions with status and target dates
  - Current focus with detailed task lists
  - Planned features and improvements
  - Technical debt and future considerations
- **Update Frequency**: During planning meetings and when priorities change
- **Ownership**: Maintained by the product team with input from all stakeholders

#### CHANGELOG.md
- **Location**: `plans/_reference/CHANGELOG.md`
- **Purpose**: Records all notable changes made to the project
- **Format**: Follows [Keep a Changelog](https://keepachangelog.com/) format
- **Contents**:
  - Versioned releases with dates and commit hashes
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
1. New features are added to ROADMAP.md under appropriate version sections
2. As work begins, detailed tasks are added to the relevant version in ROADMAP.md
3. Upon completion, changes are recorded in CHANGELOG.md
4. README.md is updated to reflect major changes and new features
5. All documentation is kept in sync with the current state of the project

## AI Collaboration

### Prompt Management

For each version or feature implementation, maintain a `prompt.md` file that documents all AI interactions. This ensures:
- Reproducibility of AI-assisted development
- Clear communication of requirements to AI assistants
- Consistent approach to AI collaboration across the team
- Knowledge transfer for future maintenance

#### Prompt File Structure
Each `prompt.md` should include:
1. **Version/Feature Overview**: Brief description of what's being implemented
2. **Implementation Prompts**: All prompts used with AI assistants
3. **Review Process**: How prompts were reviewed and validated
4. **Best Practices**: Any lessons learned about effective prompting
5. **Version Control**: How changes are tracked and committed

#### Best Practices for AI Prompts
1. **Be Specific**: Clearly define requirements and constraints
2. **Provide Context**: Include relevant code snippets or file references
3. **Request Explanations**: Ask AI to explain non-obvious implementation choices
4. **Document Assumptions**: Note any assumptions made during implementation
5. **Review Outputs**: Always review and validate AI-generated code

Example structure is available in `plans/2_inprogress/V0.2.3/prompt.md`

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

### 3. McKinsey Slide Layout Deep Dive.pdf
- **Purpose**: Reference document for slide design standards
- **Contents**:
  - Slide templates
  - Color schemes
  - Typography guidelines
  - Layout specifications
  - Data visualization standards

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

### Version Planning Template (plan_version.md)

The `plan_version.md` template is a comprehensive guide for managing software versions throughout their entire lifecycle. It's designed to be used with AI assistance and follows a phased approach from planning to post-release.

#### Location
- Template: `plans/_templates/plan_version.md`
- Usage: Copy to `plans/1_planning/VX.Y.Z/` when starting a new version

#### Directory Structure Created
When executed, this template will create and manage the following structure:

```
plans/1_planning/VX.Y.Z/
├── comms/               # Communication materials
│   ├── announcements/   # Release announcements
│   └── updates/         # Status updates
├── design/              # Design documents
│   ├── architecture.md  # System architecture
│   ├── api.md          # API specifications
│   └── constraints.md  # Technical constraints
├── docs/                # Documentation
│   ├── user_guide.md   # End-user documentation
│   └── api/            # API documentation
├── testing/            # Test documentation
│   ├── test_cases.md   # Test scenarios
│   └── strategy.md     # Testing approach
├── decisions/          # Key decisions log
├── issues/             # Bug reports and issues
├── README.md           # Version overview
├── requirements.md     # Feature requirements
├── tasks.md           # Task tracking
├── risks.md           # Risk assessment
└── retrospective.md   # Post-release review
```

#### Key Features
- **AI-Assisted Execution**: Can be executed with a single command
- **Phased Approach**: 10 distinct phases from planning to post-release
- **Comprehensive Documentation**: Ensures all aspects are documented
- **Version Control Ready**: Includes guidance for Git integration

#### How to Use
1. Copy the template to your version directory
2. Run `Execute plan_version.md` with your AI assistant
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
- Tag all releases with corresponding version numbers
- Include release notes in the tag annotation

### Branching Strategy
- `main`: Production-ready code
- `feature/*`: New features or significant changes
- `fix/*`: Bug fixes
- `docs/*`: Documentation updates

### AI-Generated Code
- Document which parts were AI-generated in commit messages
- Include the prompt used in the commit message or reference the prompt.md file
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
