# V0.2.1 Visual & Interaction Design

## Visual Design

### 1. Color System
- **Primary**: `#3B82F6` (Blue-500) - Main brand color
- **Secondary**: `#10B981` (Emerald-500) - Success states
- **Accent**: `#8B5CF6` (Violet-500) - Call-to-actions
- **Text**: 
  - Primary: `#1F2937` (Gray-900)
  - Secondary: `#4B5563` (Gray-600)
- **Background**: 
  - Light: `#FFFFFF` (White)
  - Dark: `#F9FAFB` (Gray-50)
- **Borders**: `#E5E7EB` (Gray-200)

### 2. Typography & Assets

#### Typography
- **Font Family**: 'Inter', system-ui, sans-serif
- **Scale**:
  - H1: 3rem (48px), 600 weight
  - H2: 2.25rem (36px), 600 weight
  - H3: 1.875rem (30px), 600 weight
  - Body: 1.125rem (18px), 400 weight
  - Small: 1rem (16px), 400 weight
  - Caption: 0.875rem (14px), 400 weight

#### Image Assets
- **Logo**:
  - File: `sentient-logo.png`
  - Usage: Header, cover slides, footers
  - Sizes: 60px (header), 120px (cover), 40px (footer)

- **Team Photos**:
  - Format: PNG with transparent background
  - Size: 400x400px (source), displayed at 120x120px
  - Style: Circular with subtle border

- **Illustrations**:
  - `smartchat-illustration.png` for detailed graphics
  - `smartchat-illustration.svg` for scalable elements
  - `about-sentient.svg` for decorative elements

#### Image Optimization
- **PNGs**:
  - Max width: 1920px for full-bleed images
  - Quality: 80% for JPG, lossless for PNG
  - Use WebP where supported
- **SVGs**:
  - Optimize with SVGO
  - Inline critical SVGs
  - Lazy load non-critical SVGs
- **Line Heights**: 1.2-1.6 for optimal readability

### 3. Slide Designs

#### Slide 1: Title Slide - Sentient.io revolutionizes enterprise knowledge management through private AI deployment
- **Layout**: Full-bleed header with centered content
- **Elements**:
  - **Logo**: `sentient-logo.png` (top-left, max-height: 60px)
  - **Title**: Large, centered (H1)
  - **Subtitle**: Below title (H3)
  - **Background**: Subtle gradient overlay on dark theme
  - **Presenter Info**: Bottom-right corner
    - Photo: `chris-yeo.png` (circular, 80x80px)
    - Name and title in small text

#### Slide 2: About the Founder - Christopher Yeo brings 25+ years of proven entrepreneurial success and AI expertise to enterprise transformation
- **Layout**: 3-column grid with header
- **Background**: `smartchat-illustration.png` as a subtle watermark
- **Sections**:
  1. **Business Overview** (Left)
     - Icon: Use top-left quadrant of `about-sentient.svg`
     - Key metrics and highlights
  2. **Value Propositions** (Middle)
     - Icon: Middle section of `smartchat-illustration.svg`
     - 3-4 key points with checkmarks
  3. **Financial Highlights** (Right)
     - Icon: Graph element from `smartchat-illustration.svg`
     - Key metrics with trend indicators

#### Team Slide (Additional)
- **Layout**: Grid of team members
- **Team Members**:
  - Chris Yeo: `chris-yeo.png`
  - Eddie Leong: `eddie-leong.png`
  - Gloria Koh: `gloria-koh.png`
  - Priya Somasundaram: `priya-somasundaram.png`
- **Each Card**:
  - Circular photo (120x120px)
  - Name and title
  - Brief 1-2 line description

#### Slide 3: Management Team - Sentient.io management team combines deep AI expertise with proven enterprise sales execution
- **Layout**: Two-column with footer
- **Visual Elements**:
  - Left: Data visualization using elements from `smartchat-illustration.svg`
  - Right: Competitive matrix with brand colors
  - Bottom: Key takeaways with icon callouts
- **Background**: Light texture from `about-sentient.svg` at 5% opacity

#### Executive Summary
- **Layout**: 3-column grid
- **Sections**:
  - Business overview (left)
  - Value propositions (middle)
  - Financial highlights (right)
- **Visuals**: Icons for each section

