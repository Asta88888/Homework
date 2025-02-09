import pytest


def filter_by_state(transactions_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    new_list_of_dict = list()
    for i in transactions_list:
        if i.get("state") == state:
            new_list_of_dict.append(i)
    return new_list_of_dict


def sort_by_date(transactions_list: list[dict], reverse: bool = True) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате"""
    list_sorted_by_date = list(sorted(transactions_list, key=lambda x: x["date"], reverse=reverse))
    return list_sorted_by_date


if __name__ == "__main__":
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(transactions))
    print(sort_by_date(transactions))
