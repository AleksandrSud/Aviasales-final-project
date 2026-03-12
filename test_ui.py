import allure
import pytest
from selenium import webdriver
from main_page import MainPage
from config import HEADLESS, IMPLICIT_WAIT
import time


@allure.feature("UI Тесты")
class TestAviasalesUI:

    @pytest.fixture
    def driver(self):
        """Настройка браузера"""
        options = webdriver.ChromeOptions()
        if HEADLESS:
            options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(IMPLICIT_WAIT)
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.title("Тест 1: Шрифты отображаются")
    @allure.severity(allure.severity_level.NORMAL)
    def test_fonts(self, driver):
        """Проверка что шрифты есть"""
        page = MainPage(driver).open()

        with allure.step("Проверяем шрифт"):
            font = page.font_family()
            assert font, "Шрифт не найден"
            allure.attach(f"Шрифт: {font}", name="Font")

    @allure.title("Тест 2: Цвет кнопки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_button_color(self, driver):
        """Проверка цвета кнопки поиска"""
        page = MainPage(driver).open()

        with allure.step("Проверяем цвет"):
            color = page.button_color()
            assert color, "Цвет не найден"
            allure.attach(f"Цвет: {color}", name="Button color")

    @allure.title("Тест 3: Появляется сообщение об ошибке при пустом поиске")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_error_message(self, driver):
        """Проверка что появляется сообщение 'Укажите город прибытия'"""
        page = MainPage(driver).open()

        with allure.step("Кликаем поиск без данных"):
            page.click(page.SEARCH_BUTTON)
        time.sleep(2)  # ждем появление сообщения

        with allure.step("Проверяем что появилось сообщение об ошибке"):
            assert page.error_message_displayed(), \
                "Сообщение об ошибке не появилось"

        with allure.step("Проверяем текст сообщения"):
            error_text = page.get_error_text()
        assert error_text.upper() == "УКАЖИТЕ ГОРОД ПРИБЫТИЯ", \
            f"Неверный текст ошибки: {error_text}"

    @allure.title("Тест 4: Навигация (проверка наличия кнопки Профиль)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigation(self, driver):
        """Проверка что кнопка профиля есть на странице"""
        page = MainPage(driver).open()

        with allure.step("Проверяем логотип"):
            assert page.logo_visible(), "Логотип не виден"

        with allure.step("Проверяем наличие кнопки профиля"):
            assert page.profile_visible(), \
                "Кнопка профиля не найдена на странице"

    @allure.title("Тест 5: Изображения")
    @allure.severity(allure.severity_level.NORMAL)
    def test_images(self, driver):
        """Проверка что изображения есть"""
        page = MainPage(driver).open()

        with allure.step("Проверяем логотип"):
            assert page.logo_visible(), "Логотип не загрузился"

        page.screenshot("Страница")
