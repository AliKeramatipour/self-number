from math import log

def binary_sum(m):
    return sum(int(digit) for digit in bin(m)[2:])

# Whether n is a self-number or not
def is_self_number(n):
    start = max(1, n - int(log(n)))
    for m in range(start, n):
        if m + binary_sum(m) == n:
            print(f"{m}: {bin(m)[2:]} -> generates {n}")
            return True
    return False

# Generates all possible Bricks
# n - length of the substring
# def Brick_generator(n):
    


n = 21
print(is_self_number(20)) 