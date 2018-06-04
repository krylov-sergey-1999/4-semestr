import math
from Task6.Subtask1.storage import *


def methodtaylor(x, x0, table):
    i = 2
    k = 5
    s = [0]
    if x - x0 == 0:
        return sum(s)
    while k != 0:
        temporary = table[2][i] / math.factorial((i - 2)) * pow(x - x0, i - 2)
        i += 1
        if temporary != 0:
            k -= 1
            s.append(temporary)
    return sum(s)


def diff(arr, h):
    l = len(arr)
    k = 2
    while k != 10:
        temporary = (-3 * arr[0][k] + 4 * arr[1][k] - arr[2][k]) / (2 * h)
        (arr[0]).append(temporary)
        for i in range(1, l - 1):
            temporary = (arr[i + 1][k] - arr[i - 1][k]) / (2 * h)
            (arr[i]).append(temporary)
        temporary = (3 * arr[l - 1][k] - 4 * arr[l - 2][k] + arr[l - 3][k]) / (2 * h)
        (arr[l - 1]).append(temporary)
        k += 1


def start_method_taylor(k, q, table, x0):
    start = 0
    while True:
        if k <= table[start][0] <= q:
            x = table[start][1]
            t = methodtaylor(x, x0, table)
            r = exact_solution(x)
            print("Индекс: ", table[start][0], "Значение найденное методом Тейлора:", t)
            print("Абсолютная погрешность метода разложения в ряд Тейлора:",abs(t - r))
            print()
            start += 1
        else:
            break


def nice_conclusion_table_update(o):
    """Красивый вывод таблицы"""
    print("\n\nТаблица значений точного решения в равноотстоящих с шагом h точках.")
    print("Индексы :", end=" ")
    for i in o:
        print(reg(i[0]), end=" ")
    print("\n", "Узел    :", sep="", end=" ")
    for i in o:
        print(reg(i[1]), end=" ")
    print("\n", "Значение:", sep="", end=" ")
    for i in o:
        print(reg(i[2]), end=" ")
    print("\n", "D1      :", sep="", end=" ")
    for i in o:
        print(reg(i[3]), end=" ")
    print("\n", "D2      :", sep="", end=" ")
    for i in o:
        print(reg(i[4]), end=" ")
    print("\n", "D3      :", sep="", end=" ")
    for i in o:
        print(reg(i[5]), end=" ")
    print("\n", "D4      :", sep="", end=" ")
    for i in o:
        print(reg(i[6]), end=" ")
    print("\n", "D5      :", sep="", end=" ")
    for i in o:
        print(reg(i[7]), end=" ")
    print()


def reg(x):
    # Возвращает строчку из 20 символов
    const = 20
    s = str(x)
    n = const - len(s)
    for i in range(n):
        s = s + " "
    return s
