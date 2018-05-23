from Task5.helper import *

A = 0
B = 1
M = 100
info(A, B, M)
m0 = False
m1 = False
m2 = False
m3 = False
arr = [m0, m1, m2, m3]
for i in range(len(arr)):
    try:
        my_func_w_x(A, i)
        my_func_w_x(B, i)
        arr[i] = simpson(A, B, M, my_func_w_x, i)
        # print("Симпсон")
    except:
        arr[i] = central_rectangle(A, B, M, my_func_w_x, i)
        # print("Центр")
m0, m1, m2, m3 = arr
G, H = decision_system(m1, m2, m0, m1, -m2, -m3)
X_1, X_2 = decision_system_type_2(1, G, H)
A_1, A_2 = decision_system(1, X_1, 1, X_2, m0, m1)

print("________________________________________________________________________________________")
result = method_gauss(A, B, M, my_func_f_w) # Параграф 7.3.1
print("Интеграл от функции f(x) решенный при помощи составной КФ Гаусса с двумя узлами с числом промежутков деления [a, b] равным m равен: ",result)
print("________________________________________________________________________________________")
control_type_1(A, B, X_1, X_2)
control_type_2(A_1, A_2)
# control_type_3(m3, A_1, A_2, X_1, X_2)

result = A_1 * my_func_f(X_1) + A_2 * my_func_f(X_2)  # КФ типа Гаусса с двумя узлами. Параграф 7.2
print("Моменты весовой функции равны: ")
print("    m0 = ", m0)
print("    m1 = ", m1)
print("    m2 = ", m2)
print("    m3 = ", m3)
print("Ортогональный многочлен: x^2+",G,"* x +",H)
print("Узлы: X_1 =",X_1,"; X_2 =",X_2)
print("Коэффиценты КФ: A_1 =",A_1,"; A_2 =",A_2)
print("Интеграл равен: ", result, " по КФ типа Гаусса с двумя узлами.")
