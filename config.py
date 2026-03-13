# API настройки
# Базовые URL для разных сервисов Aviasales
API_TICKETS_BASE = "https://tickets-api.aviasales.com"
API_EXPLORE_BASE = (
    "https://explore-api.aviasales.com/aggregated/v1/web/aviasales"
)
API_SUGGEST_BASE = "https://suggest.aviasales.com"

# Тестовые данные
TEST_DATA = {
    # Для API
    "currency_codes": ["RUB", "USD", "EUR"],
    "markets": ["ru", "us"],
    "invalid_market": "русский",  # невалидный market
    "invalid_holidays_enabled": 10,  # невалидный holidays_enabled
    "valid_locale": "ru_RU",
    "invalid_locale": "78_90",
    "coordinates": [
        {"lat": 55.7558, "lon": 37.6176},  # Москва
    ],
    # Для UI
    "origin": "MOW",
    "destination": "LED",
    "departure_date": "2024-04-15",
    "return_date": "2024-04-20"
}

# Настройки браузера
HEADLESS = False
IMPLICIT_WAIT = 5
