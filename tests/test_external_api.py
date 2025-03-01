from src.external_api import conversion
from unittest.mock import patch



@patch("requests.get")
def test_conversion(mock_get):
    mock_get.return_value.json.return_value = {"result": 30.0}
    result = conversion(  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  })
    assert result != {"result": 30.0}


