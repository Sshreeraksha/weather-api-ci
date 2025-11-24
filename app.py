from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to generate weather description
def get_description(temp):
    t = int(temp)
    if t < 15:
        return "Cold and Breezy"
    elif t < 25:
        return "Pleasant Weather"
    else:
        return "Hot and Sunny"

@app.route('/weather')
def weather_api():
    city = request.args.get("city")
    
    if not city:
        return jsonify({"error": "City parameter is missing!"}), 400

    temperature = "25"
    humidity = "60%"
    wind = "12 km/h"
    description = get_description(temperature)

    return jsonify({
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind,
        "description": description,
        "status": "success"
    })

@app.route('/weather-json')
def weather_json_pretty():
    city = request.args.get("city")
    if not city:
        city = "Unknown"

    temperature = "25"
    humidity = "60%"
    wind = "12 km/h"
    description = get_description(temperature)

    return jsonify({
        "weather_report": {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind,
            "description": description
        }
    })

@app.route('/weather-ui')
def weather_ui():
    city = request.args.get("city", "Unknown")
    temperature = "25"
    humidity = "60%"
    wind = "12 km/h"
    description = get_description(temperature)

    return f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial;
                    background: #f3f4f6;
                    padding: 20px;
                }}
                .card {{
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    width: 300px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }}
                h1 {{
                    color: #2a2a2a;
                }}
            </style>
        </head>

        <body>
            <div class="card">
                <h1>Weather Report</h1>
                <p><b>City:</b> {city}</p>
                <p><b>Temperature:</b> {temperature}°C</p>
                <p><b>Humidity:</b> {humidity}</p>
                <p><b>Wind Speed:</b> {wind}</p>
                <p><b>Description:</b> {description}</p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
