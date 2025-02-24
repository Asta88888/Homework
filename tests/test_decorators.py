import pytest
from src.decorators import log


def test_log_error_console(capsys):
    @log()
    def func(x, y):
        raise TypeError
    with pytest.raises(TypeError):
        func(1, "2")


def test_log_with_error(capsys):
    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out


def test_log_output(capsys):
    @log()
    def add(x, y):
        return x + y
    result = add(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert "Начало выполнения функции: add" in captured.out
    assert "Конец выполнения функции: add" in captured.out
    assert "Результат: 3" in captured.out
