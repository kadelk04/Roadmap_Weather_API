from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import requests
import redis
import json
from urllib.parse import quote

app = Flask(__name__)
CORS(app)

# connect to Redis
redis_connection = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route('/weather', methods=['GET'])
def get_weather():
  city = request.args.get('city', '')
  return check_redis(city)

def check_redis(city):
    print("Checking Redis for city:", city)

    # Check if the city key exists in Redis
    cached_data = redis_connection.get(city)
    if cached_data is not None:
        print("Found in Redis:", cached_data)
        return json.loads(cached_data)
    else:
        # Key not found, adding to Redis with a test value
        print(f"City '{city}' not found in Redis. Adding it with value 'test'.")
        
        encoded_city = quote(city)
        api_key = os.getenv('YOUR_API_KEY')
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{encoded_city}?unitGroup=metric&key={api_key}&contentType=json"
        response = requests.get(url)
        if response.status_code == 200:
          # API call was successful
          data = response.json()  # Parse the JSON response
          print("This is the data")
          print(data)
          redis_connection.set(city, json.dumps(data))
          return data
        else:
          # API call failed
            print(f"Error {response.status_code}: {response.text}")
        return None
    
        

if __name__ == '__main__':
  app.run(debug=True)