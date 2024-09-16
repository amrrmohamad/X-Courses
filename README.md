<h1>🌤 X Weather - Daily Weather Forecast Website</h1>

X Weather is a modern, responsive weather forecast website that provides users with real-time weather updates, weekly and hourly forecasts, and top city forecasts. The website is designed with a sleek and minimal interface to offer an excellent user experience. Users can also subscribe to receive regular weather updates via email.

## 🌐 Live Demo

[Insert your website's URL here]

## 📜 Features

Current Weather Display: Shows real-time weather data such as temperature, humidity, wind speed, and rain probability.
Weekly Weather Forecast: Provides a 7-day weather outlook.
Hourly Weather Update: Displays weather conditions for specific hours of the day (e.g., sunrise, sunset).
Top City Forecast: Users can view quick weather reports for major cities across the world.
Recent Searches: A section where users can quickly revisit their last searched cities.
Weather News: Get the latest updates and news related to weather conditions globally.
Newsletter Subscription: Users can subscribe to receive weather updates via email.
Responsive Design: Fully functional on both mobile and desktop platforms.

## 🛠 Tech Stack

1. **Frontend:**
    - HTML5
    - CSS3 (Bootstrap or Custom CSS)
    - JavaScript (jQuery dynamic UI)

2. **Backend:**
    - Flask (Python)

3. **APIs:**
    - OpenWeatherMap or WeatherAPI for fetching real-time weather data.

4. **Database (Optional):**
    - PostgreSQL or MySQL for storing user data (e.g., newslette subscriptions).

## 🖥️ Installation Instructions

Step 1: Clone the Repository

```bash
    git clone https://github.com/yourusername/X-weather.git
    cd X-weather
```

Step 2: Install Dependencies
    For Python (Flask) backend:

```bash
    pip install -r requirements.txt
```

Step 3: API Setup
    Sign up for an API key from OpenWeatherMap or WeatherAPI.
    Create a .env file at the root of your project and add your API key:

```bash
    API_KEY=your_api_key_here
```

Step 4: Run the Application
    For Flask (Python):

```bash
    flask run
```

Step 5: Access the Website
    Open your browser and go to <a herf="http://localhost:5000">run-server</a> (Flask).

## 🚀 Features in Detail

Current Weather: Fetches and displays weather data for a selected city or the user’s current location.
Weekly Forecast: Displays a 7-day weather forecast, showing min and max temperatures and weather icons.
Hourly Weather: Provides detailed weather forecasts for different times of the day.
Search History: Stores and displays the user’s recent search results.
Top City Forecast: Quick weather summaries for popular cities worldwide, using country flags as visual aids.
Weather News Section: Features weather-related news articles with thumbnail images and links to full content.
Newsletter Subscription: Users can sign up to receive periodic weather updates directly in their inbox.

## 📦 Folder Structure

```bash
    X-weather/
    |
    ├── static/
    |   |── css/
    |   |    ├── style.css
    |   |    ├── login.css
    |   |    └── signup.css
    |   ├── js/
    |   |    └── script.js
    |   └── images/
    |
    ├── templates/
    |   ├── login.html
    |   ├── signup.html
    |   └── index.html
    |
    ├── app.py
    ├── database.py (if using a database)
    ├── README.md
    └── requirements.txt (or package.json)
```

## 📧 Newsletter Subscription

The website offers a feature where users can subscribe to daily weather updates via email. You can implement this by integrating a service like MailChimp or sending emails through your backend server using Python’s smtplib or Node’s nodemailer.

## 📝 License

This project is licensed under the MIT License.

## 👥 Author

1. ** Amr Mohamad Bakr.
2. ** Yousef Hany Mohamed.
3. ** Abdelrahman Deyaa.
4. ** add author here.
5. ** add author here.
