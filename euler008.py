# ======================================================================
# PROJECT EULER PROJECT NO. 008: LARGEST PRODUCT IN A SERIES
# ----------------------------------------------------------------------
# Find the thirteen greatest digits in a given number, that have the
# greatest product.
#
# ======================================================================

def product_of_digits(digits):
    ''' given a string of digits, find their product '''
    p = 1
    for j in digits:
        p *= int(j)
        return p

bignumstring = ""

with open("euler008.txt","r") as rawnumber:
    for line in rawnumber:
        bignumstring += str(int(line))
    # close file

productslist = []

for i in range(988):
    productslist.append(product_of_digits(bignumstring[i:i+13]))

print max(productslist)