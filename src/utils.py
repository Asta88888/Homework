import json
import os
import logging
from operator import ifloordiv
from typing import Any
import re
from collections import Counter

log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("utils.py")
file_handler = logging.FileHandler(os.path.join(log_dir, "utils.log"), encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
logger.debug("Debug message")

console_handler = logging.StreamHandler()
console_handler.setFormatter(file_formatter)
logger.addHandler(console_handler)


def get_transactions(path_file: str) -> list[dict[str, Any]]:
    """Функция принимающая путь до JSON-файла и возвращает список словарей с
    данными о финансовых транзакциях"""
    logger.info("Выполняется чтение JSON-файла с транзакциями")
    try:
        with open(path_file, "r", encoding="utf8") as transactions_file:
            try:
                transactions_data = json.load(transactions_file)

            except json.JSONDecodeError as e:
                logger.error(f"Ошибка чтения JSON-файла", exc_info=True)
                print("File empty")
                return []
    except FileNotFoundError:
        logger.error("JSON-файл не найден")
        print("File not found")
        return []
    for operation in transactions_data:
        operation_amount = operation.pop("operationAmount") if operation.get("operationAmount") else {}
        operation["amount"] = operation_amount.get("amount")
        operation["currency_name"] = operation_amount.get("currency", {}).get("name")
        operation["currency_code"] = operation_amount.get("currency", {}).get("code")

    logger.info("Получены транзакции из JSON-файла")
    return transactions_data


def find_by_description(transactions_list: list[dict], find_string: str) -> list[dict]:
    """Функция возвращающая список транзакций, найденных по описанию"""
    pattern = re.compile(re.escape(find_string), re.IGNORECASE)
    return [t for t in transactions_list if pattern.search(t.get("description", ""))]


def count_categories(transaction_list: list[dict], categories: list[str]) -> dict:
    """Функция принимает список транзакций и категории транзакций, а
     возвращает словарь, в котором ключи — это названия категорий,
     а значения — это количество операций в каждой категории."""
    descriptions = [t.get("description") for t in transaction_list if t.get("description") in categories]
    c = Counter(descriptions)
    return dict(c)


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    transactions = get_transactions(path)
    print(transactions)
    print(count_categories(transactions, ["Открытие вклада", "Перевод организации"]))
