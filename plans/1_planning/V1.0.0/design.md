# Design Document: Sentient.io Interactive Presentation

**Version:** V1.0.0

## Design System

### Color Palette
- **Primary:** #D92E26 (Sentient Red)
- **Secondary:** #4CAF50 (Sentient Green)
- **Text:** #2C3E50 (Dark Blue-Gray)
- **Background:** #F5F7FA (Light Gray)
- **Accent:** #2196F3 (Blue)
- **Highlight:** #FFC107 (Amber)

### Typography
- **Primary Font:** Roboto (Google Fonts)
- **Headings:** 700 weight, 2.5-3.5rem
- **Body Text:** 400 weight, 1.1-1.3rem line height
- **Code:** 'Courier New', monospace

### Layout
- **Max Width:** 1200px
- **Content Padding:** 2rem (mobile) to 4rem (desktop)
- **Grid System:** CSS Grid with Flexbox fallbacks
- **Breakpoints:**
  - Mobile: < 768px
  - Tablet: 768px - 1023px
  - Desktop: 1024px+

## Slide Designs

### 1. Title Slide
- Full-bleed background with Sentient branding
- Large, bold title
- Subtitle and tagline
- Subtle animation on load

### 2. Mission & Values
- Two-column layout (text + chart)
- Clean, readable typography
- Icon-based value indicators
- Interactive chart visualization

### 3. Features/Products
- Card-based layout
- Hover effects
- Clear icons
- Concise descriptions

### 4. Statistics
- Animated counters
- Data visualizations
- Comparison charts
- Clear labels and legends

### 5. Contact/CTA
- Clean, focused layout
- Contact information
- Social media links
- Clear call-to-action buttons

## UI Components

### Navigation
- Previous/Next buttons
- Slide indicator dots
- Progress bar
- Keyboard navigation

### Interactive Elements
- Hover states for all interactive elements
- Smooth transitions and animations
- Touch-friendly controls
- Clear visual feedback

### Charts & Visualizations
- Consistent color scheme
- Clear labels and legends
- Responsive scaling
- Interactive tooltips

## Animation Guidelines

### Transitions
- Slide transitions: 300ms ease-in-out
- Fade effects: 200ms ease
- Scale animations: 150ms ease-out

### Micro-interactions
- Button hover: Scale 1.05
- Card hover: Elevation increase + slight scale
- Menu items: Fade + slide in

## Accessibility

### Color Contrast
- Text: Minimum 4.5:1 contrast ratio
- Interactive elements: 3:1 contrast ratio
- Color not used as the only visual cue

### Keyboard Navigation
- Full keyboard accessibility
- Visible focus states
- Logical tab order
- Skip to content link

### Screen Readers
- ARIA labels for interactive elements
- Semantic HTML structure
- Alternative text for images and charts
- Proper heading hierarchy

## Assets

### Icons
- Material Icons
- Custom SVG where needed
- Consistent stroke width (2px)
- Accessible alternatives

### Images
- Optimized for web
- Responsive srcset
- Lazy loading
- Alternative text

## Performance

### Loading Strategy
- Critical CSS inlined
- JavaScript deferred
- Lazy loading for below-the-fold content
- Preload key resources

### Asset Optimization
- SVGs optimized and inlined when possible
- Images in modern formats (WebP)
- Font display: swap
- Minified CSS/JS in production
