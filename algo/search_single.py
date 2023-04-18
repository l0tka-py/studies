"""
    Дано: массив целых чисел в котором, все числа встречаются 2 раза и лишь одно число встречается 1 раз.
    Найти: число, которое встречается 1 раз
"""
from functools import reduce
from python_tricks.time_decorator import *


@counting_time
def search_single1(numbers):
    numbers = sorted(numbers)
    for num in numbers:
        if numbers.count(num) == 1:
            return num


@counting_time
def search_single_xor(numbers):
    return reduce(lambda x, y: x ^ y, numbers)


if __name__ == "__main__":
    numbers_list = [2, 2, 33, 33, 14, 14, 5, 3, 3, 7, 7, 8, 8, 100, 100, 221, 221, 32, 32, 77, 77]
    print(search_single_xor(numbers_list))
