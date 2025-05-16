import pathlib
from setuptools import setup, find_packages

# Путь до директории с setup.py
HERE = pathlib.Path(__file__).parent

# Считываем версию из файла "version"
VERSION = (HERE / "version").read_text(encoding="utf-8").strip()

setup(
    name="ctl-app",
    version=VERSION,
    author="Ваше Имя",
    author_email="you@example.com",
    description="CLI для погоды и других команд",
    long_description=(HERE / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests", "tests.*", ".github"]),
    py_modules=["main"],
    install_requires=[
        "typer[all]>=0.4.0",
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": [
            "ctl=main:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
    ],
    python_requires=">=3.7",
)
