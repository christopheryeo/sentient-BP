// Slide data - array of slide objects
const slidesData = [
    // Title Slide
    {
        title: "Sentient.io - Naturally Intelligent",
        content: `
            <div class="icon">🤖</div>
            <h1>Sentient.io</h1>
            <h2>Naturally Intelligent</h2>
            <p>AI-Powered Solutions for the Modern Enterprise</p>
        `
    },
    {
        title: "About Sentient.io",
        content: `
            <div class="slide-content company-facts-slide" id="company-facts">
              <h2>About Sentient.io</h2>
              <div class="facts-container">
                <div class="fact-item logo-item">
                  <img src="/static/images/sentient-logo.png" alt="Sentient.io Logo" class="company-logo-facts-slide">
                </div>
                <div class="fact-item">
                  <span class="fact-label">Founded:</span>
                  <span class="fact-value">May 2017</span>
                </div>
                <div class="fact-item">
                  <span class="fact-label">Headquarters:</span>
                  <span class="fact-value">Singapore <img src="/static/images/Singapore.png" alt="Singapore" class="inline-flag-image"></span>
                </div>
                <div class="fact-item">
                  <span class="fact-label">Founder & CEO:</span>
                  <span class="fact-value">Christopher Yeo</span>
                </div>
                <div class="fact-item">
                  <span class="fact-label">Team Size:</span>
                  <span class="fact-value">15+ professionals</span>
                </div>
                <!-- Placeholder for other key statistics or achievements -->
                <div class="fact-item full-width">
                  <p>Pioneering AI solutions to empower businesses globally.</p>
                </div>
              </div>
            </div>
        `
    }
    // Add more slides here following the same pattern
    // Example:
    // {
    //     title: "Slide Title",
    //     content: "<p>Slide content here</p>"
    // }
];

// DOM Elements
const slideDeck = document.getElementById('slide-deck');
const prevButton = document.getElementById('prev-slide');
const nextButton = document.getElementById('next-slide');
const slideCounter = document.getElementById('slide-counter');

// State
let currentSlideIndex = 0;

// Initialize the presentation
function initPresentation() {
    // Create slides from data
    slidesData.forEach((slide, index) => {
        const slideElement = document.createElement('div');
        slideElement.className = 'slide';
        if (index === 0) slideElement.classList.add('active');
        
        slideElement.innerHTML = `
            <h2>${slide.title}</h2>
            <div class="slide-content">
                ${slide.content}
            </div>
        `;
        
        slideDeck.appendChild(slideElement);
    });

    updateNavigation();
    updateSlideCounter();
}

// Update navigation buttons state
function updateNavigation() {
    prevButton.disabled = currentSlideIndex === 0;
    nextButton.disabled = currentSlideIndex === slidesData.length - 1;
}

// Update slide counter
function updateSlideCounter() {
    slideCounter.textContent = `${currentSlideIndex + 1} / ${slidesData.length}`;
}

// Go to specific slide
function goToSlide(index) {
    // Validate index
    if (index < 0 || index >= slidesData.length) return;
    
    const currentSlide = document.querySelector('.slide.active');
    const nextSlide = document.querySelectorAll('.slide')[index];
    
    if (currentSlide && nextSlide) {
        // Add exit animation
        currentSlide.classList.add('exiting');
        
        // After animation completes, update active states
        setTimeout(() => {
            currentSlide.classList.remove('active', 'exiting');
            nextSlide.classList.add('active');
            currentSlideIndex = index;
            updateNavigation();
            updateSlideCounter();
            
            // Call any slide-specific initialization
            if (slidesData[currentSlideIndex].init) {
                slidesData[currentSlideIndex].init();
            }
        }, 500);
    }
}

// Event Listeners
prevButton.addEventListener('click', () => {
    if (currentSlideIndex > 0) {
        goToSlide(currentSlideIndex - 1);
    }
});

nextButton.addEventListener('click', () => {
    if (currentSlideIndex < slidesData.length - 1) {
        goToSlide(currentSlideIndex + 1);
    }
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft' && currentSlideIndex > 0) {
        goToSlide(currentSlideIndex - 1);
    } else if (e.key === 'ArrowRight' && currentSlideIndex < slidesData.length - 1) {
        goToSlide(currentSlideIndex + 1);
    }
});

// Touch events for mobile
let touchStartX = 0;
let touchEndX = 0;

slideDeck.addEventListener('touchstart', (e) => {
    touchStartX = e.touches[0].clientX;
}, false);

slideDeck.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].clientX;
    handleSwipe();
}, false);

function handleSwipe() {
    const swipeThreshold = 50; // Minimum distance for a swipe
    const swipeDistance = touchStartX - touchEndX;
    
    if (Math.abs(swipeDistance) > swipeThreshold) {
        if (swipeDistance > 0 && currentSlideIndex < slidesData.length - 1) {
            // Swipe left - next slide
            goToSlide(currentSlideIndex + 1);
        } else if (swipeDistance < 0 && currentSlideIndex > 0) {
            // Swipe right - previous slide
            goToSlide(currentSlideIndex - 1);
        }
    }
}

// Initialize the presentation when the DOM is loaded
document.addEventListener('DOMContentLoaded', initPresentation);
