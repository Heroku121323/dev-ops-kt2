#!/usr/bin/env python3
import typer
import requests
from scripts.weather import get_weather

app = typer.Typer()

@app.command()
def weather(
    city: str = typer.Argument( 
        "Moscow",
        help="Город, для которого показать погоду",
    ),
):
    """
    Get the weather for a specific city.
    """
    try:
        data = get_weather(city=city)
    except requests.exceptions.HTTPError as http_err:
        typer.secho(f"Ошибка HTTP: {http_err}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)
    
    if isinstance(data, str):
        typer.secho(data, fg=typer.colors.RED, err=True)
        raise typer.Exit(1)
    
    typer.echo(f"Город: {data['city']}")
    typer.echo(f"Температура: {data['temperature']}°C")
    typer.echo(f"Состояние: {data['condition']}")

@app.command()
def hello(name: str):
    """
    test cli
    """
    typer.echo(f"Hello {name}!")

@app.command()
def hearts():
    """
    print beautiful hearts
    """
    typer.echo("    ❤️       ❤️")
    typer.echo("  ❤️   ❤️   ❤️   ❤️")
    typer.echo(" ❤️      ❤️      ❤️")
    typer.echo(" ❤️             ❤️")
    typer.echo("  ❤️           ❤️")
    typer.echo("    ❤️       ❤️")
    typer.echo("      ❤️   ❤️")
    typer.echo("        ❤️")

if __name__ == "__main__":
    app()
