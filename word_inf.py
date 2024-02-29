def binary_sum(m):
    return sum(int(digit) for digit in bin(m)[2:])

N = 1000
f = [0] * N

for m in range(0, N):
    n = m + binary_sum(m)
    if n < N:
        f[n] = 1

# Convert the sequence list to a string for easy display
all_one = True
cnt = 0
mx = 0
for i in range(N - 1):
    if f[i] == 0 and f[i + 1] == 0:
        print(i, i + 1)

# print(mx)
f_str = ''.join(map(str, f))
print(f[21])
print(f_str)