# Check Lemma `lemmaRight` first instances
from Modules import *

err = False
for n in range(1,15):
    fails = False
    for i in range(n-1, 2**n - 2):
        if is_self_number(2**n + 1 + i) != is_self_number(i):
            print(f"ERROR: for {n} in {i}")
            fails = True
            break
    if fails:
        err = True
        print(f"The Lemma fails for n = {n}:")
    else:
        print(f"The Lemma holds for n = {n}:")
            

if err:
    print("Error found")
else:
    print("Lemma holds.")