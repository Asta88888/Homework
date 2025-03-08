from unittest.mock import patch
import pandas as pd
from src.reader_csv_excel import read_csv, read_excel
import pandas

@patch("pandas.read_csv")
def test_read_csv(mock_read_csv):
    mock_data = pd.DataFrame([
        {"id": 1, "amount": 100, "status": "completed"},
        {"id": 2, "amount": 200, "status": "pending"}
    ])
    mock_read_csv.return_value = mock_data
    result = pandas.read_csv("fake_path.csv")
    result = result.to_dict(orient="records")
    expected = [
        {"id": 1, "amount": 100, "status": "completed"},
        {"id": 2, "amount": 200, "status": "pending"}
    ]
    assert result == expected
    mock_read_csv.assert_called_once_with("fake_path.csv")


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel):
    mock_data = pd.DataFrame([
        {"id": 3, "amount": 300, "status": "failed"},
        {"id": 4, "amount": 400, "status": "completed"}
    ])
    mock_read_excel.return_value = mock_data
    result = pandas.read_excel("fake_path.xlsx")
    result = result.to_dict(orient="records")
    expected = [
        {"id": 3, "amount": 300, "status": "failed"},
        {"id": 4, "amount": 400, "status": "completed"}
    ]
    assert result == expected
    mock_read_excel.assert_called_once_with("fake_path.xlsx")


