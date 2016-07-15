# ======================================================================
# PROJECT EULER PROBLEM NO. 4: LARGEST PALINDROME PRODUCT
# ----------------------------------------------------------------------
# Find the largest palindrome that is the product of 3-digit numbers.
# ======================================================================

import math as m

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def factorize(n):
    for i in range(int(m.sqrt(n)),999):
        #if n / i > 999 or i*i > n:
        #    break
        if n % i == 0:
            return (True, (n, i, n / i))

    return (False, (n, 0, 0))

palindromes = [x for x in range(100*100,999*999) if isPalindrome(x)]

for p in palindromes[::-1]:
    result = factorize(p)
    if result[0]:
        print result[1]
        break

