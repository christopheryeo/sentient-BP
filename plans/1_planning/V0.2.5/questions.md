# Version Planning Questions

<!--
===========================================
QUESTIONS TEMPLATE
===========================================
PURPOSE:
This file contains all the questions needed for automated version planning.
The AI will use these answers to execute `create_version.md` without interruption.

INSTRUCTIONS:
1. Fill in your answers below each section
2. Set boolean flags (true/false) to indicate if changes are needed
3. Provide details only when the corresponding flag is set to true
4. Keep the YAML syntax intact
5. Save the file when done

NOTE: All fields are optional - the AI will use default values for any missing fields
-->

## Phase 2: Development Kickoff

### Milestone Review
```yaml
# Set to true if you need to modify any milestones from ROADMAP.md
milestone_changes_needed: false  # true/false

# If milestone_changes_needed is true, describe the changes needed:
# - Be specific about what milestones need to change
# - Include version numbers and new dates if applicable
milestone_changes: |
  # Example:
  # - Move V1.2.0 release date to 2025-07-15
  # - Add new milestone for feature X in V1.3.0
```

### Team Assignments
```yaml
# Set to true if you need to change component ownership from defaults
ownership_changes_needed: false  # true/false

# If ownership_changes_needed is true, specify the changes:
# - List components and their new owners
# - Include contact information if relevant
ownership_changes: |
  # Example:
  # - Component: Frontend
  #   New Owner: Jane Smith
  #   Contact: jane@example.com
  # - Component: Backend API
  #   New Owner: AI Assistant
```

### Development Standards
```yaml
# Set to true if you need any exceptions to standard development practices
standard_exceptions_needed: false  # true/false

# If standard_exceptions_needed is true, describe:
# - Which standards need exceptions
# - The reason for each exception
# - Any alternative approaches being taken
standard_exceptions: |
  # Example:
  # - Standard: Code coverage requirement
  #   Exception: Reduce from 90% to 80%
  #   Reason: Limited test coverage for legacy components
  #   Mitigation: Will improve in next sprint
```

## Phase 3: Implementation

### Progress Update
```yaml
# Set to true if there are any issues blocking progress
blocking_issues: false  # true/false

# If blocking_issues is true, provide details:
# - Describe each blocking issue
# - Include impact and potential solutions
# - Reference any related tickets or discussions
blocking_issues_description: |
  # Example:
  # 1. Issue: Database connection timeout
  #    Impact: Blocks user authentication
  #    Solution: Increase timeout threshold
  #    Ticket: DB-123

# Set to true if any requirements need to change from original plan
requirements_changes_needed: false  # true/false

# If requirements_changes_needed is true, specify:
# - Which requirements are changing
# - Reason for the change
# - Impact on timeline/scope
requirements_changes: |
  # Example:
  # - Change: Remove dark mode feature
  #   Reason: Technical limitations with current framework
  #   Impact: Moved to V1.3.0
```

## Phase 4: Testing & QA

### Test Results Review
```yaml
# Set to true if any critical issues were found during testing
critical_issues_found: false  # true/false

# If critical_issues_found is true, provide details:
# - List each critical issue
# - Include test case IDs and descriptions
# - Note severity and priority
critical_issues: |
  # Example:
  # - ID: TEST-456
  #   Description: Payment processing fails for amounts over $10,000
  #   Severity: Critical
  #   Status: Blocking release
  #   Assigned To: Payments Team

# Set to true if there are any quality concerns that don't block release
quality_concerns: false  # true/false

# If quality_concerns is true, describe:
# - Nature of the quality issues
# - Potential impact
# - Recommended actions
quality_issues: |
  # Example:
  # - Issue: Performance degradation in search results
  #   Impact: 20% slower response times
  #   Action: Optimize database queries
  #   Target: V1.2.1
```

## Phase 5: Deployment Preparation

### Deployment Readiness
```yaml
# Set to true if there are any concerns about deployment
deployment_concerns: false  # true/false

# If deployment_concerns is true, document:
# - Specific deployment risks
# - Mitigation strategies
# - Contingency plans
deployment_issues: |
  # Example:
  # 1. Risk: Database migration required
  #    Mitigation: Test migration in staging first
  #    Rollback Plan: Database restore point
  #    Owner: DevOps Team
  #    Status: Testing in progress

# Set to true if any required documentation is missing
documentation_missing: false  # true/false

# If documentation_missing is true, list:
# - Missing document names
# - Responsible person/team
# - Due date
missing_docs: |
  # Example:
  # - API Documentation (Dev Team, due: 2025-06-10)
  # - Deployment Checklist (Ops Team, due: 2025-06-08)
  # - Rollback Procedures (DevOps, due: 2025-06-09)
```

## Phase 6: Release & Post-Release

### Release Status
```yaml
# Set to true if any issues were found after release
post_release_issues: false  # true/false

# If post_release_issues is true, document:
# - Description of each issue
# - Severity level (Critical/High/Medium/Low)
# - Current status and next steps
issues_description: |
  # Example:
  # 1. Issue: Mobile app crashes on iOS 15
  #    Severity: High
  #    Status: Under investigation
  #    Next Steps: Hotfix in progress
  #    ETA: 24 hours

# Set to true if there are concerning user feedback trends
user_feedback_concerns: false  # true/false

# If user_feedback_concerns is true, summarize:
# - Nature of feedback
# - Volume and source
# - Recommended actions
user_feedback: |
  # Example:
  # - Feedback: Confusion about new dashboard layout
  #   Volume: 25+ support tickets
  #   Source: In-app feedback and support tickets
  #   Action: Schedule UI/UX review session
```

## Phase 7: Retrospective & Roadmap Update

### Retrospective
```yaml
key_learnings: |
  # Document key learnings from this version

improvement_areas: |
  # Areas for improvement in future versions

roadmap_updates_needed: false  # true/false
roadmap_updates: |
  # Describe any roadmap updates needed
```

## Version Information
```yaml
# Auto-populated by do_plan.md
version: VX.Y.Z
created_date: YYYY-MM-DD
status: Planning
```

## Usage Notes
1. Set boolean flags to `true` only if you need to provide additional information
2. Keep all YAML syntax intact
3. The AI will automatically process this file during execution
