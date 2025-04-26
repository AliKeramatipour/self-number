# Check Lemma `lemmaRight` first instances
from Modules import *

err = False
for k in range(1,20):
    err = False
    for a in range(1, k):
        for c in range(1, k):
            b = k + a
            d = k + c
            # <a, b> and <c, d> are two strings of length k
            ab = Generate_Sequence(a, b)
            cd = Generate_Sequence(c, d)[::-1]
            mainLeft = 2 ** (b + c + 2) + 1 + a
            mainRight = 2 ** (b + c + 2) + 1 + b
            main = Generate_Sequence(mainLeft, mainRight)
            # Check if the two strings are equal
            if or_sequences(ab, cd) != main:
                print(f"ERROR: for {k} in {a}, {b}, {c}, {d}")
                err = True
                break
        if err:
            break
    if err:
        break
            
if err:
    print("Error found")
else:
    print("Lemma holds.")