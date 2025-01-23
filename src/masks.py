from typing import Union


def get_mask_card_number(card_number: Union[int]) -> Union[str]:
    """Функция получает номер карты и возвращает ее маску"""
    card_number_str = str(card_number)
    card_mask = card_number_str[0:4], card_number_str[4:6] + "**", "****", card_number_str[-4:]
    return " ".join(card_mask)


def get_mask_account(account_number: Union[int]) -> Union[str]:
    """Функция получает номер аккаунта и возвращает его маску"""
    account_number_str = str(account_number)
    account_mask = "**", account_number_str[-4:]
    return "".join(account_mask)



