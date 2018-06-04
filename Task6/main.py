from Task6.Subtask1.storage import *
from Task6.Subtask2.storage import *

x0, k, N, h, table = set_initial_data()
info(x0,k,N,h)
nice_conclusion_table(table)
diff(table, h)
#nice_conclusion_table_update(table)
start_method_taylor(k,2,table,x0)

#methodtaylor(1, x0, table)
#print(exact_solution(1))
# End Step 2
#