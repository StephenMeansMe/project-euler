# Project Euler Problem No. 5: Smallest multiple
# ----------------------------------------------
# Find the smallest positive number that is
# evenly divisible by all of the numbers from 1
# to 20
#
# CREATED on 25 Nov 2014 by stephen
#
def factor_count(n,p):  # find max{k > 0 : p^k | n}
    num = n             # start with our number
    count = 0           # assume not divisible
    while num % p == 0:
        num /= p        # divide out the factor
        count += 1      # increment the factor count 

    return count


prime_factors = {
        2:1,
        3:1,
        5:1,
        7:1,
        11:1,
        13:1,
        17:1,
        19:1
        }       # initialize prime factor table

for i in range(4,21):
    p_candidates = [p for p in prime_factors if p < i]
    for j in p_candidates:
        divs_list = [0]+[d for d in range(1,5) if i % j**d == 0]
        exponent = max(divs_list)
        if exponent > prime_factors[j]:
            prime_factors[j] = exponent

result = 1
for k in prime_factors:
    print(str(k)+"^"+str(prime_factors[k])+"*",)
    result = result * (k ** prime_factors[k])

print(" = ",result)
