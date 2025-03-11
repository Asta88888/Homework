import os
from src.reader_csv_excel import read_csv, read_excel
from src.utils import get_transactions, find_by_description
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def main():
    """Функция отвечает за основную логику проекта и связывает
    функциональности между собой."""
    print(
        """Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n 
    Выберите необходимый пункт меню:\n
    1. Получить информацию о транзакциях из JSON-файла\n
    2. Получить информацию о транзакциях из CSV-файла\n
    3. Получить информацию о транзакциях из XLSX-файла\n"""
    )
    while True:
        file_types = {1: "JSON-файл", 2: "CSV-файл", 3: "XLSX-файл"}
        user_input = int(input("Пользователь: "))
        if user_input in file_types:
            print(f"Для обработки выбран {file_types.get(user_input)}")
            break
        else:
            print("Введен некорректный ответ. Повторите ввод")
    if user_input == 1:
        transactions = get_transactions(os.path.join("data", "operations.json"))
    elif user_input == 2:
        transactions = read_csv(os.path.join("data", "transactions.csv"))
    elif user_input == 3:
        transactions = read_excel(os.path.join("data", "transactions_excel.xlsx"))
    while True:
        print("""Программа: 
        Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        user_input_2 = input("Пользователь: ").upper()
        if user_input_2 in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print(f"Программа:\n Статус операции {user_input_2} недоступен.")
            continue
    filtered_transactions = filter_by_state(transactions, user_input_2)
    print(f"Программа: \nОперации отфильтрованы по статусу {user_input_2}")
    while True:
        print("Программа: \nОтсортировать операции по дате? Да/Нет")
        user_input_3 = input("Пользователь: ").lower()
        if user_input_3 in ("да", "нет"):
            break
        else:
            print("Введен некорректный ответ. Повторите ввод")
    if user_input_3 == "да":
        while True:
            print("Программа: \nОтсортировать по возрастанию или по убыванию?")
            user_input_4 = input("Пользователь: ").lower()
            if user_input_4 in ("по возрастанию", "по убыванию"):
                break
            else:
                print("Введен некорректный ответ. Повторите ввод")
        if user_input_4 == "по возрастанию":
                direction = False
        elif user_input_4 == "по убыванию":
            direction = True
        sorted_date = sort_by_date(filtered_transactions, direction)
    elif user_input_3 == "нет":
        sorted_date = sort_by_date(filtered_transactions)
    while True:
        print("Программа: \nВыводить только рублевые транзакции? Да/Нет")
        user_input_5 = input("Пользователь: ").lower()
        if user_input_5 in ("да", "нет"):
            break
        else:
            print("Введен некорректный ответ. Повторите ввод")
    if user_input_5 == "да":
        rub = [t for t in sorted_date if t.get("currency_code") == "RUB"]
    elif user_input_5 == "нет":
        rub = sorted_date
    while True:
        print("Программа: \nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input_6 = input("Пользователь: ").lower()
        if user_input_6 in ("да", "нет"):
            break
        else:
            print("Введен некорректный ответ. Повторите ввод")
    if user_input_6 == "да":
        user_input_7 = input("Введите слово для фильтрации: ").lower()
        filtered_by_description = find_by_description(rub, user_input_7)
        result = filtered_by_description
    elif user_input_6 == "нет":
        result = rub
    count_transactions = len(result)
    if count_transactions > 0:
        print("Программа: Распечатываю итоговый список транзакций...")
        print(f"Программа: \nВсего банковских операций в выборке: {count_transactions}")
        for transaction in result:
            description_transaction = transaction.get("description")
            if description_transaction == "Открытие вклада":
                from_ = description_transaction
            else:
                from_ = mask_account_card(transaction.get("from"))
                to_ = mask_account_card(transaction.get("to"))
                date = get_date(transaction.get("date"))
                amount = transaction.get("amount")
                currency = transaction.get("currency_code")
            if description_transaction == "Открытие вклада":
                print(f"{date} {description_transaction}\nСчет {to_}\nСумма {amount} {currency}\n")
            else:
                print(f"{date} {description_transaction}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")
    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


# if __name__ == "main":
print(main())
