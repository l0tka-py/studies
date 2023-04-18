"""
Декоратор: некая обертка функции, которая позволяет изменить поведение функции, не меняя ее код
"""
import time


def counting_time(func):
    def res(*args, **kwargs):
        datetime = time.time()
        rs = func(*args, **kwargs)
        print(f"Время работы вашей функции: {datetime - time.time()}")
        return rs
    return res
