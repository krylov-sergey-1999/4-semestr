import math


def info(x0, k, N, h):
    """Выводит информацию о задаче."""
    print("Численное решение Задачи Коши для обыкновенного дифференциального уравнения первого порядка")
    print("y'(x) = - y^2(x) + 1")
    print("x0 =", x0)
    print("h =", h)
    print("N =", N)
    print("k =", k)
    print()


def set_initial_data():
    """Возвращает x0, k, N, h, table"""
    x0 = 0
    k = -2
    N = 10
    h = 0.1
    table = []
    for i in range(k, N):
        node = x0 + i * h
        table.append([i, node, exact_solution(node)])
    return x0, k, N, h, table


def exact_solution(x):
    # Точное решение
    y = (math.exp(2 * x) - 1) / (math.exp(2 * x) + 1)
    return y


def nice_conclusion_table(o):
    """Красивый вывод таблицы"""
    print("Таблица значений точного решения в равноотстоящих с шагом h точках.")
    print("Индексы :", end=" ")
    for i in o:
        print(reg(i[0]), end=" ")
    print("\n", "Узел    :", sep="", end=" ")
    for i in o:
        print(reg(i[1]), end=" ")
    print("\n", "Значение:", sep="", end=" ")
    for i in o:
        print(reg(i[2]), end=" ")
    print("\n")


def reg(x):
    # Возвращает строчку из 20 символов
    const = 20
    s = str(x)
    n = const - len(s)
    for i in range(n):
        s = s + " "
    return s
