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
