import time
from typing import Callable
from typing import Optional
from typing import Any


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, автоматически регистрирующий детали выполнения функций,
    такие как время вызова, имя функции, передаваемые аргументы, результат
    выполнения и информация об ошибках."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                print(f"Начало выполнения функции: {func.__name__}")
                time_start = time.time()
                result = func(*args, **kwargs)
                time_finish = time.time()
                durations = time_finish - time_start
                print(f"Конец выполнения функции: {func.__name__}")
                print(f"Время выполнения функции: {durations:.7f}")
                log_message = f"{func.__name__} ok \nРезультат: {result}\n"
                if filename:
                    with open(filename, "a", encoding="utf8") as file:
                        file.write(f"{log_message}\n")
                else:
                    print(f"{log_message}\n")
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}.Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf") as file:
                        file.write(error_message)
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator


if __name__ == "__main__":

    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
