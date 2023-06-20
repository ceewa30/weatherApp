import requests
from weatherAPI import _get_api_key

API_KEY = _get_api_key()

# https://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}

def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    filtered_data = data["list"]
    # Number of days * 8
    nr_values = 8 * forecast_days
    
    filtered_data = filtered_data[:nr_values]        
    return filtered_data

if __name__=="__main__":
    print(get_data(place="London", forecast_days=3))


