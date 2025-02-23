import pytest
from src.decorators import log


def test_log_error_console(capsys):
    @log()
    def func(x, y):
        raise TypeError
    with pytest.raises(TypeError):
        func(1, "2")

def test_log_success_console(capsys):
    @log(filename="my_log.txt")
    def func(x, y):
        return x + y

    func(1, 2)
    with open("my_log.txt", "r", encoding="utf8") as file:
        all_lines = file.readlines()
        message = all_lines[-1]
        assert message  == "\n"