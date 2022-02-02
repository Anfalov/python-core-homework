from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            execution_time_sum = 0
            for i in range(num):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                print(end - start)
                execution_time_sum += end - start
            print(execution_time_sum / num)
        return inner_wrapper
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
