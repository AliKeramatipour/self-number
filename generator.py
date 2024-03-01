from math import log

def binary_sum(m):
    return sum(int(digit) for digit in bin(m)[2:])

def log_2(m):
    return len(bin(m)[2:])

# Simple function to add to the substring dictionary
# while preserving their first appearance
def add_brick(bricks, word):
    bricks.add(word)
    word = word[::-1]
    bricks.add(word)

# Generates all possible Bricks
# n - length of the substring
def Brick_generator(seq, bricks, n):
    # adding all the bricks and their reverses to the dictionary
    l = 0
    while l < log_2(l + n + 1):
        add_brick(bricks, word=tuple(seq[l:l + n]))
        l += 1
    
# Generates all possible sub-brick pairs that are matching
def compatible_SubBrick_pairs(seq, bricks, n):
    # zero_extended_sequence
    z_seq = seq[:n].copy() + [False]*n
    for i in range(n):
        right = (z_seq[-i:] if (i > 0) else []) + z_seq[:n-i]
        for j in range(n):
            left = (z_seq[-j:] if (j > 0) else []) + z_seq[:n-j]
            left = left[::-1]
            dist = n - j - i - 1
            
            if dist < 0:
                continue
            mx_length = 2 ** (2 + dist) - 2
            if n - i > mx_length or n - j > mx_length:
                continue
            brick = [right[i] or left[i] for i in range(n)]
            add_brick(bricks, tuple(brick))

# Merging sub-bricks and bricks to generate all substrings
def merge_generator(seq, bricks, n):
    # if a Sub-Brick does not add something, it cannot add anything until the end
    z_seq = seq[:n].copy() + [False]*n
    for i in range(n):
        sub_brick = (z_seq[-i:] if (i > 0) else []) + z_seq[:n-i]
        # left-sided subbrick
        sub_brick = tuple(sub_brick[::-1])
        temporary_set = set()
        for word in bricks:
            new_word = [(word[j] or sub_brick[j]) for j in range(n)]
            add_brick(temporary_set, tuple(new_word))
        for key in temporary_set:
            bricks.add(key)

# Converts a boolean tuple into a binary string            
def binary(bool_tuple):
    result = ""
    for i in range(len(bool_tuple)):
        result += '1' if bool_tuple[i] else '0'
    return result

# Basics
# 2 3 5 8 11 17 24 35 51 68 85 104 126 148 172
LEN = 11
SZ = 10000
seq = [False] * SZ
for m in range(0, SZ):
    p = m + binary_sum(m)
    if p < SZ:
        seq[p] = True

Bricks = set()
Brick_generator(seq, Bricks, LEN)

compatible_SubBrick_pairs(seq, Bricks, LEN)
merge_generator(seq, Bricks, LEN)
print(len(Bricks))
for brick in Bricks:
    print(binary(brick))
