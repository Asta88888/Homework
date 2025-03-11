import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"


def conversion(transaction: dict) -> float:
    """Функция возвращает сумму транзакции, если транзакция
    была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы
    операции в рубли в рублях"""
    amount = 0
    currency = transaction.get("currency_code")
    amount_transaction = transaction.get("amount")
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
        amount += float(transaction.get("amount"))
    return amount


# transactions = {'id': 957763565, 'state': 'EXECUTED',
#                 'date': '2019-01-05T00:52:30.108534',
#                 'description': 'Перевод со счета на счет',
#                 'from': 'Счет 46363668439560358409',
#                 'to': 'Счет 18889008294666828266', 'amount': '87941.37',
#                 'currency_name': 'руб.', 'currency_code': 'RUB'}
#
#
# if __name__ == "__main__":
#     transaction_amount = conversion(transactions)
#     print(transaction_amount)
