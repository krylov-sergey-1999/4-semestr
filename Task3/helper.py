import math


def info(a, b, epsilon, m, n, h, f):
    """Выводит информацию о задаче. Названия и входные данные."""
    print("Задача обратного интерполирования.")
    print("f(x) = exp(-x) - pow(x, 2) / 2")
    print("[A; B] = [", a, ";", b, "]")
    print(" eps = ", epsilon)
    print("M =", m)
    print("Степень интерполяционного многочлена: N =", n)
    print("Шаг будет: H =", h)
    print("Значение функции F =", f)
    print("___________________________________________________________________")


def my_func(x):
    """Функция задачи."""
    return math.exp(-x) - pow(x,2) / 2


def my_func_d_1(x):
    return -x - math.exp(-x)


def my_func_d_2(x):
    return math.exp(-x) - 1

def set_setting(a, b, n, m, func):
    """Устанавливает начальные параметры для задачи. Проверка на дурака минимальная."""
    F = 0
    check = int(input("Введите 1 если использовать стандартные M,N. Введите 2 если ввести новые: "))
    if check == 1:
        print("Будут использованы стандартные входные данные!")
    else:
        while True:
            m = int(input("Введите значение m, будет m+1 узлов: "))
            if 0 < m:
                break
            else:
                print("Неправильное значение m, введите заново.")
        while True:
            n = int(input("Введите значение n, степень интерполяционного многочлена: "))
            if 0 <= n <= m:
                break
            else:
                print("Неправильное значение n, введите заново.")
    nodes = []
    h = (b - a) / m
    print("Шаг будет: ", h)
    start = a
    for i in range(m):
        nodes.append((start, func(start)))
        start = start + h
    nodes.append((b, func(b)))
    print("Node    : ", end="")
    for i in nodes:
        print(reg(i[0]), end=" ")
    print()
    print("f(Node) : ", end="")
    for i in nodes:
        print(reg(i[1]), end=" ")
    print()
    while True:
        F = float(input("Введите значение F, значение которое принимает наша функция: "))
        if (func(a) <= F <= func(b)) or (func(a) >= F >= func(b)):
            break
        else:
            print("Такого f(x) нет в данном промежутке [A; B], введите заново.")
    print("___________________________________________________________________")
    return F, n, m, h


def info_new(a, b, n, m, f, h, epsilon):
    print("[A, B] = [", a, "; ", b, "]")
    print("N = ", n, "; M = ", m)
    print("F = ", f, "; H = (B - A) / M = ", h, "; eps = ", epsilon)
    print("Узлов будет: ", m + 1)
    print("___________________________________________________________________")


def step_one(a, b, m, f, h, func):
    """Подготовительный этап. Создание и вывод таблицы с узлами и значениями в узлах.
    output: возвращает таблицу, ее описание в документации
    """
    nodes = []
    table = []
    print("Шаг будет: ", h)
    start = a
    for i in range(m):
        nodes.append(start)
        start = start + h
    nodes.append(b)
    for i in nodes:
        table.append((func(i), i, abs(func(i) - f)))
    print("___________________________________________________________________")
    print_table(False, table)  # вывод таблицы до сортировки
    return table


def reg(x):
    const = 20
    s = str(x)
    n = const - len(s)
    for i in range(n):
        s = s + " "
    return s


def print_table(check, t):
    if check:
        print("Результат после сортировки!")
    else:
        print("Таблица!")
    print("f(node):     ", end='')
    for i in t:
        print(reg(i[0]), end="; ")
    print()
    print("Node:        ", end='')
    for i in t:
        print(reg(i[1]), end="; ")
    print()
    print("|F-f(node)|: ", end='')
    for i in t:
        print(reg(i[2]), end="; ")
    print()
    print("___________________________________________________________________")


def node_selection(t, k):
    """" Сортировка по k значению элемента таблицы t."""
    t.sort(key=lambda x: x[k])


def i_A(q, w, t):
    if w - q != 1:
        return (i_A(q + 1, w, t) - i_A(q, w - 1, t)) / (t[w][0] - t[q][0])
    else:
        return (t[w][1] - t[q][1]) / (t[w][0] - t[q][0])


