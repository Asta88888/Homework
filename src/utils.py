import json
import os
import logging
from typing import Any

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
    try:
        logger.info("Выполняется чтение JSON-файла с транзакциями")
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
    logger.info("Получены транзакции из JSON-файла")
    return transactions_data


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    transactions = get_transactions(path)
    print(transactions)
