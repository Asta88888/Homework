from typing import Union
import logging
import os

log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("masks.py")
file_handler = logging.FileHandler(os.path.join(log_dir, "masks.log"), encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
logger.debug("Debug message")

console_handler = logging.StreamHandler()
console_handler.setFormatter(file_formatter)
logger.addHandler(console_handler)


def get_mask_card_number(card_number: Union[int]) -> Union[str, None]:
    """Функция получает номер карты и возвращает ее маску"""
    logger.info("Выполняется проверка на корректность номера карты")
    try:
        if len(str(card_number)) != 16:
            logger.error("Ошибка: Некорректная длина номера карты")
            raise ValueError("Некорректная длина номера карты")

        card_number_str = str(card_number)
        card_mask = card_number_str[0:4], card_number_str[4:6] + "**", "****", card_number_str[-4:]
        logger.info("Номер карты успешно замаскирован")
        return " ".join(card_mask)
    except ValueError as e:
        logger.error(f"Ошибка: {e}")
        raise e
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")
        raise e


def get_mask_account(account_number: Union[int]) -> Union[str, None]:
    """Функция получает номер аккаунта и возвращает его маску"""
    logger.info("Выполняется проверка номера аккаунта")
    try:
        if len(str(account_number)) != 20:
            logger.error("Ошибка: Некорректная длина номера аккаунта")
            raise ValueError("Некорректная длина номера аккаунта")
        account_number_str = str(account_number)
        account_mask = "**", account_number_str[-4:]
        logger.info("Номер аккаунта успешно замаскирован")
        return "".join(account_mask)
    except ValueError as e:
        logger.error(f"Ошибка: {e}")
        raise e
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")
        raise e


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
