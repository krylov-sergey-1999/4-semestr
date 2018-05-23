import math


def info(a, b, epsilon):
    print("ЧИСЛЕННЫЕ МЕТОДЫ РЕШЕНИЯ НЕЛИНЕЙНЫХ УРАВНЕНИЙ")
    print("f(x) = 10 * cos(x) - 0.1 * x^2")
    print("[A; B] = [", a, ";", b, "]")
    print("eps = ", epsilon)
    print("___________________________________________________________________")


def my_func(x, order_epsilon=5):
    """Возвращает значение функции.
    input: принимает аргумент и порядок точности(order_epsilon)
    output: возвращает значение
    """
    return 10 * math.cos(x) - 0.1 * x * x


def diff_my_func(x, order_epsilon=5):
    """Возвращает значение производной функции.
    input: принимает аргумент и порядок точности(order_epsilon)
    output: возвращает значение
    """
    return -0.2 * x - 10 * math.sin(x)


def diff_2_my_func(x, order_epsilon=5):
    """Возвращает значение второй производной функции.
    input: принимает аргумент и порядок точности(order_epsilon)
    output: возвращает значение
    """
    return -10 * math.cos(x) - 0.2


def input_data(A, B):
    """"Ввод данных и определение шага.
    input: принимает границы
    output: возвращает шаг
    """
    H = 0
    while True:
        check = int(
            input("Если хотите ввести N (кол-во шагов) нажмите 1, если хотите ввести шаг H = (B-A)/N введите 2: "))
        if check == 1:
            N = float(input("Введите N: "))
            H = (B - A) / N
            print("Получаются шаги размера: ", H)
            break
        elif check == 2:
            H = float(input("Введите H: "))
            break
        else:
            print("Неверный ввод. Введите заново!")
    print("___________________________________________________________________")
    return H


def roots_step(a, b, h, func):
    """"Отделение корней.
    input: принимает границы, шаг , функцию
    output: возвращает лист интервалов в которых есть корень
    """
    arr = []  # Лист интервалов
    l = a  # левая граница, будем ее двигать
    r = l + h  # правая граница, будем ее двигать
    while l < r:
        y_1 = func(l)
        y_2 = func(r)
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


def method_bisection(interval_root, func, epsilon=pow(10, -5), order_epsilon=5):
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
            if func(a) * func(c) <= 0:
                b = c
            else:
                a = c
            if b - a > epsilon:
                pass
            else:
                break
        X = (a + b) / 2
        delta = (b - a) / 2
        m_fX = abs(func(X))
        print("Корень №", counter, " | Начальные приближения : ", i[0], " ; ", i[1], " | Количество шагов : ", step)
        print("X = ", X, "; delta = ", delta, " ; |f(X)-0| = ", m_fX)
        root.append(X)
    print("___________________________________________________________________")
    return root


def methodNewton(interval_root, func, d_1_func, d_2_func, epsilon=pow(10, -5), order_epsilon=5):
    """Метод Ньютона. Для нахождения корней
        input: лист интервалов в которых есть корень , функцию , функцию являющейся ее первой производной,
         функцию являющейся ее второй производной, погрешность с которой ищем(epsilon), порядок этой погрешности
        output: лист корней
    """
    print("\nМетод Ньютона (метод касательных): ")
    counter = 0
    root = []
    for i in interval_root:
        counter += 1
        check = 0
        step = 0
        a = i[0]
        b = i[1]
        x_0 = False
        if abs(func(a) - 0) < epsilon:
            print("Число :", a, "является корнем(а)")
            check += 1
        if abs(func(b) - 0) < epsilon:
            print("Число :", b, "является корнем(b)")
            check += 1
        if check == 0:
            if func(a) * d_2_func(a) > 0:
                x_0 = a
            if func(b) * d_2_func(b) > 0:
                x_0 = b
            if x_0 == False:
                x_0 = (a + b) / 2
            x_1 = x_0 - func(x_0) / d_1_func(x_0)
            step += 1
            while abs(x_1 - x_0) > epsilon:
                step += 1
                x_0 = x_1
                x_1 = x_0 - func(x_0) / d_1_func(x_0)
            delta = abs(x_1 - x_0)
            X = x_1
            root.append(X)
            m_fX = abs(func(X))
            print("Корень №", counter, " | Начальные приближения : ", i[0], " ; ", i[1], " | Количество шагов : ", step)
            print("X = ", X, "; delta = ", delta, " ; |f(X)-0| = ", m_fX)
    print("___________________________________________________________________")
    return root


