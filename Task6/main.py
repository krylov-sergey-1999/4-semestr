from Task6.Subtask1.storage import *
from Task6.Subtask23.storage import *
from Task6.Subtask6.storage import *
from Task6.Subtask5.storage import *
from Task6.Subtask4.storage import*

x0, y0, k, N, h, table = set_initial_data()
table_up = table_update(table, k) # Таблица для методов Эйлера Значений

info(x0, y0, k, N, h)
nice_conclusion_table(table)
diff(table, h)
#start_method_taylor(k, 2, table, x0,True)
table_rez = []
method_Euler(x0, y0, h, table_up, N,table_rez)
method_Euler_update(x0, y0, h, table_up, N,table_rez)
method_Euler_update_two(x0, y0, h, table_up, N,table_rez)
runge_kutta_4(x0,y0,h,table_up,N,table_rez)
methodAdamca(k,table,x0,table_up,h,table_rez)

print("\n")
print("Абсолютная погрешность метода Эйлера равна:" , abs(table_rez[0]-table[-1][2]))
print("Абсолютная погрешность метода Эйлера-Update равна:" , abs(table_rez[1]-table[-1][2]))
print("Абсолютная погрешность метода Эйлера-Коши равна:" , abs(table_rez[2]-table[-1][2]))
print("Абсолютная погрешность метода Р-К равна:" , abs(table_rez[3]-table[-1][2]))
print("Абсолютная погрешность метода Адамся равна:" , abs(table_rez[4]-table[-1][2]))
