import pytest
from src.widget import mask_account_card, get_date


@pytest.fixture
def type_data():
    return ["Visa Platinum 7000792289606361",
            "Maestro 7000792289606361",
            "Счет 73654108430135874305",
            "MasterCard 7158300734726758",
            "Visa Classic 6831982476737658",
            "Visa Gold 5999414228426353",
            "Счет 35383033474447895560"]


@pytest.mark.parametrize("type_data, expected", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                                                 ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
                                                 ("Счет 73654108430135874305", "Счет **4305"),
                                                 ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                                 ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                                 ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                                                 ("Счет 35383033474447895560", "Счет **5560")])
def test_mask_account_card(type_data, expected):
    assert mask_account_card(type_data) == expected


def test_mask_account_card_invalid_length(type_data):
    with pytest.raises(ValueError):
        mask_account_card("0")


@pytest.fixture
def date():
    return ["2024-03-11T02:26:18.671407",
            "2008-12-10T02:26:18.671407",
            "1987-03-20T02:26:18.671407"]


@pytest.mark.parametrize("date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                            ("2008-12-10T02:26:18.671407", "10.12.2008"),
                                            ("1987-03-20T02:26:18.671407", "20.03.1987")])
def test_get_date(date, expected):
    assert get_date(date) == expected


def test_get_date_invalid():
    with pytest.raises(ValueError) as error:
        get_date("")
    assert str(error.value) == "Дата не может быть пустой"
