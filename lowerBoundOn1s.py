# The aim is to find the first instance of strings 1^i in the sequence.
from Modules import *
import re

N = 2000
f = Generate_First_Elements_Sequence(N)
match = re.search('1{20}', f)
if match:
    print("Found at index:", match.start())
else:
    print("Not found")

# print(f)