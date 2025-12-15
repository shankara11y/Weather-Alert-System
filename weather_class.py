from datetime import datetime
from weather_utils import alert_logger


class WeatherStation:
    def __init__(self, city, temperature, humidity, rain_prob):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.rain_prob = rain_prob
        self.alert_status = []

    @alert_logger
    def check_weather(self, thresholds):
        self.alert_status.clear()

        if self.temperature >= thresholds["high_temp"]:
            self.alert_status.append("High Temperature Alert")

        if self.humidity >= thresholds["high_humidity"]:
            self.alert_status.append("High Humidity Warning")

        if self.rain_prob >= thresholds["rain_probability"]:
            self.alert_status.append("Rain Alert")

        return self.alert_status

    def send_alert(self):
        if not self.alert_status:
            print(f"No alerts for {self.city}. Weather is normal.")
        else:
            for alert in self.alert_status:
                print(f"⚠️ {alert} in {self.city}")

    def hourly_forecast(self):
        return (
            f"City: {self.city} | "
            f"Temp: {self.temperature}°C | "
            f"Humidity: {self.humidity}% | "
            f"Rain Probability: {self.rain_prob}%"
        )

    def save_weather_log(self, filename):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(filename, "a") as file:
            file.write(
                f"{timestamp},{self.city},"
                f"{self.temperature},{self.humidity},{self.rain_prob}\n"
            )
