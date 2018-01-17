# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5
from time import *
import contextlib
@contextlib.contextmanager
def timer():
    time_start = time();
    yield
    time_end = time();
    print(time_end - time_start)
