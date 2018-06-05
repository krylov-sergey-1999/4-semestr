def f(x, y):
    #return -y * y + 1
    return -y + x


def method_Euler(x0,y0, h, table, N):
    arr = []
    l = N
    arr.append((x0, y0))
    for i in range(1, l):
        t = arr[i - 1][1] + h * f(table[i - 1], arr[i - 1][1])
        arr.append((i, t))

    print("\nМетод Эйлера")
    print(reg("Узел:"), end=" ")
    for i in range(1, l):
        print(reg(i), end=" ")
    print()
    print(reg("Значение:"), end=" ")
    for i in range(1, l):
        print(reg(arr[i][1]), end=" ")


def method_Euler_update(x0, y0, h, table, N):
    arr = []
    l = N
    arr.append((x0, y0))
    y_middle = y0 + h / 2 * f(x0, y0)
    for i in range(1, l):
        t = arr[i - 1][1] + h * f(table[i - 1] + h / 2, y_middle)
        arr.append((i, t))
        y_middle = arr[i][1] + h / 2 * f(table[i], arr[i][1])
    print("\n\nМетод Эйлера Update")
    print(reg("Узел:"), end=" ")
    for i in range(1, l):
        print(reg(i), end=" ")
    print()
    print(reg("Значение:"), end=" ")
    for i in range(1, l):
        print(reg(arr[i][1]), end=" ")


def method_Euler_update_two(x0, y0, h, table, N):
    arr = []
    l = N
    arr.append((x0, y0))
    Y = y0 + h * f(x0, y0)
    for i in range(1, l):
        t = arr[i - 1][1] + h / 2 * (f(table[i - 1],arr[i - 1][1]) + f(table[i],Y))
        arr.append((i, t))
        Y = arr[i][1] + h * f(table[i],arr[i][1])

    print("\n\nМетод Эйлера Эйлера-Коши")
    print(reg("Узел:"), end=" ")
    for i in range(1, l):
        print(reg(i), end=" ")
    print()
    print(reg("Значение:"), end=" ")
    for i in range(1, l):
        print(reg(arr[i][1]), end=" ")



def reg(x):
    # Возвращает строчку из 20 символов
    const = 20
    s = str(x)
    n = const - len(s)
    for i in range(n):
        s = s + " "
    return s
