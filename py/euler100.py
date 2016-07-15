# ======================================================================
# PROJECT EULER PROBLEM NO. 100: ARRANGED PROBABILITY
# ----------------------------------------------------------------------
# For what number X of blue discs out of N total red or blue discs
# is the probability of drawing 2 blue discs at random, 1/2?
#
# NOTE: (X / N) * ((X - 1) / (N - 1)) = 1/2 <=> T_(N-1) = 2 * T_(X - 1)!
# ======================================================================

from math import sqrt

# THE PROGRAM
def find_first(N):
    while 1:
        triangle_N = (N*N - N) / 2
        triangle_X = triangle_N / 2
        test_X = sqrt(8*triangle_X + 1)
        if (test_X == int(test_X)) and (test_X > sqrt(0.5)*(10**12)):
            return (N, (test_X - 1)/2 + 1)
        else:
            N += 1

result = find_first(10**12)

print(str(result[1])+" blue discs out of "+str(result[0])+" total.")
#print("Check: "+str((result[1] / result[0])*((result[1] - 1) / (result[0] - 1))))
