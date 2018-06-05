from Task6.Subtask23.storage import *


def f(x, y):
    # return -y * y + 1
    return -y + x


def methodAdamca(k, table, x0, table_up, h, q=2):
    #arr = start_method_taylor(k, q, table, x0, False)
    arr = []
    for i in range(0,5):
        arr.append([table[i][1],table[i][2]])
    #
    for i in range(3, len(table_up)):
        arr.append([table_up[i]])
    l = len(arr)

    def q(x):
        return h * f(arr[x][0], arr[x][1])

    def delta_q(x, n):
        if n == 0:
            return q(x)
        else:
            return delta_q(x + 1, n - 1) - delta_q(x, n - 1)

    for i in range(5, l):
        t = arr[i - 1][1] + q(i - 1) + 1 / 2 * delta_q(i - 2, 1) + 5 / 12 * delta_q(i - 3, 2) + 3 / 8 * delta_q(i - 4,3) + 251 / 720 * delta_q(i - 5, 4)
        (arr[i]).append(t)
    l = len(arr)
    print("Метод Адамса   4-го порядка")
    print(reg("Узел:"), end=" ")
    for i in range(l):
        print(reg(arr[i][0]), end=" ")
    print()
    print(reg("Значение:"), end=" ")
    for i in range(l):
        print(reg(arr[i][1]), end=" ")



def reg(x):
    # Возвращает строчку из 20 символов
    const = 20
    s = str(x)
    n = const - len(s)
    for i in range(n):
        s = s + " "
    return s

