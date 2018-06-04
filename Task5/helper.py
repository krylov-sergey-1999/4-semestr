import math


def info(a, b, m):
    print("Вычисление интегралов при помощи квадратурных формул Наивысшей Алгебраической Степени Точности (КФ НАСТ)")
    print("Начальные данные [A; B] = [", a, ";", b, "]")
    print("M = ", m)
    print("f(x) = math.sin(x)")
    print("w(x) = 1/pow(x,1/4)")


def my_func_f(x):
    return math.sin(x)


def my_func_w(x):
    return 1/pow(x,1/4)

def my_func_f_w(x):
    return my_func_f(x)*my_func_w(x)


def my_func_w_x(x, k, f=my_func_w):
    return f(x) * pow(x, k)


def decision_system(a1, a2, b1, b2, e1, e2):
    """Решение системы линейных уравнений из 2 штук с 2 неизвестными."""
    determinant = a1 * b2 - a2 * b1
    if determinant != 0:
        determinant_x = e1 * b2 - e2 * b1
        determinant_y = a1 * e2 - a2 * e1
        x = determinant_x / determinant
        y = determinant_y / determinant
        return x, y
    else:
        print("Дискриминант отрицательный.")


def decision_system_type_2(a, b, c):
    """Решение квадратного уравнения."""
    D = b * b - 4 * a * c
    if D < 0:
        print("Дискрименант меньше нуля.\n")
    x_1 = (-b + math.sqrt(D)) / (2 * a)
    x_2 = (-b - math.sqrt(D)) / (2 * a)
    return x_1, x_2


def control_type_1(a, b, x_1, x_2):
    """Контроль найденных переменных."""
    check = 0
    if (x_1 != x_2) and (a <= x_1 <= b) and (a <= x_2 <= b):
        print("Контроль корней пройден!")
    else:
        print("Контроль корней не пройден.")


def control_type_2(a_1, a_2):
    """Контроль A_1, A_2"""
    if a_1 * a_2 > 0:
        print("Контроль коэффицентов А_1 и А_2 пройден!")
    else:
        print("Контроль коэффицентов А_1 и А_2 не пройден.")


def control_type_3(m3, a1, a2, x1, x2):
    """Проверка при f(x) = x^3"""
    res = abs(m3 - a1 * pow(x1, 3) - a2 * pow(x2, 3))
    if res < pow(10, 8):
        print("Проверка пройдена, погрешность около машинного нуля!")
    else:
        print("Проверка не пройдена! Погрешность больше машинного нуля!")


def simpson(a, b, m, func, k):
    h = (b - a) / (2 * m)
    start = a
    table = []
    d = 3
    s = 0
    for i in range((m * 2) + 1):
        table.append((start, func(start, k)))
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


def central_rectangle(a, b, m, func, k):
    # формула не является интерполяционной
    h = (b - a) / m
    d = 1
    s = 0
    for i in range(1, m):
        s = s + func(((a + h / 2) + (i - 1) * h), k)
    s = s * h
    return s


def method_gauss(a, b, m, func):
    """"Вычисление интеграла при помощи составной КФ Гаусса с двумя узлами с числом промежутков деления [a, b] равным m
    Весовая функция в данном случае равна 1
    [a, b] = [−1, 1]. Узлы — корни многочлена Лежандра.
    """
    h = (b - a) / m
    arr = []
    s = 0
    t_1 = 1 / math.sqrt(3)
    t_2 = - 1 / math.sqrt(3)
    for i in range(m + 1):
        z = a + i * h
        arr.append(z)
    for i in range(m):
        z = (arr[i] + arr[i + 1]) / 2
        s = s + func(h / 2 * t_1 + z) + func(h / 2 * t_2 + z)
    s = s * h / 2
    return s