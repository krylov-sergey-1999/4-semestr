import math


def info(a, b, x, n, m, func):
    """Выводит информацию о задаче. Названия и входные данные."""
    print("Задача алгебраического интерполирования. Интерполяционный многочлен в форме Ньютона и в форме Лагранжа")
    print("Тестовая задача.")
    print("f(x) = exp(-x) - pow(x, 2) / 2")
    print("[A; B] = [", a, ";", b, "]")
    print("x = ", x, "; n = ", n, "; m = ", m, "; f(x) = ", func(x))
    print("Узлов будет: ", m + 1)
    print("___________________________________________________________________")


def info_new(a, b, x, n, m, func):
    """Вторая функция для вывода информации о задаче. Дополнительная."""
    print("Начальные данные изменились. Обратите внимания на изменения!")
    print("f(x) = exp(-x) - pow(x, 2) / 2")
    print("[A; B] = [", a, ";", b, "]")
    print("x = ", x, "; n = ", n, "; m = ", m, "; f(x) = ", func(x))
    print("___________________________________________________________________")


def my_func(x):
    """Функция задачи."""
    return math.exp(-x) - pow(x, 2) / 2


def set_setting(a, b, x, n, m, func):
    """Устанавливает начальные параметры для задачи. Проверка на дурака минимальная."""
    check = int(input(
        "Если использовать начальные параметры нажмите 1, если ввести новые, нажмите 2: "))
    while True:
        if check == 1:
            print("Принято! Будут использованы стандартные параметры!")
            break
        elif check == 2:
            x = float(input("Введите \'x\': "))
            m = int(input("Введите \'m\': "))
            while True:
                n = int(input("Введите \'n\': "))
                if 0 <= n <= m:
                    break
                else:
                    print("Неверный ввод. Попробуйте заново.")
            info_new(a, b, x, n, m, func)
            break
        else:
            print("Неверный ввод, введите заново!")
    h = (b - a) / m
    return (x, m, n, h)


def step_one(a, b, x, n, m, h, nodes, table, func):
    """Подготовительный этап. Создание и вывод таблицы с узлами и значениями в узлах."""
    print("Шаг будет: ", h)
    start = a
    for i in range(m):
        nodes.append(start)
        start = start + h
    nodes.append(b)
    for i in nodes:
        table.append((i, func(i), abs(x - i)))
    print("___________________________________________________________________")


def reg(x):
    const = 20
    s = str(x)
    n = const - len(s)
    for i in range(n):
        s = s + " "
    return s


def print_table(t, check):
    if check:
        print("Результат после сортировки!")
    else:
        print("Таблица!")
    print("Node:        ", end='')
    for i in t:
        print(reg(i[0]), end="; ")
    print()
    print("f(node):     ", end='')
    for i in t:
        print(reg(i[1]), end="; ")
    print()
    print("abs(x-node): ", end='')
    for i in t:
        print(reg(i[2]), end="; ")
    print()
    print("___________________________________________________________________")


def node_selection(t, p):
    """" Сортировка по 3 значению аргумента таблицы. """
    t.sort(key=lambda x: x[p])


def i_A(q, w, t):
    if w - q != 1:
        return (i_A(q + 1, w, t) - i_A(q, w - 1, t)) / (t[w][0] - t[q][0])
    else:
        return (t[w][1] - t[q][1]) / (t[w][0] - t[q][0])


def methodNewton(x, n, t, func):
    P_n = 0
    difference = 1
    arr = []
    arr.append(t[0][1])
    for i in range(1, n + 1):
        memory = i_A(0, i, t)
        difference = difference * (x - t[i - 1][0])
        arr.append(memory * difference)
    for i in range(n + 1):
        P_n = P_n + arr[i]
    print("Метод Ньютона, мы получили: P_n = ", P_n)
    print("Погрешность равна |f(x) - P_n(x)| = ", abs(P_n - func(x)))
    print("___________________________________________________________________")
    return abs(P_n - func(x))


def i_Product(t, k, n, x):
    numerator = 1
    denominator = 1
    for i in range(n + 1):
        if i != k:
            numerator = numerator * (x - t[i][0])
        if i != k:
            denominator = denominator * (t[k][0] - t[i][0])
    return numerator / denominator


def methodLagrange(x, n, t, func):
    s = 0
    for i in range(n + 1):
        s = s + t[i][1] * i_Product(t, i, n, x)
    print("Метод Лагранжа, мы получили: P_n = ", s)
    print("Погрешность равна |f(x) - P_n(x)| = ", abs(s - func(x)))
    print("___________________________________________________________________")
    return abs(s - func(x))
