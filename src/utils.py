import json


def get_transactions(path: str) -> list[dict[str]]:
    """Функция принимающая путь до JSON-файла и возвращает список словарей с
    данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf8") as transactions_file:
            try:
                transactions_data = json.load(transactions_file)
            except json.JSONDecodeError:
                print("File empty")
                return False
    except FileNotFoundError:
        print("File not found")
        return False
    return transactions_data


if __name__ == "__main__":
    path = "C:/Users/User/PycharmProjects/Homework_Project_1/data/operations.json"
    transactions = get_transactions(path)
    print(transactions)