# ======================================================================
# PROJECT EULER PROBLEM NO. 50: CONSECUTIVE PRIME SUM
# ----------------------------------------------------------------------
# Which prime less than 1,000,000 can be written as the sum of the most
# consecutive primes?
# ======================================================================

import math as m

def prime(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

def primeSieve(n):
    big_list = [True]*n
    for i in range(2, int(m.sqrt(n))):
        if big_list[i]:
            for j in range(i*i, n, i):
                big_list[j] = False

    return [x for x in range(2,n) if big_list[x] == True ]

millionprimes = primeSieve(10**6)

sums = []

for i in range(0,len(millionprimes)):
    primesum = 0
    length = 0
    for p in millionprimes[i::]:
        if primesum + p < 10**6:
            primesum += p
            length += 1
        else:
            sums.append((primesum, length))
            break

print [x for x in sums if x[1] == max([y[1] for y in sums])]
