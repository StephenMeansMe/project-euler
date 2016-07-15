# ======================================================================
# PROJECT EULTER PROBLEM NO. 40: CHAMPERNOWNE'S CONSTANT
# ----------------------------------------------------------------------
# 0.12345678910111213... find the product of the 10^nth decimal digits
# For n = 0,1,2,3,4,5,6. Note: 1st and 10th decimal digits are 1.
# ======================================================================

champernowne = [0]
number = 0

while len(champernowne) < 10**6 + 1:
    number += 1
    addendum = [str(number)[i] for i in range(len(str(number)))]
    champernowne += addendum

print([champernowne[10**n] for n in range(7)])
