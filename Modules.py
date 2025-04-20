def binary_sum(m):
    if m < 0:
        raise ValueError("binary_sum is not defined for negative numbers")
    return sum(int(digit) for digit in bin(m)[2:])

def log_2(m):
    if m < 0:
        raise ValueError("log_2 is not defined for negative numbers")
    return len(bin(m)[2:])

def is_self_number(n):
    if n < 0:
        raise ValueError("is_self_number is not defined for negative numbers")
    if n == 0:
        return True
    start = max(1, n - int(log_2(n)) - 10)
    for m in range(start, n):
        if m + binary_sum(m) == n:
            return True
    return False

# Generate the first N elements of the sequence
def Generate_Sequence(N):
    f = [0] * N

    for m in range(0, N):
        n = m + binary_sum(m)
        if n < N:
            f[n] = 1
    return f