from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Находим элемент: {locator}")
    def find_element(self, locator):
        """Поиск элемента"""
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator):
        """Клик по элементу"""
        self.find_element(locator).click()

    @allure.step("Проверяем видимость элемента: {locator}")
    def is_visible(self, locator):
        """Проверка видимости элемента"""
        try:
            return self.wait.until(EC.visibility_of_element_located(
                locator)).is_displayed()
        except Exception:
            return False

    @allure.step("Получаем CSS свойство: {property}")
    def get_css(self, locator, property):
        """Получение CSS свойства"""
        return self.find_element(locator).value_of_css_property(property)

    @allure.step("Делаем скриншот")
    def screenshot(self, name="Скриншот"):
        """Сделать скриншот"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
