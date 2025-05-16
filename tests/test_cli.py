from typer.testing import CliRunner
from main import app
import pytest
import requests

runner = CliRunner()

def test_hello():
    result = runner.invoke(app, ["hello", "Alim"])
    assert result.exit_code == 0
    assert "Hello Alim!" in result.stdout


def test_weather_success(monkeypatch):
    # готовим фиктивный ответ
    fake_data = {
        "city": "Testville",
        "temperature": 12.3,
        "condition": "Cloudy",
    }

    monkeypatch.setattr("main.get_weather", lambda city: fake_data)

    result = runner.invoke(app, ["weather", "Testville"])
    assert result.exit_code == 0

    assert "Город: Testville" in result.stdout
    assert "Температура: 12.3°C" in result.stdout
    assert "Состояние: Cloudy" in result.stdout


def test_weather_http_error(monkeypatch):
    def fake_raise(city):
        raise requests.exceptions.HTTPError("404 Not Found")

    monkeypatch.setattr("main.get_weather", fake_raise)
    result = runner.invoke(app, ["weather", "Nocity"])
    assert result.exit_code == 1
    assert "Ошибка HTTP: 404 Not Found" in result.stdout


def test_weather_str_error(monkeypatch):
    monkeypatch.setattr("main.get_weather", lambda city: "City not found")
    result = runner.invoke(app, ["weather", "Nowhere"])
    assert result.exit_code == 1
    assert "City not found" in result.stdout