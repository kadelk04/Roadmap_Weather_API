# Roadmap_Weather_API

# https://roadmap.sh/projects/weather-api-wrapper-service

This repository provides a Weather API built with Python, Flask, and OpenWeatherMap. 
This fufills the project requirements for roadmap.sh project 'Weather API'

## Features

- **Location-based Queries:** Input location (city name) to retrieve specific weather data.
- **API Integration:** Uses OpenWeatherMap API for fetching live weather data.

## Setup Instructions

### Prerequisites

- Python 3.x installed
- `pip` for package management
- OpenWeatherMap API key (create an account and get your API key at [OpenWeatherMap](https://openweathermap.org/api))
- Redis database + connection string at [https://redis.io/docs/latest/develop/clients/redis-py/]

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/kadelk04/Roadmap_Weather_API.git
   cd Roadmap_Weather_API
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Unix/Mac
   venv\Scripts\activate     # For Windows
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Create a `.env` file in the root directory.
   - Add your OpenWeatherMap API key:
     ```env
     API_KEY=your_openweathermap_api_key
     ```
  - Add your Redis connection string:
     ```env
     REDIS_CONNECTION_STRING=your_redis_connection_string
     ```

5. Run the application:
   ```bash
   cd frontend
   npm start
   ```

6. Access the Weather API UI at: `http://localhost:3000`

# What I learned
1) Interacting with APIs
2) Building applications using the Flask framework
3) Utilizing Redis for database management and caching
