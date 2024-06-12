from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    weather_data = None
    city = 'haripur'
    api_key = 'cff61a6daf8f4826e621a86fa6f11181'  # Replace with your OpenWeather API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
    else:
        weather_data = {'error': 'City not found'}
    return render_template('home.html', weather_data=weather_data)


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'cff61a6daf8f4826e621a86fa6f11181'  # Replace with your OpenWeather API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found'}
    return render_template('home.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)