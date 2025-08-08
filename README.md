# Fusion - Startup Website

A modern, responsive startup website for Fusion, specializing in AI, Web Development, Automation, and Backend Solutions.

## Features

- **Modern Design**: Dark theme with gradient accents and smooth animations
- **Responsive**: Mobile-first design that works on all devices
- **Interactive**: Smooth scrolling, form handling, and scroll animations
- **Fast**: Built with FastAPI for optimal performance

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with gradients and animations
- **Fonts**: Google Fonts (Inter)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Open your browser and navigate to `http://localhost:8000`

## Project Structure

```
company website/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css      # Styles
│   └── js/
│       └── script.js      # JavaScript functionality
└── README.md
```

## Sections

- **Hero**: Company tagline with call-to-action buttons
- **Services**: AI Solutions, Web Development, Automation, Backend Systems
- **About**: Mission and vision statements
- **Projects**: Portfolio showcase (FusionStore, Fusion Hub, AI Analytics Suite)
- **Contact**: Contact form with backend integration
- **Footer**: Quick links and social media

## Customization

- Update company information in `templates/index.html`
- Modify colors and styling in `static/css/style.css`
- Add functionality in `static/js/script.js`
- Extend backend routes in `main.py`

## Deployment

The application can be deployed to platforms like:
- Vercel
- Render
- Heroku
- AWS EC2
- DigitalOcean

For production, consider adding:
- Database integration
- Email service for contact form
- SSL certificates
- Environment variables for configuration