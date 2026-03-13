from selenium.webdriver.common.by import By
from base_page import BasePage
import allure
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    """Главная страница Aviasales"""

    # Локаторы
    LOGO = (By.CSS_SELECTOR, "[data-test-id='logo-text']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-test-id='form-submit']")
    DESTINATION_INPUT = (By.CSS_SELECTOR, "[data-test-id='destination-input']")

    # Укажите город прибытия:
    ERROR_MESSAGE = (By.XPATH, "//*[text()='Укажите город прибытия']")

    # Кнопка профиля (вместо избранного)
    PROFILE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='profile-button']")

    @allure.step("Открываем главную страницу")
    def open(self):
        """Открыть страницу"""
        self.driver.get("https://www.aviasales.ru")
        self.wait.until(EC.visibility_of_element_located(self.LOGO))
        return self

    @allure.step("Проверяем логотип")
    def logo_visible(self):
        """Проверка видимости логотипа"""
        return self.is_visible(self.LOGO)

    @allure.step("Проверяем кнопку профиля")
    def profile_visible(self):
        """Проверка видимости кнопки профиля"""
        try:
            element = self.find_element(self.PROFILE_BUTTON)
            return element.is_displayed()
        except Exception:
            return False

    @allure.step("Получаем цвет кнопки поиска")
    def button_color(self):
        """Цвет кнопки поиска"""
        return self.get_css(self.SEARCH_BUTTON, "background-color")

    @allure.step("Получаем шрифт")
    def font_family(self):
        """Шрифт на странице"""
        return self.get_css(self.LOGO, "font-family")

    @allure.step("Проверяем наличие сообщения об ошибке")
    def error_message_displayed(self):
        """Проверяет появилось ли сообщение 'Укажите город прибытия'"""
        try:
            element = self.find_element(self.ERROR_MESSAGE)
            return element.is_displayed()
        except Exception:
            return False

    @allure.step("Получаем текст ошибки")
    def get_error_text(self):
        """Получает текст сообщения об ошибке"""
        try:
            element = self.find_element(self.ERROR_MESSAGE)
            return element.text
        except Exception:
            return None
