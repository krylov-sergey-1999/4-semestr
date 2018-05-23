import math


def i_my_func(a, b):
    return math.exp(b) - math.exp(a)


def my_func(x):
    return math.exp(x)


def info(a, b, m):
    """Вывод информации о задаче и начальные данные."""
    print("Приближённое вычисление интеграла по составным квадратурным формулам")
    print("Начальные данные [A; B] = [", a, ";", b, "]")
    print("M = ", m)
    print("f(x) = e^x")
    print("Значение интеграла по начальным данным равно: ", i_my_func(a, b))


def set_data(a, b, m):
    """Задание начальных данных."""
    A = a
    B = b
    M = m
    check = int(input("Введите 1, если хотите использовать начальные данные, и 2 если хотите ввести новые: "))
    if check == 1:
        print("Будут использованы начальные данные!")
    else:
        A = int(input("Введите A: "))
        while True:
            B = int(input("Введите B: "))
            if B < A:
                print("Ввод неверный. Введите заново!")
            else:
                break
        while True:
            M = int(input("Введите M: "))
            if M > 0:
                break
            else:
                print("Ввод неверный. Введите заново!")
        print("Новое ТОЧНОЕ значение интеграла равно: ", i_my_func(A, B))
    return A, B, M


def left_rectangle(a, b, m, func):
    # формула не является интерполяционной
    h = (b - a) / m
    s = 0
    d = 0
    for i in range(1, m + 1):
        s = s + func(a + (i - 1) * h)
    s = s * h
    return s


def right_rectangle(a, b, m, func):
    # формула не является интерполяционной
    h = (b - a) / m
    s = 0
    d = 0
    for i in range(1, m + 1):
        s = s + func((a + h) + (i - 1) * h)
    s = s * h
    return s


def central_rectangle(a, b, m, func):
    # формула не является интерполяционной
    h = (b - a) / m
    d = 1
    s = 0
    for i in range(1, m + 1):
        s = s + func((a + h / 2) + (i - 1) * h)
    s = s * h
    return s


def trapeze(a, b, m, func):
    h = (b - a) / m
    start = a
    table = []
    d = 1
    s = 0
    for i in range(m):
        table.append((start, func(start)))
        start += h
    table.append((b, func(b)))
    for i in range(m + 1):
        if (i != 0) and (i != m):
            s = s + 2 * table[i][1]
        else:
            s = s + table[i][1]
    s = s * (b - a) / (2 * m)
    return s


def simpson(a, b, m, func):
    h = (b - a) / (2 * m)
    start = a
    table = []
    d = 3
    s = 0
    for i in range((m * 2) + 1):
        table.append((start, func(start)))
        start += h
    for i in range((2 * m) + 1):
        if (i == 0) or (i == 2 * m):
            s = s + table[i][1]
        elif i % 2 == 1:
            s = s + 4 * table[i][1]
        elif (i % 2 == 0) and (i != 0) and (i != 2 * m):
            s = s + 2 * table[i][1]
    s = s * (b - a) / (6 * m)
    return s


def delta(const, a, b, d, m):
    answer = const * (b - a) * pow(((b - a) / m), d + 1) * math.exp(b)
    return answer
