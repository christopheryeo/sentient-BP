# V0.2.4 - Founder Slide Implementation Prompts

> **PROMPT 4 COMPLETED**: Vision and Approach Enhancement
> **NEXT PROMPT TO EXECUTE**: 5. Documentation Updates

This document contains all prompts used with AI coding assistants (like Google Jules) to implement the features and fixes for version V0.2.4.

## Purpose
- Track AI-assisted development prompts for reproducibility
- Document the thought process behind implementation decisions
- Provide context for future maintenance and updates
- Ensure consistency in AI collaboration

## Implementation Prompts

### 1. Founder Photo Implementation
```
Add a professional headshot of the founder (Chris Yeo) to the 'About the Founder' slide.
The image file is named 'chris-yeo.png' and is located in the static/images/ directory.
Please ensure:
1. The image is properly sized and centered
2. It has a subtle border and shadow
3. Alt text is included for accessibility
4. The image is responsive on all screen sizes
```

### 2. Photo Size Adjustment
```
The founder's photo on the 'About the Founder' slide needs to be 70% larger.
Current size is 200px, please adjust to 340px while maintaining aspect ratio.
Update both the HTML and any related CSS to ensure proper display.
```

### 3. Employment History Update
```
Update Christopher Yeo's employment history to include:
1. A*STAR entry with focus on IP commercialization
2. Singapore Press Holdings entry
3. Ensure proper chronological order

Update both content.md and index.html to maintain consistency.
```

### 4. Vision and Approach Enhancement
```
Please enhance the 'Vision and Approach' section of the founder slide by making it 50% more concise while maintaining all key points and impact. The content and layout must strictly adhere to McKinsey slide standards as defined in 'content/McKinsey Slide Layout Deep Dive.pdf'.

Content Requirements:
1. More scannable and readable from a distance (minimum 24pt font for body text)
2. Focused on the most impactful statements (maximum 5-7 bullet points)
3. Structured with clear, concise bullet points (one idea per bullet)
4. Maintain the professional and visionary tone
5. Keep all essential technical and business value propositions
6. Use consistent formatting and parallel structure

McKinsey Layout Standards to Follow:
- Clear hierarchy of information (Headline, Subhead, Body)
- Left-aligned text with proper line spacing (1.0-1.5)
- Generous white space (minimum 0.5" margins)
- Consistent bullet point style and indentation
- High contrast between text and background
- Limited color palette (2-3 colors max)
- Visual balance and alignment
- Data visualization where applicable

Current content for reference:
[Include current Vision and Approach content here]

Please provide:
1. The revised version of the content
2. Explanation of key changes made
3. How the new version adheres to McKinsey standards
4. Any recommended visual elements or data visualizations that could enhance the slide
```

### 5. Documentation Updates
```
Update the following documentation to reflect the V0.2.4 changes:
1. README.md version history
2. Any relevant design documentation
3. Ensure all file paths and references are accurate
```

## Review Process
1. All prompts should be reviewed by a team member before implementation
2. Actual implementation should be verified against the prompt requirements
3. Any deviations from the prompt should be documented with reasoning

## Best Practices for AI Collaboration
1. Always include context about the project and current state
2. Be specific about requirements and constraints
3. Ask for explanations of any non-obvious implementation choices
4. Request code to be well-commented for future maintenance
5. Ask about potential edge cases and error handling

## Version Control Integration
- All changes should be committed with descriptive messages
- Reference the relevant prompt ID in commit messages when applicable
- Tag releases according to semantic versioning

---
*Last Updated: 2025-06-02*
