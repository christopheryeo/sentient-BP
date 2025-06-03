# V0.2.4 - Management Team Photos & Bios Implementation

> **NEXT PROMPT TO EXECUTE**: 1. Team Section Implementation

This document contains all prompts used with AI coding assistants (like Google Jules) to implement the Management Team Photos & Bios feature for version V0.2.4.

## Purpose
- Track AI-assisted development prompts for the management team section
- Document implementation decisions and design rationale
- Ensure consistency in AI collaboration and code quality
- Provide context for future maintenance

## Implementation Prompts

### 1. Team Section Layout
```
Create a responsive team section layout for the management team with the following requirements:
1. Grid-based layout that adjusts based on screen size (4 columns on desktop, 2 on tablet, 1 on mobile)
2. Each team member card should include:
   - Photo container (circular mask, 200x200px)
   - Name and title
   - Brief bio (truncated with 'Read more')
   - Subtle hover effect (slight scale and shadow)
3. Ensure proper spacing and alignment
4. Add smooth transitions for interactive elements
5. Make sure it's accessible (keyboard navigation, screen reader friendly)
```

### 2. Team Member Cards
```
Implement individual team member cards with the following specifications:
1. Create a reusable card component in JavaScript
2. Each card should display:
   - Circular profile photo (200x200px)
   - Name (H3)
   - Position (H4)
   - Short bio (max 150 characters visible, expandable)
3. Include loading states for images
4. Add subtle animations on hover and focus
5. Ensure proper contrast and readability
```

### 3. Photo Optimization
```
Optimize team member photos with the following requirements:
1. Convert all images to WebP format
2. Generate responsive image sets (1x, 2x, 3x)
3. Implement lazy loading
4. Add proper alt text for accessibility
5. Include a default placeholder image for missing photos
```

### 4. Interactive Bio Expansion
```
Implement an interactive bio expansion feature:
1. Show truncated bio with 'Read more' link
2. Smooth expand/collapse animation
3. Ensure proper ARIA attributes for accessibility
4. Handle focus management
5. Make it keyboard navigable
```
Update the following documentation to reflect the V0.2.4 changes:
1. README.md version history
2. Team member documentation
3. Ensure all image assets are properly documented
```

### 5. V0.2.4 Feature Verification and Finalization
```
Perform a final verification of the V0.2.4 feature implementation ("Management Team Photos & Bios") and related presentation enhancements.

**Task 1: Documentation Review**
- Read and verify the following V0.2.4 documentation files:
    - `plans/1_planning/V0.2.4/README.md`
    - `plans/1_planning/V0.2.4/design.md`
    - `plans/1_planning/V0.2.4/tech-spec.md`
- Confirm that these documents accurately describe the "Management Team Photos & Bios" feature as implemented.
- Ensure they reflect the inclusion of team members: Christopher Yeo, Eddie Leong, Priya Somasundaram, and Gloria Koh.

**Task 2: Management Team Slide Implementation Verification**
- Inspect the `index.html` file, specifically the Management Team slide (expected around Slide 3, with `id="slide3"`).
- Verify the following:
    - **Team Member Images**: Confirm that images for all four executives (Christopher Yeo, Eddie Leong, Priya Somasundaram, Gloria Koh) are correctly sourced from the `static/images/` directory (e.g., `static/images/chris-yeo.png`). Ensure appropriate `alt` text is present for each image.
    - **Team Member Information**: Confirm that names, titles, and biographies for each executive are correctly displayed and correspond to the information provided in `content/content.md` under the "Sentient.io management team combines deep AI expertise with proven enterprise sales execution" section.
    - **Layout**: Check that the team members are presented in a professional and clear layout (e.g., a grid or row of cards).
    - **Responsiveness**: While direct visual confirmation of responsiveness is not possible via code review, check if the HTML structure and CSS classes used (e.g., `team-executive-grid`, `team-member-card`) suggest a responsive design (e.g., use of CSS grid/flexbox, percentage-based widths, or media queries if visible in embedded styles).

**Task 3: Final Slide Professionalism Check**
- Inspect the final slide in `index.html` (expected around Slide 15, with `id="slide15"`).
- Verify the following aspects for professional presentation:
    - **Concluding Message/Call to Action**: Ensure there is a clear concluding message (e.g., "Thank You") and/or a call to action (e.g., "Questions?", "Next Steps").
    - **Contact Information**: Confirm the presence of essential contact information, such as a website URL (e.g., www.sentient.io) and a contact email address (e.g., info@sentient.io).
    - **Layout & Branding**: Check that the layout is clean, uncluttered, and uses whitespace effectively. Verify that company branding (e.g., logo or company name in header/footer) is consistent with other slides.
    - **Overall Professionalism**: Ensure the typography is clear and readable, and the overall appearance aligns with a professional business presentation. The styling should aim for clarity and effective communication, reminiscent of McKinsey presentation standards where appropriate.

**Reporting:**
Provide a summary of your findings for each task. Note any discrepancies or areas that do not align with the requirements.
```

## Review Process
1. Review all team member cards for consistency and accuracy
2. Verify responsive behavior across different devices
3. Check accessibility compliance (keyboard navigation, screen readers)
4. Test image loading performance

## Best Practices for AI Collaboration
1. Provide clear requirements for each team member's content
2. Specify image dimensions and format requirements
3. Request responsive design considerations
4. Ask for accessibility best practices implementation
5. Inquire about performance optimization techniques

## Version Control Integration
- All image assets should be properly named and organized
- Commit messages should reference team member additions/updates
- Tag releases according to semantic versioning

---
*Last Updated: 2025-06-02*
