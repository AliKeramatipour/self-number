# Check Lemma `lemmaLeft` first instances
from module import *

err = False
for n in range(2,20):
    for i in range(n-1, 2**n + 1):
        inv = 2 ** n + n - 1 - i
        if is_self_number(i) != is_self_number(inv):
            print(f"ERROR: for {n} in {i}")

if err:
    print("Error found")