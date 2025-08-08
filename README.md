# RoboLogin UI Automation Tests

## 📌 Описание проекта
Данный проект — это пример автоматизации UI-тестов с использованием:
- **Python 3.13**
- **Pytest** и **Pytest-BDD**
- **Selenium WebDriver**
- **Dotenv** для конфигураций

Тесты написаны в **BDD-формате** (Gherkin) и покрывают сценарий успешной авторизации с переходом на страницу торгов.

## 📂 Структура проекта
```
.
├── ui_components/        # Page Object классы и локаторы
│   ├── base_page.py
│   ├── login/
│   └── trading/
├── utils/                # Утилиты (создание драйвера и т.д.)
├── tests/                # Тесты и BDD-steps
│   ├── features/
│   └── steps/
├── .env                  # Конфигурация (логин, пароль, урлы)
├── conftest.py           # Фикстуры Pytest
├── requirements.txt      # Зависимости проекта
└── README.md
```

## ⚙️ Установка и запуск
### 1. Клонировать репозиторий
```bash
git clone https://github.com/username/RoboLogin.git
cd RoboLogin
```

### 2. Создать виртуальное окружение
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate   # Windows
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Создать `.env` файл
В корне проекта создайте `.env` и добавьте (тут он будет как показательный):
```
LOGIN_EMAIL=your_email@example.com
LOGIN_PASSWORD=your_password
BASE_URL=https://stockstrader.roboforex.com
LOGIN_PATH=/login
TRADING_URL=https://stockstrader.roboforex.com/trading
```

### 5. Запуск тестов
По умолчанию тесты запускаются c параметрами browser =  chrome and firefox:
```bash
pytest -v
```

#### Запуск в Chrome:
```bash
pytest -v --browser=chrome
```

#### Запуск в headless-режиме:
```bash
pytest -v --headless
```

## 📜 BDD сценарий
Пример `tests/features/login.feature`:
```gherkin
Feature: Login

  Scenario Outline: Successful login on <browser>
    Given I open the login page
    When I login with valid credentials
    Then I am redirected to the Trading page and it is loaded

    Examples:
      | browser  |
      | chrome   |
      | firefox  |
```

## 🏗️ Используемые паттерны
- **Page Object Model (POM)** — изоляция логики работы со страницами
- **BDD** — удобное описание сценариев для заказчиков и тестировщиков

## 📌 Примечания

- Проект легко расширить новыми тестами и страницами.
**А так же:**
Проект легко расширить под:
- параметризацию логинов/паролей
- Allure-репортинг
- CI-пайплайн
- запуск в несколько потоков через **pytest-xdist**
