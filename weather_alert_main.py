import matplotlib.pyplot as plt
from weather_class import WeatherStation
from weather_utils import load_thresholds, validate_number


temp_category = lambda t: (
    "Cold" if t < 15 else
    "Normal" if t <= 30 else
    "Hot"
)


def main():
    thresholds = load_thresholds("alert_thresholds.json")

    city = input("Enter city name: ")

    temperature = validate_number(input("Enter temperature (°C): "))
    humidity = validate_number(input("Enter humidity (%): "))
    rain_prob = validate_number(input("Enter rain probability (%): "))

    if None in (temperature, humidity, rain_prob):
        print("❌ Invalid input. Please enter numeric values only.")
        return

    station = WeatherStation(city, temperature, humidity, rain_prob)

    station.check_weather(thresholds)
    station.send_alert()

    print("Weather Category:", temp_category(temperature))

    station.save_weather_log("weather_logs.csv")

    

    temp_trend = [temperature - 2, temperature - 1, temperature]
    humidity_levels = [humidity - 5, humidity]

 
    plt.plot(temp_trend)
    plt.title("Temperature Trend")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.show()

    
    plt.bar(["Morning", "Evening"], humidity_levels)
    plt.title("Humidity Levels")
    plt.ylabel("Humidity (%)")
    plt.show()


if __name__ == "__main__":
    main()
