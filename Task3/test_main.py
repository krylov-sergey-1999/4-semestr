import unittest
from Task3.helper import *
import Task2.helper


class TestMethodsTask3(unittest.TestCase):
    A = 0  # Левая граница отрезка
    B = 1  # Правая граница
    M = 10  # Будет m+1 узел
    N = 10  # Степень интерполяционного многочлена
    H = (B - A) / M
    F = 0  # значение функции f при неизвестном аргументе
    eps = pow(10, -8)
    eps_order = -8
    discrepancy = pow(10, -5)
    info(A, B, eps, M, N, H, F)  # вывод информации начальной
    table = step_one(A, B, M, F, H, my_func)  # создание таблицы
    #table = []
    F, N, M, H = set_setting(A, B, N, M, my_func)  # устанавливаем начальные параметры
    info_new(A, B, N, M, F, H, eps)  # выводим новую информацию
    table = step_one(A, B, M, F, H, my_func)  # создание таблицы
    node_selection(table, 2)  # сортировка
    print_table(True, table)  # вывод таблицы после сортировки
    fallibility = methodNewton(F, N, table, my_func)  # Погрешность == Невязка
    interval = roots_step(A, B, H, my_func_modern, table, N,
                          F)  # Отделение корней с шагом H используя нашу модифицированную функцию
    roots = method_bisection(interval, my_func_modern, table, N, F, eps, eps_order)  # Находит корни методом Бисекции
    print_discrepancy(roots, my_func, F)  # выводит корни и невязки для них
    step_two(A, B, H, M, my_func, my_func_d_1, my_func_d_2)  # Формулы численного дифференцирования

    def test_Newton(self):
        check = True
        if self.fallibility > self.discrepancy:
            check = False
        self.assertTrue(True)

    def test_Method_number_two(self):
        check = True
        for i in self.roots:
            if abs(my_func(i) - self.F) > self.discrepancy:
                check = False
        self.assertTrue(True)
