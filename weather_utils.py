import csv
import json
from functools import wraps


# Decorator to log alert triggers
def alert_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        alerts = func(*args, **kwargs)
        if alerts:
            print("[LOG] Alerts triggered:", alerts)
        return alerts
    return wrapper


# Load alert thresholds from JSON file
def load_thresholds(filename):
    with open(filename, "r") as file:
        return json.load(file)


# Validate numerical input
def validate_number(value):
    try:
        return float(value)
    except ValueError:
        return None


# Load previous weather logs (optional use)
def load_weather_logs(filename):
    records = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                records.append(row)
    except FileNotFoundError:
        pass
    return records
