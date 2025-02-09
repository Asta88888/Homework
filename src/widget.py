from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(data: str) -> str:
    """Функция маскирует счет или карту"""
    split_info = data.split(" ")
    numbers = split_info[-1]
    card_or_account_type = split_info[:-1]
    if len(numbers) < 16:
        raise ValueError("Неверное количество чисел")
    if data.startswith("Счет"):
        masked_numbers = get_mask_account(int(numbers))
    else:
        masked_numbers = get_mask_card_number(int(numbers))
    return " ".join(card_or_account_type) + " " + masked_numbers


print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("Visa Classic 6831982476737658"))


def get_date(incorrect_date: str) -> str:
    """Функция выводит дату в формате ДД.ММ.ГГГГ"""
    if not incorrect_date:
        raise ValueError("Дата не может быть пустой")
    clear_date = incorrect_date[0:10]
    year, month, day = clear_date.split("-")
    correct_date = day, month, year
    return ".".join(correct_date)


print(get_date("2024-03-11T02:26:18.671407"))
