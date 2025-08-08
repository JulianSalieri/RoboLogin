from selenium.webdriver.common.by import By


class LoginLocators:
    # Элемент для ввода текста в поле email
    EMAIL_INPUT = (By.ID, "ion-input-0")

    # Видимый элемент для активации поля email
    EMAIL_CLICK = (By.ID, "email")

    # Видимый элемент для активации поля password
    PASSWORD_CLICK = (By.ID, "password")

    # Элемент для ввода текста пароля
    PASSWORD_INPUT = (By.ID, "ion-input-1")

    # Кнопка Продолжить
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='button']")

    # Блокирующая модалка «нет соединения» (в Firefox иногда всплывает и перекрывает кнопку)
    NO_CONNECTIVITY_MODAL = (By.CSS_SELECTOR, "ion-modal#no-connectivity-modal.show-modal")

