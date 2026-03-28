import requests

def get_clima(ciudad: str, api_key: str)-> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": ciudad,
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }
    response=requests.get(url, params=params)
    response.raise_for_status()
    return response.json()