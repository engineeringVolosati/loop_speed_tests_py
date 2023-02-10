import random, ctypes
import numpy as np
from time import perf_counter

numb = 10_000_000

#==============================================================================
# Сравним суммирование проходов по списку и использование функций sum и range
#==============================================================================
def cycle_example():
    result = 0
    numbers = [num for num in range(numb)]

    for num in numbers:
        result += num
    print(result)

def sum_example():
    numbers = [num for num in range(numb)]
    print(sum(numbers))

def sum_range():
    print(sum(range(numb)))

#==============================================================================
# Сравнение enumerate и доступа по индексам
#==============================================================================
def enumerate_example():
    temp = 0
    numbers = [num for num in range(numb)]

    for index, num in enumerate(numbers):
        temp = num
    print(temp)

def index_access():
    temp = 0
    numbers = [num for num in range(numb)]

    for num in range(len(numbers)):
        temp = numbers[num]
    print(temp)

#==============================================================================
# Сравнение zip и обычного прохода циклами
#==============================================================================
def idx_example():
    res = 0
    a = [num for num in range(numb)]
    b = [num for num in range(numb)]

    for index in range(len(a)):
        res = a[index] + b[index]
    print(res)

def zip_example():
    res = 0
    a = [num for num in range(numb)]
    b = [num for num in range(numb)]

    for a_val, b_val in zip(a, b):
        res = a_val + b_val
    print(res)

#==============================================================================
# Сравнение циклов с генераторами
#==============================================================================
USERS_BUY = [
    ("confirmed", 100),
    ("unconfirmed", 500),
    ("confirmed", 900),
]

def fill_users_list():
    global USERS_BUY
    temp = [("confirmed", random.randint(10, 200)) for user in range(numb)]
    USERS_BUY += temp

def list_example():
    balance_list = [user[1] for user in USERS_BUY if user[0] == "confirmed"]
    res = sum(balance_list)
    print(res)

def generator_example():
    balance_list = (user[1] for user in USERS_BUY if user[0] == "confirmed")
    res = sum(balance_list)
    print(res)

def cycle_example():
    res = 0

    for user in USERS_BUY:
        if user[0] == "confirmed":
            res += user[1]
    print(res)

#==============================================================================
# Сравнение стандартных CPython функций и NumPy
#==============================================================================
def sum_range():
    print(sum(range(numb)))

def np_sum():
    print(np.sum(np.arange(numb)))

#==============================================================================
# Собственная реализация на чистом C
#==============================================================================
testlib = ctypes.CDLL("./loop.dll")

def loop_dll():
    print(ctypes.c_uint32(testlib.loop(numb)))


if __name__ == "__main__":
    print("Сравним суммирование проходов по списку и\nиспользование функций sum и range")

    start = perf_counter()
    cycle_example()
    print(f"cycle_example time: {(perf_counter() - start):.02f}")

    start = perf_counter()
    sum_example()
    print(f"sum_example time: {(perf_counter() - start):.02f}")

    start = perf_counter()
    sum_range()
    print(f"sum_range time: {(perf_counter() - start):.02f}")

    input("\nENTER to continue\n")

    print("Сравнение enumerate и доступа по индексам")

    start = perf_counter()
    enumerate_example()
    print(f"enumerate_example time: {(perf_counter() - start):.02f}")

    start = perf_counter()
    index_access()
    print(f"index_access time: {(perf_counter() - start):.02f}")

    input("\nENTER to continue\n")

    print("Сравнение zip и обычного прохода циклами")

    start = perf_counter()
    idx_example()
    print(f"idx_example time: {(perf_counter() - start):.02f}")

    start = perf_counter()
    zip_example()
    print(f"zip_example time: {(perf_counter() - start):.02f}")

    input("\nENTER to continue\n")

    print("Сравнение циклов с генераторами")

    fill_users_list()

    start = perf_counter()
    list_example()
    print(f"list_example time: {(perf_counter() - start):.02f}")

    start = perf_counter()
    generator_example()
    print(f"generator_example time: {(perf_counter() - start):.02f}")

    start = perf_counter()
    cycle_example()
    print(f"cycle_example time: {(perf_counter() - start):.02f}")

    input("\nENTER to continue\n")

    print("Сравнение стандартных CPython функций и NumPy")

    print('\nВАЖНО!\n numpy воспринимает int именно как int (-2,147,483,648 to 2,147,483,647)')
    print('поэтому для корректного сравнения результатов преобразовываем в')
    print('NumPy - numb = np.uint64(numb)\nи\nC - numb = ctypes.c_uint64(numb)\n')

    start = perf_counter()
    sum_range()
    print(f"sum_range time: {(perf_counter() - start):.02f}")

    np_numb = np.uint64(numb)
    c_numb = ctypes.c_uint64(numb)
    _ = numb

    numb = np_numb
    start = perf_counter()
    np_sum()
    print(f"np_sum time: {(perf_counter() - start):.02f}")

    numb = c_numb
    start = perf_counter()
    loop_dll()
    print(f"loop_dll time: {(perf_counter() - start):.02f}")
    print("И вот тут выскочил трабл с dll.\n"\
        "Python воспринимает возвращаемое значение как int.")
    print("Сейчас не важно, потом можно будет подсмотреть в\n"\
        "исходниках CPython, если вдруг понадобится")