def methodNewton(F, n, t, func):
    Q_n = 0
    difference = 1
    arr = []
    arr.append(t[0][1])
    for i in range(1, n + 1):
        memory = i_A(0, i, t)
        difference = difference * (F - t[i - 1][0])
        arr.append(memory * difference)
    for i in range(n + 1):
        Q_n = Q_n + arr[i]
    print("Метод Ньютона, мы получили: Q_n = ", Q_n)
    print("Погрешность(невязка) равна |F - f(Q_n)| = ", abs(func(Q_n) - F))
    print("___________________________________________________________________")
    return abs(F - func(Q_n))


def i_Product(t, k, n, x):
    numerator = 1
    denominator = 1
    for i in range(n + 1):
        if i != k:
            numerator = numerator * (x - t[i][1])
        if i != k:
            denominator = denominator * (t[k][1] - t[i][1])
    return numerator / denominator


def methodLagrange(x, n, t, func):
    s = 0
    for i in range(n + 1):
        s = s + t[i][0] * i_Product(t, i, n, x)
    return s


def my_func_modern(x, t, n, f):
    memory = methodLagrange(x, n, t, my_func)
    return memory - f


def roots_step(a, b, h, func, t, n, f):
    """"Отделение корней.
    input: принимает границы, шаг , функцию
    output: возвращает лист интервалов в которых есть корень
    """
    arr = []  # Лист интервалов
    l = a  # левая граница, будем ее двигать
    r = l + h  # правая граница, будем ее двигать
    while l < r:
        y_1 = func(l, t, n, f)
        y_2 = func(r, t, n, f)
        if y_1 * y_2 <= 0:
            arr.append((l, r))
            l = r
            r = r + h
        else:
            l = r
            r = r + h
        if r > b:
            r = b
        if l > b:
            l = b
    return arr


def method_bisection(interval_root, func, t, n, f, epsilon=pow(10, -8), order_epsilon=8):
    """Метод Бисекции. Для нахождения корней
    input: лист интервалов в которых есть корень , погрешность с которой ищем(epsilon), порядок этой погрешности и функцию
    output: лист корней
    """
    print("Метод Бисекции: ")
    counter = 0
    root = []  # Лист корней
    for i in interval_root:
        counter += 1
        a = i[0]
        b = i[1]
        step = 0
        while True:
            step += 1
            c = (a + b) / 2
            if func(a, t, n, f) * func(c, t, n, f) <= 0:
                b = c
            else:
                a = c
            if b - a > epsilon:
                pass
            else:
                break
        X = (a + b) / 2
        delta = (b - a) / 2
        m_fX = abs(func(X, t, n, f))
        print("Корень №", counter, " | Начальные приближения : ", i[0], " ; ", i[1], " | Количество шагов : ", step)
        print("X = ", X, "; delta = ", delta) # , " ; |f(X)-0| = ", m_fX
        root.append(X)
    print("___________________________________________________________________")
    return root


def print_discrepancy(root, func, f):
    for i in root:
        print("Невязка для корня: ", i, " равна |f(root) - F| = ", abs(func(i) - f))
    print("___________________________________________________________________")


def step_two(a, b, h, m, func, func_d, func_d_2):
    print("Формулы численного дифференцирования")
    print("Шаг : ", h, "; Погрешность может быть: ", h * h)
    nodes = []
    table = []  # x_i , f(x_i)
    table_d = []  # f'(x_i) ЧД , |f'(x_i) ЧД - f'(x_i) Т|
    table_d_2 = []  # f''(x_i) ЧД , |f''(x_i) ЧД - f''(x_i) Т|
    start = a
    for i in range(m + 1):
        nodes.append(start)
        table.append((start, func(start)))
        start += h

    for i in range(0, m+1):
        if i == m:
            f_d_1 = (table[i][1] - table[i-1][1]) / h
            memory = func_d(table[i][0])
            table_d.append((f_d_1, abs(f_d_1 - memory)))
        else:
            f_d_1 = (table[i+1][1] - table[i][1]) / h
            memory = func_d(table[i][0])
            table_d.append((f_d_1, abs(f_d_1 - memory)))

    for i in range(1, len(table) - 1):
        memory = (table[i + 1][1] + table[i - 1][1] - 2 * table[i][1]) / (h * h)
        table_d_2.append((memory, abs(memory - func_d_2(table[i][0]))))

    for i in table:
        print("x_i =", i[0], "; f(x_i)=", i[1])
    for i in table_d:
        print("f'(x_i) ЧД =", i[0], "; abs(f'(x_i)т - f'(x_i)ЧД)=", i[1])
    for i in table_d_2:
        print("f''(x_i) ЧД =", i[0], "; abs(f''(x_i)т - f''(x_i)ЧД)=", i[1])
