import pytest
import os
from dotenv import load_dotenv
from utils.browser import create_driver
from ui_components.login.page import LoginPage
from ui_components.trading.page import TradingPage

# Загружаем переменные окружения из .env
load_dotenv()


def pytest_addoption(parser):
    """
    Добавляет кастомные опции командной строки для pytest:
    --browser  : указывает браузер (chrome или firefox)
    --headless : флаг для запуска в headless-режиме
    """
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome | firefox")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run headless mode")


@pytest.fixture
def browser_name(request, _pytest_bdd_example):
    """
    Определяет, в каком браузере запустить тест

    1) Если тест — Scenario Outline (BDD), читает значение из колонки Examples (поле `browser`)
       _pytest_bdd_example = {"browser": "chrome", ...}
    2) Иначе берёт CLI-параметр --browser
    """
    try:
        val = _pytest_bdd_example.get("browser")
        if val:
            return str(val).lower()
    except Exception:
        pass
    return request.config.getoption("--browser").lower()


@pytest.fixture
def driver(request, browser_name):
    """
    Создаёт экземпляр WebDriver для указанного браузера.

    :param browser_name: Имя браузера (chrome или firefox)
    :param headless:    True — без UI, False — с UI
    """
    headless = request.config.getoption("--headless")
    drv = create_driver(browser_name, headless)
    yield drv
    drv.quit()


@pytest.fixture
def login_page(driver):
    """
    Возвращает объект страницы логина (LoginPage) для взаимодействия с UI
    """
    return LoginPage(driver)


@pytest.fixture
def trading_page(driver):
    """
    Возвращает объект страницы торгов (TradingPage) для взаимодействия с UI.
    """
    return TradingPage(driver)


@pytest.fixture
def auth_data():
    """
    Загружает данные авторизации из .env:
    - email        — логин пользователя
    - password     — пароль
    - base_url     — базовый URL тестируемого приложения
    - login_path   — относительный путь (маршрут) к странице логина
    - trading_url  — путь к странице торгов

    Включает проверки, чтобы тесты не запустились с пустыми учётными данными
    """
    data = {
        "email": os.getenv("LOGIN_EMAIL", ""),
        "password": os.getenv("LOGIN_PASSWORD", ""),
        "base_url": os.getenv("BASE_URL", "https://stockstrader.roboforex.com"),
        "login_path": os.getenv("LOGIN_PATH", "/login"),
        "trading_url": os.getenv("TRADING_URL", "https://stockstrader.roboforex.com/trading"),
    }

    # Проверяем, что логин и пароль заданы в .env
    assert data["email"], "LOGIN_EMAIL is empty. Set it in .env"
    assert data["password"], "LOGIN_PASSWORD is empty. Set it in .env"

    return data
