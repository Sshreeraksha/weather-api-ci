from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def fetch_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    current = data['current_condition'][0]
    astronomy = data['weather'][0]['astronomy'][0]
    return current, astronomy

@app.route('/weather')
def get_weather_json():
    city = request.args.get("city", "London")
    current, astronomy = fetch_weather(city)
    return jsonify({
        "city": city,
        "temperature": current["temp_C"],
        "humidity": current["humidity"],
        "feels_like": current["FeelsLikeC"],
        "wind_speed": current["windspeedKmph"],
        "description": current["weatherDesc"][0]["value"],
        "sunrise": astronomy["sunrise"],
        "sunset": astronomy["sunset"]
    })

@app.route('/weather-ui')
def get_weather_ui():
    city = request.args.get("city", "London")
    current, astronomy = fetch_weather(city)

    icon = current["weatherDesc"][0]["value"]
    temp = current["temp_C"]
    humidity = current["humidity"]
    feels = current["FeelsLikeC"]
    wind = current["windspeedKmph"]
    sunrise = astronomy["sunrise"]
    sunset = astronomy["sunset"]

    html = f"""
    <html>
    <head>
    <title>Weather for {city}</title>
    <style>
        body {{
            background: linear-gradient(135deg, #6dd5fa, #2980b9);
            font-family: Arial, sans-serif;
            color: white;
            text-align: center;
            padding-top: 40px;
        }}
        .card {{
            background: rgba(255,255,255,0.12);
            padding: 25px;
            border-radius: 20px;
            width: 420px;
            margin: auto;
            box-shadow: 0px 6px 18px rgba(0,0,0,0.25);
        }}
        h1 {{ font-size: 28px; margin-bottom: 6px; }}
        p  {{ font-size: 18px; margin: 6px 0; }}
    </style>
    </head>
    <body>
    <div class="card">
        <h1>🌤 Weather in {city}</h1>
        <p><b>Description:</b> {icon}</p>
        <p><b>Temperature:</b> {temp}°C</p>
        <p><b>Humidity:</b> {humidity}%</p>
        <p><b>Feels Like:</b> {feels}°C</p>
        <p><b>Wind Speed:</b> {wind} km/h</p>
        <p><b>Sunrise:</b> {sunrise}</p>
        <p><b>Sunset:</b> {sunset}</p>
    </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