def methodNewtonModification(interval_root, func, d_1_func, d_2_func, epsilon=pow(10, -5), order_epsilon=5):
    """Метод Ньютона Модифицированный. Для нахождения корней
    input: лист интервалов в которых есть корень , функцию , функцию являющейся ее первой производной,
         функцию являющейся ее второй производной, погрешность с которой ищем(epsilon), порядок этой погрешности
    output: лист корней
    """
    print("\nМетод Ньютона Модификация: ")
    counter = 0
    root = []
    for i in interval_root:
        counter += 1
        check = 0
        step = 0
        a = i[0]
        b = i[1]
        x_0 = False
        if abs(func(a) - 0) < epsilon:
            print("Число :", a, "является корнем(а)")
            check += 1
        if abs(func(b) - 0) < epsilon:
            print("Число :", b, "является корнем(b)")
            check += 1
        if check == 0:
            if func(a) * d_2_func(a) > 0:
                x_0 = a
            if func(b) * d_2_func(b) > 0:
                x_0 = b
            if x_0 == False:
                x_0 = (a + b) / 2
            x_1 = x_0 - func(x_0) / d_1_func(x_0)
            step += 1
            memory = x_0
            while abs(x_1 - memory) > epsilon:
                step += 1
                memory = x_1
                x_1 = x_1 - func(x_1) / d_1_func(x_0)
            delta = abs(x_1 - x_0)
            X = x_1
            root.append(X)
            m_fX = abs(func(X))
            print("Корень №", counter, " | Начальные приближения : ", i[0], " ; ", i[1], " | Количество шагов : ", step)
            print("X = ", X, "; delta = ", delta, " ; |f(X)-0| = ", m_fX)
    print("___________________________________________________________________")
    return root


def methodSecant(interval_root, func, d_1_func, d_2_func, epsilon=pow(10, -5), order_epsilon=5):
    """Метод Ньютона Модифицированный. Для нахождения корней
    input: лист интервалов в которых есть корень , функцию , функцию являющейся ее первой производной,
             функцию являющейся ее второй производной, погрешность с которой ищем(epsilon), порядок этой погрешности
    output: лист корней
    """
    print("Метод Секущих: ")
    counter = 0
    root = []
    for i in interval_root:
        counter += 1
        check = 0
        step = 0
        a = i[0]
        b = i[1]
        x_0 = False
        if abs(func(a) - 0) < epsilon:
            print("Число :", a, "является корнем(а)")
            check += 1
        if abs(func(b) - 0) < epsilon:
            print("Число :", b, "является корнем(b)")
            check += 1
        if check == 0:
            if func(a) * d_2_func(a) > 0:
                x_0 = a
            if func(b) * d_2_func(b) > 0:
                x_0 = b
            if x_0 == False:
                x_0 = (a + b) / 2
            x_1 = x_0 - func(x_0) / d_1_func(x_0)
            step += 1
            while abs(x_1 - x_0) > epsilon:
                step += 1
                memory = x_1
                x_1 = x_1 - func(x_1) * (x_1 - x_0) / (func(x_1) - func(x_0))
                x_0 = memory

            delta = abs(x_1 - x_0)
            X = x_1
            root.append(X)
            m_fX = abs(func(X))
            print("Корень №", counter, " | Начальные приближения : ", i[0], " ; ", i[1], " | Количество шагов : ", step)
            print("X = ", X, "; delta = ", delta, " ; |f(X)-0| = ", m_fX)
    print("___________________________________________________________________")
    return root
