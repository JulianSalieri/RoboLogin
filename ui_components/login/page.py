from ui_components.base_page import BasePage
from .locators import LoginLocators as L


class LoginPage(BasePage):
    def login(self, email, password):
        """
        Выполняет авторизацию на странице входа

        :param email: адрес электронной почты пользователя
        :param password: пароль пользователя
        """
        # Ждем появления поля email
        self.wait_for_invisible(L.NO_CONNECTIVITY_MODAL)
        self.wait_for_visible(L.EMAIL_CLICK)

        # Вводим email и пароль
        self.wait_for_invisible(L.NO_CONNECTIVITY_MODAL)
        self.send_keys(L.EMAIL_INPUT, email)
        self.send_keys(L.PASSWORD_INPUT, password)

        # Ждем пока кнопка "Продолжить" станет кликабельной
        self.wait_for_clickable(L.LOGIN_BUTTON)

        # Кликаем по кнопке входа
        self.click(L.LOGIN_BUTTON)
