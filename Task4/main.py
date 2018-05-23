from Task4.helper import *

A = -3
B = 1
M = 100
info(A, B, M)
A, B, M = set_data(A, B, M)

answer = i_my_func(A, B)

l = left_rectangle(A, B, M, my_func)
print("Левые: ", l, ";  Погрешность абсолютная фактическая равна: ", abs(l - answer))
print("Теор. погрешность: ", delta(1 / 2, A, B, 0, M), end="\n\n")

r = right_rectangle(A, B, M, my_func)
print("Правые: ", r, ";  Погрешность абсолютная фактическая равна: ", abs(r - answer))
print("Теор. погрешность: ", delta(1 / 2, A, B, 0, M), end="\n\n")

c = central_rectangle(A, B, M, my_func)
print("Средние: ", c, ";  Погрешность абсолютная фактическая равна: ", abs(c - answer))
print("Теор. погрешность: ", delta(1 / 24, A, B, 1, M), end="\n\n")

t = trapeze(A, B, M, my_func)
print("Трапеции: ", t, ";  Погрешность абсолютная фактическая равна: ", abs(t - answer))
print("Теор. погрешность: ", delta(1 / 12, A, B, 1, M), end="\n\n")

s = simpson(A, B, M, my_func)
print("Симпсон: ", s, ";  Погрешность абсолютная фактическая равна: ", abs(s - answer))
print("Теор. погрешность: ", delta(1 / 2880, A, B, 3, M), end="\n\n")
