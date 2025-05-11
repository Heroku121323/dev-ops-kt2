import pytest

from scripts.weather import get_weather, get_city_name

def test_get_city_name():
    assert get_city_name("Moscow") == "Москва"
    assert get_city_name("Saint Petersburg") == "Санкт-Петербург"
    assert get_city_name("Ulyanovsk") == "Ульяновск"
    assert get_city_name("Unknown City") == "Unknown City"

def test_get_city_name_unknown():
    assert get_city_name("Paris") == "Paris"

class DummyResponse:
    def __init__(self, status_code, payload):
        self.status_code = status_code
        self._payload = payload

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise Exception(f"HTTP {self.status_code}")

    def json(self):
        return self._payload
    
@pytest.fixture
def fake_weather_response():
    return {
        "location": {"name": "Moscow"},
        "current": {
            "temp_c": 5.5,
            "condition": {"text": "Ясно"}
        }
    }

def test_get_weather_success(monkeypatch, fake_weather_response):
    """Проверяем, что get_weather парсит JSON и переводит город."""
    def fake_get(url, params, timeout):
        # можно проверить, что ключ и город пришли верно:
        assert "key" in params and params["q"] == "Moscow"
        return DummyResponse(200, fake_weather_response)

    monkeypatch.setattr("scripts.weather.requests.get", fake_get)

    result = get_weather("Moscow")
    assert result["city"] == "Москва"
    assert result["temperature"] == 5.5
    assert result["condition"] == "Ясно"


def test_get_weather_http_error(monkeypatch):
    """Если сервер вернёт 4xx/5xx, должен выброситься Exception."""
    def fake_bad_get(url, params, timeout):
        return DummyResponse(404, {})
    monkeypatch.setattr("scripts.weather.requests.get", fake_bad_get)

    with pytest.raises(Exception):
        get_weather("Moscow")