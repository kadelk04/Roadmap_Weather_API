from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
import requests
import redis
import json
from urllib.parse import quote

app = Flask(__name__)
CORS(app)
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

redis_url = os.getenv('REDIS_CONNECTION_STRING')
if not redis_url:
    raise ValueError("Environment variable 'REDIS_CONNECTION_STRING' is not set.")
# checking redis connection
try:
    redis_connection = redis.Redis.from_url(redis_url, decode_responses=True)
    redis_connection.ping()  
except redis.ConnectionError as e:
    raise ConnectionError("Failed to connect to Redis. Check your connection string.") from e

api_key = os.getenv('YOUR_API_KEY')
if not api_key:
    raise ValueError("Environment variable 'YOUR_API_KEY' is not set.")


@app.route('/weather', methods=['GET'])
def get_weather():
  city = request.args.get('city', '')
  if not city:
    return jsonify({"error": "City parameter is required"}), 400
  return check_redis(city)

def check_redis(city):
  print("Checking Redis for city:", city)

  # Check if the city key exists in Redis
  try:
    cached_data = redis_connection.get(city)
  except redis.RedisError as e:
    return jsonify({"error": "Redis operation failed"}), 500
  if cached_data is not None:
      try:
         return json.loads(cached_data)
      except json.JSONDecodeError:
         return jsonify({"error": "Cached data is corrupted"}), 500
  else:
       # Key not found, adding to Redis with a test value
      print(f"City '{city}' not found in Redis. Adding it with value 'test'.")
        
      encoded_city = quote(city)
      url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{encoded_city}?unitGroup=metric&key={api_key}&contentType=json"
      try:
        response = requests.get(url)
        response.raise_for_status()
      except requests.exceptions.RequestException as e:
          return jsonify({"error": f"Failed to fetch weather data: {str(e)}"}), 502
      try:
        data = response.json()  # Parse the JSON response
      except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse API response"}), 502
      print("This is the data")
      print(data)
      redis_connection.set(city, json.dumps(data))
      return data
      
          
        

if __name__ == '__main__':
  app.run(debug=True)