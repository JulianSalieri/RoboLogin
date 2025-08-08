from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def create_driver(browser_name="chrome", headless=False):
    """
    Создает и настраивает WebDriver под указанный браузер.

    :param browser_name: 'chrome' или 'firefox'
    :param headless: запуск без UI (True/False)
    """
    browser_name = browser_name.lower()

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Browser '{browser_name}' is not supported. Use 'chrome' or 'firefox'.")

    return driver
