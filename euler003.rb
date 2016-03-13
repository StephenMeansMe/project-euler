# ======================================================================
# PROJECT EULER PROBLEM NO. 3: LARGEST PRIME FACTOR
# ----------------------------------------------------------------------
# Using Ruby (because primes library), return the largest prime factor
# of the number 600851475143. TO-DO: Implement this at a lower level
# using the sieve of Eratosthenes or something.
# ----------------------------------------------------------------------
# Created on 23 January 2014 by StephenMeansMe.
# ======================================================================

require 'prime'

thebignumber = 600851475143

divisors = Prime.prime_division(thebignumber)

print divisors.last
