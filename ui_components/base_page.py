from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlsplit


class BasePage:
    def __init__(self, driver, timeout=10):
        """
        Базовый класс для всех PageObject.

        :param driver: WebDriver — экземпляр браузера.
        :param timeout: Максимальное время ожидания (по умолчанию 10 секунд).
        """
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        """
        Ищет один элемент на странице.

        :param locator: локатор в формате (By, value).
        :return: найденный WebElement.
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """
        Ищет несколько элементов на странице.

        :param locator: локатор в формате (By, value).
        :return: список найденных WebElement.
        """
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """
        Ожидает кликабельность и кликает по элементу.

        :param locator: локатор в формате (By, value).
        """
        self.wait_for_clickable(locator)
        self.find_element(locator).click()

    def send_keys(self, locator, text, clear=True):
        """
        Вводит текст в элемент.

        :param locator: локатор в формате (By, value).
        :param text: текст для ввода.
        :param clear: очищать ли поле перед вводом (по умолчанию True).
        """
        elem = self.find_element(locator)
        if clear:
            elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        """
        Получает текст элемента.

        :param locator: локатор в формате (By, value).
        :return: текст элемента.
        """
        return self.find_element(locator).text

    def is_input_enabled(self, locator):
        """
        Проверяет, активно ли поле ввода (доступно для взаимодействия).

        :param locator: локатор в формате (By, value).
        :return: True, если элемент доступен для ввода.
        """
        return self.driver.find_element(*locator).is_enabled()

    # --- URL ожидания ---
    def wait_for_url_contains(self, substring):
        """
        Ждет, пока URL будет содержать указанный текст.

        :param substring: подстрока, которую должен содержать URL.
        """
        WebDriverWait(self.driver, self.timeout).until(EC.url_contains(substring))

    def wait_for_url_endswith(self, suffix):
        """
        Ждет, пока URL будет заканчиваться на указанный суффикс.

        Зачем:
        Используется, когда на одном домене есть похожие пути и важно попасть именно в конец:
        пример — /trading vs /trading/history и убрать все query-параметры

        :param suffix: окончание URL (например, "/trading").
        """

        def _endswith(_):
            cur = self.driver.current_url
            parsed = urlsplit(cur)
            cur_no_q = f"{parsed.scheme}://{parsed.netloc}{parsed.path}".rstrip("/")
            return cur_no_q.endswith(suffix.rstrip("/"))

        WebDriverWait(self.driver, self.timeout).until(_endswith)

    # --- проверки видимости ---
    def is_visible(self, locator):
        """
        Проверяет, виден ли элемент на странице.

        :param locator: локатор в формате (By, value).
        :return: True, если элемент виден; False, если не виден.
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_visible(self, locator):
        """
        Ждет видимость элемента.

        :param locator: локатор в формате (By, value).
        :return: WebElement, если элемент найден и виден.
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_invisible(self, locator):
        """
        Ждет, пока элемент исчезнет со страницы (display:none или удалён из DOM).

        :param locator: локатор в формате (By, value).
        """
        WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    # --- кликабельность ---
    def wait_for_clickable(self, locator):
        """
        Ждет, пока элемент станет кликабельным.

        :param locator: локатор в формате (By, value).
        :return: WebElement, если элемент стал кликабельным.
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def open(self, url):
        """
        Открывает страницу по-указанному URL.

        :param url: Адрес страницы.
        """
        self.driver.get(url)
