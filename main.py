import sys
import json
import os
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QMessageBox
from PyQt5.QtGui import QIcon
from assests.main_ui import Ui_MainWindow
import requests




class WeatherApp(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Set window icon
        self.setWindowIcon(QIcon(os.getcwd()+'assests\\cloudy.png'))
        self.setWindowTitle("Weather App by V")
        self.tableWidget.setVisible(False)
        self.setFixedSize(700,250)
        self.getWeatherPushButton.clicked.connect(self.get_weather)
    

    def show_error_popup(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)  # Error icon
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def capitalize_first_letter(self,word):
        if not word:  # Check if the word is empty or None
            return word
        return word[0].upper() + word[1:] if word[0].islower() else word

    def load_api_key(self):
        # Load the API key from config.json
        print(os.getcwd()+'\\assests\\cloudy.png')
        try:
            with open(os.getcwd()+"\\assests\\config.json", "r") as config_file:
                config = json.load(config_file)
                self.api_key = config.get("api_key")
                if not self.api_key:
                    raise ValueError("API key is missing in config.json.")
                else:
                    return self.api_key
        except FileNotFoundError:
            self.show_error_popup("Error", "config.json file not found. Please ensure it exists in the same directory as the script.")
        except json.JSONDecodeError:
            self.show_error_popup("Error", "config.json file is not a valid JSON.")
        except ValueError as e:
            self.show_error_popup("Error", str(e))

    def get_weather(self):
        city = self.capitalize_first_letter(self.cityData.text())
        api_key=self.load_api_key()
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
            
            try:
                response = requests.get(url)
                data = response.json()

                if data['cod'] == '200':  # Successful API response
                    self.update_table(data)
                else:
                    self.show_error_popup("Input Error","City not found.")
            except requests.exceptions.RequestException:
                self.show_error_popup("Internet Error","Error Fetching the Data")

    def update_table(self, data):
        self.tableWidget.setVisible(True)
        self.setFixedSize(770,652)
        # Get the forecast data (we use 4 time slots: 00:00, 06:00, 12:00, 18:00)
        weather_list = data['list']
        #print(weather_list)
        self.tableWidget.setColumnCount(5)  # We have 5 days of data
        # Automatically adjust the row heights based on content
        

        # Set column headers (dates)
        dates = []
        for i in range(5):
            date = weather_list[i * 8]['dt_txt'].split(" ")[0]  # Extract the date from the forecast
            dates.append(date)
        self.tableWidget.setHorizontalHeaderLabels(dates)

        # Iterate through the forecast data and fill the table
        for row in range(4):  # Iterate through time slots
            for col in range(5):  # Iterate through the 5 days
                # Find the corresponding weather data for this time slot and day
                for entry in weather_list:
                    time = entry['dt_txt']
                    date = time.split(" ")[0]  # Extract the date
                    time_slot = time.split(" ")[1]  # Extract the time (00:00, 06:00, etc.)
                    print(time_slot,self.tableWidget.verticalHeaderItem(row).text())
                    
                    if time_slot == self.tableWidget.verticalHeaderItem(row).text() and date == self.tableWidget.horizontalHeaderItem(col).text():
                        print(True)
                        temp = entry['main']['temp']
                        description = entry['weather'][0]['description']
                        weather_info = f"{temp}°C"+"\n"+f"{description.capitalize()}"
                        print(weather_info)
                        self.tableWidget.setItem(row, col, QTableWidgetItem(weather_info))
                        break  # Stop searching once the correct time and date are found
        self.tableWidget.resizeRowsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
