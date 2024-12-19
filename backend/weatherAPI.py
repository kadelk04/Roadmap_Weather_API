from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import requests
from urllib.parse import quote

app = Flask(__name__)

CORS(app)

@app.route('/weather', methods=['GET'])
def get_weather():
  city = request.args.get('city', '')
  encoded_city = quote(city)
  api_key = os.getenv('YOUR_API_KEY')
  url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{encoded_city}?unitGroup=metric&key={api_key}&contentType=json"
  response = requests.get(url)
  if response.status_code == 200:
    # API call was successful
    data = response.json()  # Parse the JSON response
    return jsonify(data)
  else:
    # API call failed
      print(f"Error {response.status_code}: {response.text}")
@app.route('/users', methods=['DELETE'])
def delete_user():
  return jsonify({'result': 'success'})

if __name__ == '__main__':
  app.run()