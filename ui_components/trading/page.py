from ui_components.base_page import BasePage
from .locators import TradingLocators as T


class TradingPage(BasePage):
    def wait_until_opened(self, expected_url):
        """
        Ожидает полной загрузки страницы торгов

        :param expected_url: Ожидаемый адрес страницы,
                             на которую должен произойти переход после авторизации
        """
        # Ждем пока URL изменится и произойдет редирект на страницу торгов
        self.wait_for_url_contains(expected_url)
        self.wait_for_url_endswith("/trading")

        # Ждем исчезновения лоадера
        self.wait_for_invisible(T.LOADER)

        # Ждем когда иконка поиска станет видимой
        self.wait_for_visible(T.SEARCH_ICON)

        return True