#### Market Opportunity
- **Layout**: Two-column with footer
- **Sections**:
  - **Market Data (Left)**
    - Market size and growth metrics
    - Trend analysis with line/area charts
    - Key market drivers
  - **Competitive Landscape (Right)**
    - Competitor matrix (2x2 or 3x3)
    - Market share visualization
    - Competitive positioning
  - **Key Takeaways (Bottom)**
    - 3-5 bullet points
    - Actionable insights
    - Data sources and references
- **Chart Specifications**:
  - Type: SVG-based for scalability
  - Color Palette: Brand colors with semantic meaning
  - Interactivity: Tooltips on hover
  - Responsive: Stack on mobile views

#### Market Trends Visualization
- **Time Series Data**
  - Show 3-5 year projections
  - Highlight key inflection points
  - Include confidence intervals
- **Segmentation**
  - By region
  - By product/service
  - By customer segment

#### Competitive Analysis Matrix
- **Axes**
  - X: Market Share/Growth
  - Y: Competitive Strength
- **Bubble Size**: Revenue/Volume
- **Color Coding**: By market segment
- **Interactivity**:
  - Click for company details
  - Filter by category
  - Toggle between metrics

#### Slide 4: Market Problem - Enterprises face critical knowledge management challenges that existing solutions cannot address at scale
- **Layout**: Placeholder for layout description
- **Elements**: Placeholder for elements description

#### Slide 5: Market Potential - Asia-Pacific AI market represents $7.5B opportunity with 65% CAGR driving Sentient.io's expansion strategy
- **Layout**: Placeholder for layout description
- **Elements**: Placeholder for elements description

## Interactive Elements & Accessibility

### 1. Keyboard Navigation
- **Tab Order**: Logical flow through content
- **Skip Links**: Skip to main content
- **Focus States**: Visible focus indicators

### 2. Screen Reader Support
- **ARIA Labels**: For all interactive elements
- **Live Regions**: For dynamic content updates
- **Document Structure**: Proper heading hierarchy

### 3. Color & Contrast
- **Text Contrast**: Minimum 4.5:1
- **UI Elements**: 3:1 contrast
- **Color Independence**: Info not conveyed by color alone

## Testing & Quality Assurance

### 1. Visual Regression Testing
- **Tools**: BackstopJS or Percy.io
- **Test Cases**:
  - Verify layout at all breakpoints
  - Check content rendering
  - Validate interactive states
- **Acceptance Criteria**:
  - Less than 1% visual difference from approved designs
  - No content overlaps or truncation

### 2. Cross-Browser Testing
- **Browsers**:
  - Chrome (latest 2 versions)
  - Firefox (latest 2 versions)
  - Safari (latest 2 versions)
  - Edge (latest 2 versions)
- **Devices**:
  - Desktop (1920px+)
  - Laptop (1366px)
  - Tablet (768px)
  - Mobile (360px)

### 3. Accessibility Testing
- **Tools**:
  - Axe DevTools
  - WAVE Evaluation Tool
  - NVDA Screen Reader
- **Test Cases**:
  - Keyboard navigation
  - Screen reader compatibility
  - Color contrast verification
  - ARIA attribute validation

## Interaction Design

### 1. Navigation
- **Progress Bar**:
  - Position: Fixed bottom
  - Shows: Current/total slides
  - Interactive: Click to navigate
- **Controls**:
  - Previous/Next buttons (sides)
  - Home button (top-left)
  - Fullscreen toggle (top-right)

### 2. Visual Feedback
- **Buttons**:
  - Hover: Slight scale (1.05)
  - Active: Subtle shadow
  - Focus: Clear outline
- **Transitions**:
  - Duration: 200ms
  - Easing: ease-in-out
  - Properties: opacity, transform

### 3. Responsive Behavior
- **Desktop**: Full layout
- **Tablet**: Stacked columns
- **Mobile**: Single column, larger touch targets

## Assets
- **Logo**: SVG format
- **Icons**: 24x24px, 2px stroke
- **Images**: High-res, optimized
- **Charts**: Vector-based where possible

## Accessibility
- WCAG 2.1 AA compliant
- Keyboard navigation support
- Reduced motion preferences respected
- Sufficient color contrast

## Responsive Breakpoints
- Mobile: < 640px
- Tablet: 641px - 1024px
- Desktop: > 1024px

## Performance Budget
- Max bundle size increase: 50KB
- Max animation duration: 500ms
- Max FPS: 60fps

## Browser Support
- Chrome (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Edge (latest 2 versions)

## Testing Plan
1. Manual testing on all supported browsers
2. Automated visual regression testing
3. Performance testing with Lighthouse
4. Accessibility testing with axe
