import unittest
from Task2.helper import *


class TestMethodsTask2(unittest.TestCase):
    A = 0  # Левая граница отрезка
    B = 1  # Правая граница
    X = 0.65  # Точка в которой будем приближенно искать
    N = 7  # степень интерполяционного многочлена
    M = 15  # Будет m+1 узел
    H = (B-A)/M  # Шаг
    eps = pow(10, -5)
    nodes = []  # Лист узлов их координаты
    table = []  # Описание в документации
    info(A, B, X, N, M, my_func)  ## Вывод информации, о том что мы делаем.
    step_one(A, B, X, N, M, H, nodes, table, my_func)  # Подготовительный этап меняет таблицы, просто дает ознакомительную информацию
    print_table(table, False) # выводим таблицу
    nodes = [] # обнуляем, ибо мы их изменили, а для дальнейшей работы нам требуется чтобы они были пустыми (типо начинаем с чистого листа)
    table = [] # обнуляем, ибо мы их изменили, а для дальнейшей работы нам требуется чтобы они были пустыми (типо начинаем с чистого листа)
    X, M, N, H = set_setting(A, B, X, N, M, my_func)  # Установление начальных параметров
    step_one(A, B, X, N, M, H, nodes, table, my_func)  # Подготовительный этап
    print_table(table, False)
    node_selection(table, 2)  # Сортировка
    print_table(table, True)
    fallibility_one = methodNewton(X, N, table, my_func)
    fallibility_two = methodLagrange(X, N, table, my_func)

    def test_Newton(self):
        check = True
        if self.fallibility_one > self.eps:
            check = False
        self.assertTrue(check)

    def test_Lagrange(self):
        check = True
        if self.fallibility_two > self.eps:
            check = False
        self.assertTrue(check)
