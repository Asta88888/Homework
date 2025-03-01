from unittest.mock import patch, mock_open
from src.utils import get_transactions
import pytest
import json

@patch("builtins.open")
@patch("json.load")
def test_get_transactions(mock_load, mock_open_file):
    mock_open_file.new = mock_open()
    mock_load.return_value = [{"id": 123}, {"id": 321}]
    result = get_transactions("")
    assert result == [{"id": 123}, {"id": 321}]


@patch("builtins.open")
def test_get_transactions_error(mock_open_file):
    mock_open_file.new = mock_open()
    mock_open_file.side_effect = FileNotFoundError

    result = get_transactions("")
    assert  result == []


@patch("builtins.open")
@patch("json.load")
def test_get_transactions_json_decode_error(mock_load, mock_open_file):
    mock_open_file.new = mock_open()
    mock_load.side_effect = json.JSONDecodeError("Error", "", 1)
    result = get_transactions("")
    assert result == []
