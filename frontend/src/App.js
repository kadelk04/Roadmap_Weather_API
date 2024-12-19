import './App.css';

import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [city, setCity] = useState('');
    const [weather, setWeather] = useState(null);

    const getWeather = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/weather?city=${city}`);
            setWeather(response.data);

            console.log(weather)
        } catch (error) {
            console.error("Error fetching weather data:", error);
        }
    };

    const convertToF = (celsius) => {
        return (celsius * 9/5) + 32;
    }

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Weather App</h1>
            <input 
                type="text" 
                placeholder="Enter city" 
                value={city} 
                onChange={(e) => setCity(e.target.value)} 
            />
            <button onClick={getWeather}>Get Weather</button>
            {weather && (
                <p>Temperature: {convertToF(weather.currentConditions.feelslike)}°C, Condition: {weather.currentConditions.conditions}</p>
            )}
        </div>
    );
}

export default App;
