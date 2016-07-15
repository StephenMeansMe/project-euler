# ======================================================================
# PROJECT EULER PROBLEM NO. 7: 10001st PRIME
# ----------------------------------------------------------------------
# Using Ruby (because primes library) prints the ten-thousand-and-first
# prime number. TO-DO: Implement this in C or something, like a real man
# ----------------------------------------------------------------------
# Created on 23 January 2014 by StephenMeansMe
# ======================================================================

require 'prime'

print Prime.first(10001).last
