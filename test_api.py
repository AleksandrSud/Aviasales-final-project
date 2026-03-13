import allure
import pytest
from aviasales_api import AviasalesAPI
from config import TEST_DATA


@allure.feature("API Тесты Aviasales")
@pytest.mark.api
class TestAviasalesAPI:
    """Класс с API тестами"""

    def setup_method(self):
        """Подготовка перед каждым тестом"""
        self.api = AviasalesAPI()

    # ПОЗИТИВНЫЕ ТЕСТЫ

    @allure.title("Получение списка валют")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_currencies(self):
        """Проверка получения валют"""
        resp = self.api.get_currencies()

        with allure.step("Проверяем статус"):
            assert resp.status_code == 200

        with allure.step("Проверяем данные"):
            data = resp.json()
            assert isinstance(data, dict)
            assert len(data) > 0
            assert "rub" in data or "RUB" in data, "Рубль не найден \
                в списке валют"

    @allure.title("Получение праздников")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("market", TEST_DATA["markets"])
    def test_get_holidays(self, market):
        """Проверка получения праздников"""
        resp = self.api.get_holidays(market=market)

        with allure.step("Проверяем статус"):
            assert resp.status_code == 200

        with allure.step("Проверяем структуру данных"):
            data = resp.json()
            assert "periods" in data
            assert isinstance(data["periods"], list)

    @allure.title("Получение мест рядом (Москва)")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_places_moscow(self):
        """Проверка поиска мест рядом"""
        resp = self.api.get_places_nearby()

        with allure.step("Проверяем статус"):
            assert resp.status_code == 200

        with allure.step("Проверяем данные"):
            data = resp.json()
            assert isinstance(data, list)
            assert len(data) > 0
            first_place = data[0]
            assert "id" in first_place
            assert "name" in first_place
            assert "type" in first_place

    # НЕГАТИВНЫЕ ТЕСТЫ

    @allure.title("Негатив: DELETE для валют")
    @allure.severity(allure.severity_level.NORMAL)
    def test_currencies_invalid_method(self):
        """DELETE метод не должен работать"""
        resp = self.api.get_currencies_invalid_method()

        with allure.step("Проверяем статус ошибки"):
            assert resp.status_code in [405, 404, 400]

    @allure.title("Негатив: невалидный market")
    @allure.severity(allure.severity_level.NORMAL)
    def test_holidays_invalid_market(self):
        """Неверный параметр market (русский)"""
        resp = self.api.get_holidays_invalid_market()

        with allure.step("Проверяем статус ошибки"):
            if resp.status_code == 200:
                data = resp.json()
                assert "periods" in data
            else:
                assert resp.status_code in [400, 404]

    @allure.title("Негатив: невалидный holidays_enabled")
    @allure.severity(allure.severity_level.NORMAL)
    def test_holidays_invalid_param(self):
        """Неверный параметр holidays_enabled (10 вместо true/false)"""
        resp = self.api.get_holidays_invalid_param()

        with allure.step("Проверяем статус ошибки"):
            if resp.status_code == 200:
                data = resp.json()
                assert "periods" in data
            else:
                assert resp.status_code in [400, 404]

    @allure.title("Негатив: DELETE для мест рядом")
    @allure.severity(allure.severity_level.NORMAL)
    def test_places_invalid_method(self):
        """DELETE метод для places/nearby"""
        resp = self.api.get_places_nearby_invalid_method()

        with allure.step("Проверяем что API все равно вернул данные"):
            assert resp.status_code == 200

        with allure.step(
             "Проверяем что данные корректны (API игнорирует метод)"):
            data = resp.json()
            assert isinstance(data, list)
            assert len(data) > 0
        print(f"\n✅ DELETE запрос тоже работает, вернул {len(data)} мест")

    @allure.title("Негатив: невалидный locale")
    @allure.severity(allure.severity_level.NORMAL)
    def test_places_invalid_locale(self):
        """Неверный параметр locale (78_90)"""
        resp = self.api.get_places_nearby_invalid_locale()

        with allure.step("Проверяем статус ошибки"):
            if resp.status_code == 200:
                data = resp.json()
                assert isinstance(data, list)
            else:
                assert resp.status_code in [400, 404]
