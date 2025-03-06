import os
import pandas as pd
from pandas import DataFrame

path_csv = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
path_excel = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def read_csv(df: DataFrame) -> list[dict]:
    """Функция принимает путь до csv файла, считывает его и возвращает
     список словарей с транзакциями"""
    df = pd.read_csv(path_csv)
    transactions_csv = df.to_dict(orient="records")
    return transactions_csv


def read_excel(df: DataFrame) -> list[dict]:
    """Функция принимает путь до excel файла, считывает его и возвращает
     список словарей с транзакциями"""
    df = pd.read_excel(path_excel)
    transactions_excel = df.to_dict(orient="records")
    return transactions_excel


if __name__ == "__main__":
    transactions = read_csv(path_csv)
    print(type(transactions))
    transactions_ex = read_excel(path_excel)
    print(type(transactions_ex))