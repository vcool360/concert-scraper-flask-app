# Concert Scraper Flask App

## Project Overview

This Flask application allows users to scrape concert information, such as city, date, and price, from a locally hosted dummy website. Users can select the type of information they want to scrape via a web interface. Additionally, the app features a subscription form where users can sign up to receive daily email updates on concert prices for their city of choice.

## Key Features

- **Data Scraping**: Extract specific concert information (city, date, price) from a predefined webpage.
- **User Interactivity**: Web interface allows users to choose what concert data to scrape.
- **Email Subscription**: Users can subscribe to daily price updates for concerts in a specific city.

## Technologies Used

- **Flask**: Web framework used to create the application.
- **BeautifulSoup**: Library for parsing HTML and extracting data.
- **Flask-Mail**: Extension for sending emails from the Flask app.
- **APScheduler**: Used to schedule daily email notifications.

## Getting Started

### Prerequisites

Ensure you have Python 3 and pip installed on your system. This project uses virtual environments to manage dependencies.

### Setting Up the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/concert-scraper-flask-app.git
   cd concert-scraper-flask-app
