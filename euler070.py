# ======================================================================
# PROJECT EULER PROBLEM NO. 70: TOTIENT PERMUTATION
# ----------------------------------------------------------------------
# Find n and phi(n) such that phi(n) is a digit permutation of n and
# n / phi(n) is a minimum.
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

def primeFactorList(n):
    if prime(n):
        return [1,n]
    else:
        return [x for x in primeSieve(int(m.sqrt(n))) if n % x == 0]

def totient(N):
    t = N
    for p in primeFactorList(N):
        t *= 1 - 1 / p
    return (N, t)

candidates = [totient(x) for x in range(1,10**7) if set(str(totient(x))) == set(str(x))]
quotients = [y[0] / y[1] for y in candidates]

print (y for y in candidates if y[0] / y[1] == min(quotients))
