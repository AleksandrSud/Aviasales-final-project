import subprocess
import sys


def run_ui():
    """Запуск UI тестов"""
    print(" Запуск UI тестов...")
    subprocess.run([
        sys.executable, "-m", "pytest",
        "test_ui.py", "-v", "--alluredir=allure-results"
    ])


def run_api():
    """Запуск API тестов"""
    print(" Запуск API тестов...")
    subprocess.run([
        sys.executable, "-m", "pytest",
        "test_api.py", "-v", "--alluredir=allure-results"
    ])


def run_all():
    """Запуск всех тестов"""
    print("\n🚀 Запуск всех тестов...")
    subprocess.run([
        sys.executable, "-m", "pytest",
        "test_ui.py", "test_api.py", "-v", "--alluredir=allure-results"
    ])


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Aviasales Test Runner")
    print("="*50)
    print("1. UI тесты")
    print("2. API тесты")
    print("3. Все тесты")
    print("="*50)

    choice = input("Выберите (1-3): ")

    if choice == "1":
        run_ui()
    elif choice == "2":
        run_api()
    elif choice == "3":
        run_all()
    else:
        print("Неверный выбор")
