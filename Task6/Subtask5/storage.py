def f(x, y):
    return -y + x


def runge_kutta_4(x0, y0, h, table, N):
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + h / 2, y0 + k1 / 2)
    k3 = h * f(x0 + h / 2, y0 + k2 / 2)
    k4 = h * f(x0 + h, y0 + k3)
    l = N
    arr = []
    arr.append((x0, y0))
    for i in range(1, l):
        t = arr[i - 1][1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        arr.append((i, t))
        k1 = h * f(table[i], arr[i][1])
        k2 = h * f(table[i] + h / 2, arr[i][1] + k1 / 2)
        k3 = h * f(table[i] + h / 2, arr[i][1] + k2 / 2)
        k4 = h * f(table[i] + h, arr[i][1] + k3)

    print("\nМетод Рунге-Кутта")
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
