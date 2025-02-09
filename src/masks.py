from typing import Union


def get_mask_card_number(card_number: Union[int]) -> Union[str]:
    """Функция получает номер карты и возвращает ее маску"""
    if len(str(card_number)) != 16:
        raise ValueError("Некорректная длина номера карты")
    card_number_str = str(card_number)
    card_mask = card_number_str[0:4], card_number_str[4:6] + "**", "****", card_number_str[-4:]
    return " ".join(card_mask)


def get_mask_account(account_number: Union[int]) -> Union[str]:
    """Функция получает номер аккаунта и возвращает его маску"""
    if len(str(account_number)) != 20:
        raise ValueError("Некорректная длина номера аккаунта")
    account_number_str = str(account_number)
    account_mask = "**", account_number_str[-4:]
    return "".join(account_mask)


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
