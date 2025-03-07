import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_number():
    return 1234567891011213


@pytest.mark.parametrize("card_number, expected", [(1234567891011213, "1234 56** **** 1213"),
                                                   (9876543210123456, "9876 54** **** 3456")
                                                   ])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid_number(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(123456)
    with pytest.raises(ValueError):
        get_mask_card_number(123456789101112131415)
    with pytest.raises(ValueError):
        get_mask_card_number("")


@pytest.fixture
def account_number():
    return [12345678910111213141]


@pytest.mark.parametrize("account_number, expected", [(12345678910111213141, "**3141"),
                                                      (98765432101234567891, "**7891")
                                                      ])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_number_invalid_number(account_number):
    with pytest.raises(ValueError):
        get_mask_account(123456)
    with pytest.raises(ValueError):
        get_mask_account(12345678910111213141516)
    with pytest.raises(ValueError):
        get_mask_account("")
