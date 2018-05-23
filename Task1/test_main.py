import unittest
from Task1.helper import *


class TestMethodsTask1(unittest.TestCase):
    A = -8 # левая граница
    B = 2 # правая граница
    eps = pow(10, -5) # погрешность
    eps_order = 5 # порядок погрешности
    info(A, B, eps)  # Выводит вводную информацию
    H = input_data(A, B)  # Возвращает шаг
    interval = roots_step(A, B, H, my_func)  # Отделение корней
    root = method_bisection(interval, my_func, eps, eps_order) # Находит корни методом Бисекции

    def test_Newton(self):
        root = methodNewton(self.interval, my_func, diff_my_func, diff_2_my_func, self.eps, self.eps_order)
        check = True
        if len(root) != len(self.root):
            check = False
        for i in range(len(root)):
            if abs(root[i] - self.root[i]) > self.eps:
                check = False
        self.assertTrue(check)

    def test_NewtonModification(self):
        root = methodNewtonModification(self.interval, my_func, diff_my_func, diff_2_my_func, self.eps, self.eps_order)
        check = True
        if len(root) != len(self.root):
            check = False
        for i in range(len(root)):
            if abs(root[i] - self.root[i]) > self.eps:
                check = False
        self.assertTrue(check)

    def test_Secant(self):
        root = methodSecant(self.interval, my_func, diff_my_func, diff_2_my_func, self.eps, self.eps_order)
        check = True
        if len(root) != len(self.root):
            check = False
        for i in range(len(root)):
            if abs(root[i] - self.root[i]) > self.eps:
                check = False
        self.assertTrue(check)
