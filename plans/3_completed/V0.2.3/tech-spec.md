# V0.2.3 - Founder Slide Technical Specifications

## Overview

This document outlines the technical specifications for implementing the founder slide update, specifically the inclusion of Christopher Yeo's photo.

## Technical Requirements

### 1. Image Implementation
- **HTML**:
    - The image will be embedded using an `<img>` tag.
    - The `src` attribute will point to the optimized image file, e.g., `static/images/chris-yeo.png`.
    - The `alt` attribute must be populated with descriptive text for accessibility (e.g., "Headshot of Christopher Yeo, Founder and CEO of Sentient.io").
    ```html
    <img src="static/images/chris-yeo.png" alt="Headshot of Christopher Yeo, Founder and CEO of Sentient.io" class="founder-photo">
    ```
- **CSS**:
    - A dedicated CSS class (e.g., `founder-photo`) will be used to style the image.
    - Styles will control:
        - `max-width` and `height: auto` for responsiveness.
        - Specific `width` and `height` if a fixed size is determined by the design.
        - `border-radius` for rounded corners, if applicable.
        - `box-shadow` for shadow effects, if applicable.
        - `border` for a visible border, if applicable.
        - `margin` and `padding` for spacing.
    - Example CSS:
    ```css
    .founder-photo {
      max-width: 200px; /* Example size */
      height: auto;
      border-radius: 8px; /* Optional */
      border: 1px solid #ccc; /* Optional */
      box-shadow: 2px 2px 5px rgba(0,0,0,0.1); /* Optional */
    }
    ```
- **JavaScript**:
    - No specific JavaScript is anticipated for the image itself unless dynamic loading or interactive elements (e.g., a modal popup on click) are part of the extended requirements. For V0.2.3, the focus is on static display.

### 2. Slide Structure
- The existing HTML structure for slides should be used. The new image element will be integrated into the relevant slide's content block.
- Ensure that the addition of the image does not break the existing slide layout or navigation.

### 3. Performance
- **Image Optimization**: As specified in the design document, the image must be optimized (compressed, correctly sized) before being added to the `static/images/` directory.
- **Lazy Loading**: If the presentation contains many images or if initial load time is a concern, consider implementing lazy loading for images that are not immediately visible. However, for a single founder photo, this might be overkill unless it's part of a larger image optimization strategy.

### 4. Responsiveness
- CSS media queries should be used if necessary to adjust the image size, placement, or styling on different screen sizes (desktop, tablet, mobile).
- The image should scale gracefully and not distort or overflow its container.

### 5. Accessibility
- Adherence to WCAG guidelines for images.
- Ensure the alt text is implemented correctly and provides value to users of assistive technologies.

## Testing Considerations
- Verify the image displays correctly across major browsers (Chrome, Firefox, Safari, Edge).
- Test on different devices/screen resolutions to ensure responsiveness.
- Use a screen reader to check the alt text implementation.
- Check page load speed to ensure the image is not causing performance issues.
