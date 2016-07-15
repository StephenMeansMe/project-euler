# =========================================================================
# PROJECT EULER PROBLEM NO. 14: LONGEST COLLATZ SEQUENCE
# -------------------------------------------------------------------------
# Which number less than 1 million has the longest Collatz sequence?
# 
# The Collatz sequence f(n) is defined by: f(n) = 3n + 1 if n is odd, and
# f(n) = n/2 if n is even.
# =========================================================================

def collatz(n):
    if n % 2 == 0: return n // 2
    else: return 3*n + 1

# INITIAL VALUES
limit = 1000000
length = [0] * limit
length[1] = 1
max_length = [1,1]

for i in range(1,limit):
    unknown = []
    number = i
    chain = 0
    while number > limit - 1 or length[number] < 1:
        unknown.append(number)
        number, chain = collatz(number), chain + 1

    for j in range(chain):
        m = unknown[j]
        if m < limit:
            length[m] = length[number] + chain - j
            if length[m] > max_length[1]: max_length = [i, length[m]]

print(max_length)
