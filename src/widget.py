from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(numbers: str) -> str:
    if "Счет" in numbers:
        return "Счет" + " " + get_mask_account(numbers)
    else:
        number_mask = get_mask_card_number(numbers[-16:])
        result = numbers.replace(numbers[-16:], number_mask)
    return result


print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("Visa Classic 6831982476737658"))


def get_date(incorrect_date: str) -> str:
    clear_date = incorrect_date[0:10]
    year, month, day = clear_date.split("-")
    correct_date = day, month, year
    return ".".join(correct_date)


print(get_date("2024-03-11T02:26:18.671407"))