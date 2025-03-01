import json
import os

def get_transactions(path_file: str) -> list[dict[str]]:
    """Функция принимающая путь до JSON-файла и возвращает список словарей с
    данными о финансовых транзакциях"""
    try:
        with open(path_file, "r", encoding="utf8") as transactions_file:
            try:
                transactions_data = json.load(transactions_file)
            except json.JSONDecodeError:
                print("File empty")
                return []
    except FileNotFoundError:
        print("File not found")
        return []
    return transactions_data


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    transactions = get_transactions(path)
    print(transactions)
