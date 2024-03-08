def binary_sum(m):
    return sum(int(digit) for digit in bin(m)[2:])

N = 100000
f = [0] * N

for m in range(0, N):
    n = m + binary_sum(m)
    if n < N:
        f[n] = 1

def count_unique_substrings(f, window_size = 20):
    unique_sequences = set()
    for i in range(len(f) - window_size + 1):
        window = tuple(f[i:i+window_size])  # Convert the window to a tuple so it can be added to a set
        unique_sequences.add(window)
    return len(unique_sequences)


for i in range(15):
    ans = count_unique_substrings(f, i)
    print(ans)