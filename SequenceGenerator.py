from Modules import *

N = 2000
f = Generate_Sequence(N)
f_str = ','.join(map(str, f))
print(f_str)