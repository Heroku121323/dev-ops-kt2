import requests

WEATHER_API = "349d48b40657499d99b214605251105"
API_URL = "https://api.weatherapi.com/v1/current.json"
NAME_MAP = {
    "Moscow": "Москва",
    "Saint Petersburg": "Санкт-Петербург",
    "Ulyanovsk": "Ульяновск",
}
def get_city_name(city: str) -> str:
    """
    Get the Russian name of the city.
    
    :param city: Name of the city in English.
    :return: Russian name of the city.
    """
    return NAME_MAP.get(city, city)


def get_weather(city: str) -> dict:
    #Добавить обработку ошибок
    """
    Get weather information for a given city.
    
    :param city: Name of the city to get weather information for.
    :return: Weather information as a dictionary.
    """
    params = {
        "key": WEATHER_API,
        "q": city,
        "aqi": "no",
        "lang": "ru"
    }
    
    response = requests.get(url=API_URL, params=params, timeout=5)
    response.raise_for_status()
    json_eng = response.json()
    city_en = json_eng["location"]["name"]
    city_ru = get_city_name(city_en)
    return {
        "city": city_ru,
        "temperature": json_eng['current']['temp_c'],
        "condition": json_eng['current']['condition']['text']
    }



