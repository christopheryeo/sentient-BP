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
