from src.external_api import conversion
from unittest.mock import patch
import pytest

@patch("requests.get")
def test_conversion(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 30.0}

    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "100",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    result = conversion(transaction)
    assert result == 30.0


@pytest.fixture
def mock_requests_get():
    with patch("requests.get") as mock_get:
        yield mock_get

def test_conversion_rub(mock_requests_get):
    transaction = {
        "operationAmount": {
            "amount": "1000",
            "currency": {"code": "RUB"},
        }
    }
    result = conversion(transaction)
    assert result == 1000.0
    mock_requests_get.assert_not_called()