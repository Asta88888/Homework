import os
import pandas as pd


path_csv = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
path_excel = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def read_csv(file_path: str) -> list[dict]:
    """Функция принимает путь до csv файла, считывает его и возвращает
     список словарей с транзакциями"""
    df = pd.read_csv(path_csv)
    print(type(df), df)
    return df.to_dict(orient="records")


def read_excel(file_path: str) -> list[dict]:
    """Функция принимает путь до excel файла, считывает его и возвращает
     список словарей с транзакциями"""
    df = pd.read_excel(path_excel)
    return df.to_dict(orient="records")


if __name__ == "__main__":
    transactions = read_csv(path_csv)
    print(type(transactions))
    transactions_ex = read_excel(path_excel)
    print(type(transactions_ex))
