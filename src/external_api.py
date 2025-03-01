import os
import requests
from dotenv import load_dotenv
import json


load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"

def conversion(transaction: dict) -> float:
    """Функция возвращает сумму транзакции, если транзакция
    была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы
    операции в рубли в рублях"""
    amount = 0
    currency = transaction["operationAmount"]["currency"]["code"]
    amount_transaction = transaction["operationAmount"]["amount"]
    payload = {"amount": f"{amount_transaction}", "from": f"{currency}", "to": "RUB"}
    headers = {"apikey": f"{API_KEY}"}
    if currency != "RUB":
        try:
            response = requests.get(url, headers=headers, params=payload)
            status_code = response.status_code
            if status_code == 200:
                data_json = response.json()
                amount += data_json["result"]
                return round(amount, 3)
            else:
                print(status_code)
                print({response.reason})
        except requests.exceptions.RequestException:
            print("Ошибка конвертации")
    else:
        amount += float(transaction["operationAmount"]["amount"])
    return amount


transactions = {'id': 490100847, 'state':
                   'EXECUTED', 'date': '2018-12-22T02:02:49.564873',
                   'operationAmount': {'amount': '56516.63',
                   'currency': {'name': 'USD', 'code': 'USD'}},
                   'description': 'Перевод с карты на карту',
                   'from': 'Visa Gold 8326537236216459',
                   'to': 'MasterCard 6783917276771847'}


if __name__ == "__main__":
    transaction_amount = conversion(transactions)
    print(transaction_amount)
