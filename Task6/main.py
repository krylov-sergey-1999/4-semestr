from Task6.Subtask1.storage import *
from Task6.Subtask23.storage import *
from Task6.Subtask6.storage import *

x0,y0, k, N, h, table = set_initial_data()
info(x0, k, N, h)
nice_conclusion_table(table)
diff(table, h)
#start_method_taylor(k, 2, table, x0)
method_Euler(y0,h,table,N)
method_Euler_update(x0,y0,h,table,N)
method_Euler_update_two(x0,y0,h,table,N)