# ======================================================================
# PROJECT EULER PROBLEM NO. 28: NUMBER SPIRAL DIAGONALS
# ----------------------------------------------------------------------
# Find the sum of the diagonals of a spiral of numbers
# ======================================================================

limit = 502 # 1001 is the 501st odd number

total_sum = 1

for k in range(2, limit):
    n = 2*k - 1
    step = 2*k - 2
    partial_sum = 0
    for i in range(4):
        partial_sum += n*n - i*step
    #print("Sum of "+str(k)+"th diagonal entries: " + str(partial_sum))
    total_sum += partial_sum

print("The sum of all the diagonal entries is: " + str(total_sum))
