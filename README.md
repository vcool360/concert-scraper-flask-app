# Concert Scraper Flask App

## Overview

This small project is a fun exploration into web scraping that I made using Flask. The application allows users to scrape concert data, including city, date, and price, from a dummy site that I created for demonstration purposes. Additionally, users can subscribe to receive daily email updates on concert prices for cities they are interested in.

## Features

- **Interactive Scraping**: Users can select which pieces of concert data to scrape (city, date, price) through a simple web interface.
- **Email Notifications**: Provides functionality for users to subscribe to daily price alerts for their chosen city.

## Technologies

- **Flask**: A lightweight Python web framework used to build the application.
- **BeautifulSoup**: For parsing HTML and extracting data.
- **Flask-Mail**: To handle outgoing email notifications.
- **APScheduler**: For scheduling daily notification jobs.

## Setup

### Prerequisites

You should have Python 3 and pip installed on your system. This project uses virtual environments for dependency management.

### Installation

1. **Clone the Project**:
   ```bash
   git clone https://github.com/your-username/concert-scraper-flask-app.git
   cd concert-scraper-flask-app
