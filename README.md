# Weather App 🌤️
Link to Download Exe :- https://github.com/vaibhav88614/Weather_App/releases/download/WeatherApp/main.exe


![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python&logoColor=white)  
![PyQt5](https://img.shields.io/badge/Qt-PyQt5-green?style=flat&logo=qt&logoColor=white)

A desktop weather application built with **PyQt5**, designed to provide real-time weather forecasts for any city worldwide. The app offers a user-friendly interface, efficient data retrieval, and tabular weather representation. It is packaged as a standalone `.exe` file for easy usage.

---

## Features

- **Real-time Weather Data**: Fetches accurate weather forecasts using a public API.
- **Responsive UI**: Built with PyQt5 for an intuitive and visually appealing interface.
- **Error Handling**: Displays error messages for invalid city inputs or API issues.
- **Tabular Display**: Weather details, including date, temperature, and descriptions, are displayed in a neat table format.
- **Standalone Executable**: No additional installations required to run the app.

---

## Screenshots

> *Add screenshots here to showcase your app’s interface and functionality.*

---

## Requirements

To run or develop the project, ensure you have the following installed:

- **Python 3.11 or later**
- **Libraries**:
  - PyQt5
  - Requests

To install the required libraries, run:
```bash
pip install -r requirements.txt
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd weather-app
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

Alternatively, download the pre-packaged `.exe` file and run it directly.

---

## How It Works

1. **Input**: Enter the name of the city whose weather you want to view.
2. **Fetch Data**: The app sends a request to a weather API to retrieve real-time data.
3. **Display**: Weather data is displayed in a table format, showing the following:
   - **Date**: The specific date for the forecast.
   - **Temperature**: The predicted temperature for the day.
   - **Description**: A brief description of the weather (e.g., cloudy, sunny).
4. **Error Handling**: If the city is invalid or the API fails to fetch data, an error popup is displayed.

---

## File Structure

```
weather-app/
|-- main.py               # Main application file
|-- assets/
|   |-- cloudy.ico        # Application icon
|   |-- cloudy.png        # UI asset
|   |-- config.json       # API key and configuration
|-- requirements.txt      # Required libraries
|-- README.md             # Project documentation
```

---

## API Integration

The app uses a third-party weather API to fetch data. Ensure your `config.json` contains the API key:
```json
{
  "api_key": "your_api_key_here"
}
```
Replace `your_api_key_here` with your API key.

---

## Contribution

Contributions are welcome! If you want to enhance the app or fix bugs:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your fork and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) for the GUI framework.
- [OpenWeatherMap](https://openweathermap.org/) for the weather API.

---

## Author

**Your Name**  
GitHub: [yourusername](https://github.com/yourusername)

