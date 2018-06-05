from Task6.Subtask1.storage import *
from Task6.Subtask23.storage import *
from Task6.Subtask6.storage import *
from Task6.Subtask5.storage import *

x0, y0, k, N, h, table = set_initial_data()
table_up = table_update(table, k) # Таблица для методов Эйлера Значений
info(x0, y0, k, N, h)
nice_conclusion_table(table)
diff(table, h)
# start_method_taylor(k, 2, table, x0)
#method_Euler(x0, y0, h, table_up, N)
#method_Euler_update(x0, y0, h, table_up, N)
#method_Euler_update_two(x0, y0, h, table_up, N)

#runge_kutta_4(x0,y0,h,table_up,N)
