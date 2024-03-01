from math import log

def binary_sum(m):
    return sum(int(digit) for digit in bin(m)[2:])

def log_2(m):
    return len(bin(m)[2:])

# Whether n is a self-number or not
def is_self_number(n):
    if n == 0:
        return True
    start = max(1, n - int(log_2(n)) - 10)
    for m in range(start, n):
        if m + binary_sum(m) == n:
            # print(f"{m}: {bin(m)[2:]} -> generates {n}")
            return True
    return False

# Simple function to add to the substring dictionary
# while preserving their first appearance
def add_brick(bricks, word, add_rev = 1, first = -1, last = -1):
    
    if first == -1:
        first = last - len(word) + 1
    print(f"Initial first {first} and last {last}")
    last = first + len(word) - 1
    if word not in bricks or first < bricks[word]:
        verify(word, first, id = 'add_actual_brick')
        bricks[word] = first

    if not add_rev:
        return
    
    word = word[::-1]
    l = first + 1
    r = last
    newFirst = -1
    # print(f"Initial first {first} and last {last}")
    reverse_prefix = {134, 2097172, 87112285931760246646623899502532662132871}
    for f2 in reverse_prefix:
        start = f2 - first - len(word) + 1
        # print(f"detecing start is {start}")
        if start > 1 and (start < newFirst or newFirst == -1):
            newFirst = start
            print(f"WE ARE STARTING ON {f2}")
            break
    if l + 2 < log_2(newFirst) and 2 ** l + l - r - 1 < newFirst:
        newFirst = 2 ** l + l - r - 1
    if word not in bricks or newFirst < bricks[word]:
        verify(word, newFirst, id = 'add_brick_rev')
        bricks[word] = newFirst
        print(f"WE ARE STARTING ON {newFirst}")
    print("END\n")

# Generates all possible Bricks
# n - length of the substring
def Brick_generator(seq, bricks, n):
    # adding all the bricks and their reverses to the dictionary
    l = 0
    while l < log(l + n + 1):
        add_brick(bricks, word=tuple(seq[l:l + n]), first=l, add_rev=0)
        add_brick(bricks, word=tuple(seq[134 - l - n + 1:134 - l + 1]), add_rev=0, first=134 - l - n + 1)
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
            start = 2 ** (2 + dist) + dist + 1 - n + 1 + j
            add_brick(bricks, tuple(brick), first=start)

# Merging sub-bricks and bricks to generate all substrings
def merge_generator(seq, bricks, n):
    # if a Sub-Brick does not add something, it cannot add anything until the end
    z_seq = seq[:n].copy() + [False]*n
    for i in range(n):
        sub_brick = (z_seq[-i:] if (i > 0) else []) + z_seq[:n-i]
        print(len(sub_brick))
        # left-sided subbrick
        sub_brick = tuple(sub_brick[::-1])
        temporary_dict = {}
        for word, start in bricks.items():
            zero_lands_on = start + n - 1 - i
            newN = zero_lands_on + 2
            print(f"length is {len(word)} and range is {n}")
            print(binary(word))
            print(binary(sub_brick))
            new_word = [(word[j] or sub_brick[j]) for j in range(n)]
            # new word ends on 2 ** end + end - 1
            add_brick(temporary_dict, tuple(new_word), last=2 ** newN + newN - 1 + i)
        for key, value in temporary_dict.items():
            if key not in bricks or bricks[key] > value:
                bricks[key] = value

# Converts a boolean tuple into a binary string            
def binary(bool_tuple):
    result = ""
    for i in range(len(bool_tuple)):
        result += '1' if bool_tuple[i] else '0'
    return result
    
# verifies the equality of two substrings
def verify(inp, start, id = ""):
    goal = []
    ind = start
    while len(goal) < len(inp):
        goal.append(is_self_number(ind))
        ind += 1
    for i in range(len(goal)):
        if goal[i] != inp[i]:
            tmp = f"{id}:" if len(id) > 0 else ""
            print(f"{tmp}Error detected \n{binary(inp)} should start at {start} but \n{binary(goal)} starts")
            return False

# Lemma \label{reverseSubstringLemma}
# this function double-checks if the Lemma holds
def reverser(l,r):
    first = []
    for i in range(l - 1,r + 1):
        first.append(is_self_number(i))
    rev = tuple(first[::-1])
    # verify the equality
    verify(rev, 2**l + l - r - 1, id = "reverser")

# verify the "lemmaMid" lemma
def mid_verify(n):
    for i in range(n - 1):
        f_2n = is_self_number(2 ** n + 1 + i)
        or_ans = is_self_number(i) or is_self_number(n - 2 - i)
        if or_ans != f_2n:
            print("ERROR")
            return
    return

# reversible prefixes
def prefix_rev(n):
    word = []
    for i in range(n + 1):
        word.append(is_self_number(i))
    print(binary(word))
    print(binary(word[::-1]))
    print(word == word[::-1])
    return word == word[::-1]

# Basics
LEN = 5
SZ = 10000
seq = [False] * SZ
for m in range(0, SZ):
    p = m + binary_sum(m)
    if p < SZ:
        seq[p] = True

# for i in range(3,100):
#     mid_verify(i)

# building reversible prefixes IDs
reversible_prefix = []
prefix_id = 0
for _ in range(3):
    n = prefix_id + 2
    prefix_id = 2 ** n + n - 1
    reversible_prefix.append(prefix_id)

# l = 10
# n = 30
# print(binary(seq[l:l + n]))
# print(binary(seq[134 - l:134 - l - n:-1]))
# if seq[134 - l:134 - l - n:-1] == seq[l:l + n]:
#     print("true ranges are right")

print(reversible_prefix)
# mid_verify(11)
Bricks = {}
Brick_generator(seq, Bricks, LEN)

compatible_SubBrick_pairs(seq, Bricks, LEN)
merge_generator(seq, Bricks, LEN)
for brick,start in Bricks.items():
    print(binary(brick), start)

n = 21
# print(is_self_number(20)) 
# Brick_generator(10)

# Sample test case to verify the reverse lemma
# reverser(25,45)