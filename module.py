def binary_sum(m):
    return sum(int(digit) for digit in bin(m)[2:])

def log_2(m):
    return len(bin(m)[2:])

def is_self_number(n):
    if n == 0:
        return True
    start = max(1, n - int(log_2(n)) - 10)
    for m in range(start, n):
        if m + binary_sum(m) == n:
            return True
    return False