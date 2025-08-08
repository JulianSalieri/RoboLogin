from selenium.webdriver.common.by import By

class TradingLocators:
    # Иконка лупы в строке поиска на странице торгов
    SEARCH_ICON = (By.ID, "icon_search")

    # Лоадер загрузки после авторизации
    LOADER = (By.CSS_SELECTOR, "[class^='tm-landing']")
