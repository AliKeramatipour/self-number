# Check and verify the whole Table's first instances
from Modules import *

err = False
for n in range(2,15):
    fails = False

    # Check Lemma `lemmaLeft` first instances
    for i in range(n - 1, 2**n + 1):
        inv = 2 ** n + n - 1 - i
        if is_self_number(i) != is_self_number(inv):
            print(f"ERROR: for {n} in {i}")
            fails = True
            break
    
    # Check Lemma 'mid' first instances
    for i in range(2**n + 1, 2**n + n):
        inv = 2 ** n + n - 1 - i
        sam = i - 2 ** n - 1
        if (is_self_number(inv) or is_self_number(sam)) != is_self_number(i):
            print(f"ERROR: for {n} in {i}")
            fails = True
            break

    # Check Lemma `lemmaRight` first instances
    for i in range(2**n + n, 2**(n + 1)):
        sam = i - 2 ** n - 1
        if is_self_number(i) != is_self_number(sam):
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