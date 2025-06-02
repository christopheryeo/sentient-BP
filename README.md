# Sentient.io Interactive Presentation

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.2.3-blue.svg)](plans/_reference/CHANGELOG.md)

An interactive, multi-slide presentation for Sentient.io, built with HTML5, CSS3, and vanilla JavaScript.

## 📋 Table of Contents
- [✨ Features](#-features)
- [🚀 Getting Started](#-getting-started)
- [📁 Project Structure](#-project-structure)
- [💻 Development](#-development)
- [📊 Project Management](#-project-management)
- [🗺️ Roadmap](#-roadmap)
- [📜 Version History](#-version-history)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📚 Documentation](#-documentation)

## ✨ Features

### Core Presentation
- **Responsive Design**: Works on all device sizes
- **Modern UI**: Clean and professional interface
- **Interactive Elements**: Smooth animations and dynamic content
- **Chart Integration**: Using Chart.js for data visualization
- **Accessibility**: Built with accessibility in mind
- **Touch Support**: Works on touch devices

### Technical Highlights
- Built with vanilla JavaScript (no frameworks)
- Uses CSS Grid and Flexbox for layouts
- Mobile-first responsive design
- Accessible UI components
- Optimized performance

## 🚀 Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- (Optional) Local web server for development

### Quick Start
1. **Clone the repository**
   ```bash
   git clone https://github.com/christopheryeo/sentient-BP.git
   cd sentient-BP
   ```

2. **Open in Browser**
   Simply open `index.html` in your preferred web browser
   ```bash
   open index.html
   ```

## 📁 Project Structure

```
sentient-BP/
├── src/                    # Source code
│   ├── js/                 # JavaScript files
│   │   └── script.js       # Main JavaScript file
│   ├── css/                # Stylesheets
│   │   └── style.css       # Main stylesheet
│   ├── assets/             # Images, fonts, etc.
│   └── views/              # Additional HTML views
│       ├── presentation-fixed.html  # Alternative presentation
│       └── simple.html             # Simplified version
├── dist/                   # Compiled/built files (if using a build tool)
├── plans/                  # Project management
│   ├── 0_backlog/          # Future features and ideas
│   ├── 1_planning/         # Active planning
│   ├── 2_inprogress/       # Work in progress
│   ├── 3_completed/        # Completed work
│   ├── _reference/         # Reference materials
│   └── _templates/         # Document templates
├── content/                # Generated content
│   └── source.bundle.html  # Bundled HTML output
├── index.html              # Main entry point (presentation)
└── README.md               # This file
```

## 💻 Development

### Customization
- Update content in the `slidesData` array in `script.js`
- Modify theme colors in the `:root` CSS variables
- Adjust slide structure as needed

### Building
This project uses vanilla JavaScript and doesn't require a build step. Simply edit the source files and refresh your browser.

### Testing
1. Open `index.html` in your browser
2. Test all interactive elements
3. Verify responsiveness across different screen sizes
4. Check accessibility using browser developer tools

## 📊 Project Management

We use a structured approach to manage the project's development:

- **Backlog**: Future features and ideas in `plans/0_backlog/`
- **Planning**: Active planning documents in `plans/1_planning/`
- **In Progress**: Current work in `plans/2_inprogress/`
- **Completed**: Finished work in `plans/3_completed/`

For more details, see our [Project Management Guide](plans/_reference/product_management.md).

## 🗺️ Roadmap

See our [Roadmap](plans/_reference/ROADMAP.md) for planned features and future direction.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Documentation

- [Changelog](plans/_reference/CHANGELOG.md)
- [Roadmap](plans/_reference/ROADMAP.md)
- [Project Management](plans/_reference/product_management.md)

---

📅 *Last Updated: 2025-06-02*

3. **Navigate**
   - Use the "Next" and "Previous" buttons to move between slides
   - Or use keyboard arrow keys for navigation

## 📁 Project Structure

```
sentient-BP/
├── src/                    # Source code
│   ├── js/                 # JavaScript files
│   ├── css/                # Stylesheets
│   └── assets/             # Images, fonts, etc.
├── plans/                  # Project management
│   ├── 0_backlog/          # Future features and ideas
│   ├── 1_planning/         # Active planning
│   ├── 2_inprogress/       # Work in progress
│   ├── 3_completed/        # Completed work
│   └── _reference/         # Reference materials
├── content/                # Generated content
├── index.html              # Main entry point
└── README.md               # Project documentation
```

## Project Structure

```
sentient-BP/
├── css/
│   └── styles.css       # Main stylesheet
├── js/
│   └── main.js         # Main JavaScript file
├── images/              # Image assets
├── index.html           # Main HTML file
└── README.md            # Project documentation
```

## Customization

### Theme Colors
Edit the CSS variables in `css/styles.css` to match your brand colors:

```css
:root {
    --primary-color: #D92E26;  /* Sentient.io Red */
    --secondary-color: #4CAF50; /* Accent Green */
    --text-color: #333;
    --bg-color: #f8f9fa;
    --slide-bg-color: #ffffff;
    --border-color: #e0e0e0;
    --accent-color: #007bff;
}
```

### Modifying Slides
1. Edit the `slidesData` array in `script.js` to update slide content
2. Each slide can have:
   - `title`: Slide heading
   - `content`: HTML content
   - `init`: Optional function that runs when the slide loads (e.g., for charts)

### Adding New Features
1. Add new slide content in the `slidesData` array
2. Add custom styles in `css/styles.css`
3. Extend functionality in `js/main.js`

## Browser Support

The presentation is tested and works well on:

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile Safari (iOS 13+)
- Chrome for Android

## License

This project is open source and available under the [MIT License](LICENSE).

## Implementation Notes

### Key Implementation Details
- **Slide Management**: Slides are managed through a simple array of objects in JavaScript
- **Responsive Design**: Uses CSS Grid and Flexbox for layouts
- **Accessibility**: Includes ARIA attributes and keyboard navigation
- **Performance**: Optimized animations and efficient DOM updates

### Dependencies
- [Chart.js](https://www.chartjs.org/) - For interactive charts
- [Normalize.css](https://necolas.github.io/normalize.css/) - For consistent browser styling

## 📜 Version History

| Version  | Commit    | Description                                                                 |
|----------|-----------|-----------------------------------------------------------------------------|
| V0.2.3   | `xxxxxxx` | Completed founder slide update (prompt 4) and documentation                 |
| V0.2.2g  | `342183e` | Updated Chris Yeo's biography with additional employment history            |
| V0.2.2f  | `6260588` | Reviewed and finalized documentation for V0.2.2                              |
| V0.2.2e  | `bccab7f` | Planned next versions (V0.2.3-V0.2.8) with detailed feature breakdowns       |
| V0.2.2d  | `43eacfd` | Cleaned up project files and removed temporary files                        |
| V0.2.2c  | `28ba832` | Cleaned up project files                                                   |
| V0.2.2b  | `9e78f1b` | Added comprehensive business plan content to content.md                      |
| V0.2.2a  | `d1c6378` | Improved Markdown linting and formatting in content.md                       |
| V0.2.2   | `c7af4de` | Documentation corrections and updates for V0.2.1                             |
| V0.2.1   | `0f8c137` | Completed slides 1-15, updated documentation and moved V0.2.1 to completed  |
| V0.2.0e  | `e5b0354` | Added full BP presentation to source.bundle.html                            |
| V0.2.0d  | `395c6a9` | Updated source.bundle.html with code generated from Claude 4                |
| V0.2.0c  | `a1e1531` | Confirmed plans directory consistencies and removed V1.0.0                  |
| V0.2.0b  | `01ffc4f` | Moved V0.2.1 to in progress section                                         |
| V0.2.0a  | `07b3c20` | Finalised features and design planning                                      |
| V0.2.0   | `955cdfb` | Created git tags as versions and adjusted plans                            |
| V0.1.9   | `e4a195a` | Merge pull request #4 from christopheryeo/add-bug-log                      |
| V0.1.8   | `4e77e5d` | Added bug-log.md for tracking bugs                                         |
| V0.1.7   | `a720270` | Merge pull request #3 from christopheryeo/update-readme                    |
| V0.1.6   | `56a0f4e` | Appended 'This is my Jules' to README.md                                   |
| V0.1.5   | `46981f8` | Merge pull request #2 from christopheryeo/docs-enhance-pm-guide            |
| V0.1.4   | `7a29c2d` | Enhanced product_management.md with detailed plan structure               |
| V0.1.3   | `245b6c7` | Merge pull request #1 from christopheryeo/update-readme-documentation      |
| V0.1.2   | `27c7560` | Updated README.md to document content directory                           |
| V0.1.1   | `a4dd21b` | Updated project management and documentation                              |
| V0.1.0   | `c9fb87e` | Created minimal index.html with basic styling                             |
| V0.0.11  | `2e4c362` | Added simple test presentation                                            |
| V0.0.10  | `8e6ddfa` | Replaced with minimal working presentation                                |
| V0.0.9   | `3c35438` | Added test.html for GitHub Pages verification                             |
| V0.0.8   | `ad5bf43` | Simplified and cleaned up presentation structure                          |
| V0.0.7   | `9360b55` | Refactored to use inline CSS/JS for better GitHub Pages compatibility     |
| V0.0.6   | `7395be9` | Fixed paths for GitHub Pages deployment                                   |
| V0.0.5   | `8eeb1f8` | Fixed resource paths for GitHub Pages deployment                          |
| V0.0.4   | `3ce15a5` | Added GitHub Pages deployment workflow                                    |
| V0.0.3   | `7694459` | Initial file upload                                                       |
| V0.0.2   | `063a1f4` | Created static.yml for GitHub Pages                                       |
| V0.0.1   | `c6e89f8` | Initial commit: Set up project structure and documentation                |

## 🔜 Upcoming Versions

| Version | Status      | Target Date | Key Deliverables (Slides)               |
|---------|-------------|-------------|-----------------------------------------|
| V0.2.2  | Planned     | 2025-05-26  | **4-7**: Company, Product, GTM          |
| V0.2.3  | Completed   | 2025-06-02  | **8-10**: Financials, Team              |

For the complete roadmap and detailed planning, see our [Feature Ideas and Roadmap](plans/0_backlog/feature-ideas.md).

[View detailed planning →](plans/1_planning/V1.2.0/) |

---

Created with ❤️ by Sentient.io Team
