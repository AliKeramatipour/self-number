# Check Lemma `lemmaMid` first instances
from Modules import *

err = False
for n in range(1,10):
    fails = False
    for i in range(1, n):
        if is_self_number(2 ** n + i) != (is_self_number(i - 1) or is_self_number(n - i - 1)):
            print(f"ERROR: for {n} in {i}")
            fails = True
    if fails:
        err = True
        print(f"The Lemma fails for n = {n}:")
    else:
        print(f"The Lemma holds for n = {n}:")

if err:
    print("Error found")
else:
    print("Lemma holds.")