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
        return False
    start = max(1, n - int(log_2(n)) - 10)
    for m in range(start, n):
        if m + binary_sum(m) == n:
            return False
    return True

# Generate the first N elements of the sequence
def Generate_First_Elements_Sequence(N):
    f = [0] * N

    for m in range(0, N):
        n = m + binary_sum(m)
        if n < N:
            f[n] = 1
    return ''.join(str(x) for x in f)


def Generate_Sequence(l, r=None, flag=None):
    # If r is None, interpret as Generate_Sequence(0, l)
    if r is None:
        r = l
        l = 0
    
    N = r - l + 1
    f = [0] * N

    start = max(0, l - log_2(l) * 2)

    for m in range(start, r + 1):
        n = m + binary_sum(m)
        if l <= n <= r:
            f[n - l] = 1

    sequence = ''.join(str(x) for x in f)
    
    if flag == 'DEC':
        for i in range(N):
            print(f"{l + i} → {sequence[i]}")
    
    return sequence

def or_sequences(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have the same length")
    return ''.join('1' if a == '1' or b == '1' else '0' for a, b in zip(seq1, seq2))