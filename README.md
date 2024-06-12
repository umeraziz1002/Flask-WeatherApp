# Flask Weather App

Welcome to the Flask Weather App! This application allows users to check the current weather conditions for a specified location. It leverages Flask as the web framework and integrates with a weather API to fetch real-time weather data.

## Features

- **Current Weather Information:** Get real-time weather updates including temperature, humidity, and weather conditions.
- **Search by Location:** Users can search for weather updates by entering a city name.
- **Responsive Design:** The app is designed to work on both desktop and mobile devices.

## Requirements

Before running the Flask Weather App, ensure you have the following installed:

- Python 3.x
- Flask
- Requests library

You can install the required libraries using the following command:

```bash
pip install flask requests
```

## Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/umeraziz1002/Flask-WeatherApp.git
   cd flask-weather-app
   ```

2. **Install Dependencies:**

   Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Get an API Key:**

   Sign up for an account on [OpenWeatherMap](https://openweathermap.org/) and get an API key. 

4. **Configure the Application:**

   Add your API key:


## Running the Application

To start the Flask development server, run the following command:

```bash
flask run
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Enter the name of a city in the search bar and submit.
3. The app will display the current weather information for the specified city.

## Project Structure

The project files are organized as follows:

```
flask-weather-app/
├── app.py
├── templates/
│   ├── index.html
│   └── weather.html
├── static/
│   └── styles.css
├── .gitignore
└── README.md
```

- **app.py:** The main Flask application file.
- **templates/:** Contains HTML templates for the app.
- **static/:** Contains static files such as CSS.
- **.env:** Environment file to store API keys and other sensitive data.
- **.gitignore:** Specifies files and directories to be ignored by git.
- **README.md:** Project documentation.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [OpenWeatherMap](https://openweathermap.org/)

Thank you for using the Flask Weather App!
