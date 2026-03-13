import allure
import requests
from config import API_TICKETS_BASE, API_EXPLORE_BASE, API_SUGGEST_BASE


class AviasalesAPI:
    """Класс для работы с Aviasales API"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 ('
            'Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
        })

    @allure.step("GET запрос к {url}")
    def _get(self, url, params=None):
        """Выполняет GET запрос"""
        print("\n🔍 Отладка API:")
        print(f"URL: {url}")
        print(f"Params: {params}")

        resp = self.session.get(url, params=params, timeout=10)

        print(f"Status: {resp.status_code}")
        print(f"Response: {resp.text[:200]}")

        allure.attach(
            f"URL: {url}\nStatus: {resp.status_code}\nResponse: {resp.text[
                :500]}",
            name="Response",
            attachment_type=allure.attachment_type.TEXT
        )
        return resp

    @allure.step("DELETE запрос к {url}")
    def _delete(self, url, params=None):
        """Выполняет DELETE запрос (для негативных тестов)"""
        print("\n🔍 Отладка API (DELETE):")
        print(f"URL: {url}")

        resp = self.session.delete(url, params=params, timeout=10)

        print(f"Status: {resp.status_code}")
        return resp

    # ПОЗИТИВНЫЕ ТЕСТЫ

    @allure.step("Получение списка валют")
    def get_currencies(self):
        """GET /currency.json - список валют"""
        url = f"{API_TICKETS_BASE}/currency.json"
        return self._get(url)

    @allure.step("Получение праздников и выходных для рынка {market}")
    def get_holidays(self, market="ru", holidays_enabled=True):
        """GET /holidays.json - праздники и выходные"""
        url = f"{API_EXPLORE_BASE}/holidays.json"
        params = {
            "holidays_enabled": str(holidays_enabled).lower(),
            "market": market
        }
        return self._get(url, params)

    @allure.step("Получение мест рядом (locale: {locale})")
    def get_places_nearby(self, locale="ru_RU"):
        """GET /nearest_places.json - места рядом"""
        url = f"{API_SUGGEST_BASE}/v2/nearest_places.json"
        params = {"locale": locale}
        return self._get(url, params)

    # НЕГАТИВНЫЕ ТЕСТЫ

    @allure.step("Негатив: DELETE запрос для валют")
    def get_currencies_invalid_method(self):
        """DELETE /currency.json - невалидный метод"""
        url = f"{API_TICKETS_BASE}/currency.json"
        return self._delete(url)

    @allure.step("Негатив: невалидный параметр market")
    def get_holidays_invalid_market(self):
        """GET с невалидным market='русский'"""
        url = f"{API_EXPLORE_BASE}/holidays.json"
        params = {
            "holidays_enabled": "true",
            "market": "русский"
        }
        return self._get(url, params)

    @allure.step("Негатив: невалидный параметр holidays_enabled")
    def get_holidays_invalid_param(self):
        """GET с невалидным holidays_enabled=10"""
        url = f"{API_EXPLORE_BASE}/holidays.json"
        params = {
            "holidays_enabled": 10,
            "market": "ru"
        }
        return self._get(url, params)

    @allure.step("Негатив: DELETE запрос для мест рядом")
    def get_places_nearby_invalid_method(self):
        """DELETE /nearest_places.json - невалидный метод"""
        url = f"{API_SUGGEST_BASE}/v2/nearest_places.json"
        params = {"locale": "ru_RU"}
        return self._delete(url, params)

    @allure.step("Негатив: невалидный параметр locale")
    def get_places_nearby_invalid_locale(self, locale="78_90"):
        """GET с невалидным locale='78_90'"""
        url = f"{API_SUGGEST_BASE}/v2/nearest_places.json"
        params = {"locale": locale}
        return self._get(url, params)
