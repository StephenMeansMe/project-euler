# ======================================================================
# PROJECT EULER PROBLEM NO. 17: NUMBER LETTER COUNTS
# ----------------------------------------------------------------------
# How many letters are used when writing out 1 through 1000, inclusive,
# with 'and'?
# ======================================================================

import re

unit_names = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
tens_names = "zero ten twenty thirty fourty fifty sixty seventy eighty ninety".split()

#print unit_names, tens_names

def english(n):
    ''' Returns the British English name of the number'''
#    print n
    if n >= 1000:
#        print n // 1000
        thousands = english(n // 1000) + " thousand"
        n = n % 1000
        if n == 0:
            return thousands
        elif n < 100:
            return thousands + " and " + english(n)
        else:
            return thousands + ", " + english(n)
    elif n >= 100:
#        print n // 100
        hundreds = unit_names[n // 100] + " hundred"
        n = n % 100
        if n == 0:
            return hundreds
        else:
            return hundreds + " and " + english(n)
    elif n >= 20:
#        print n // 10
        tens = tens_names[n // 10]
        n = n % 10
        if n == 0:
            return tens
        else:
            return tens + "-" + english(n)
    else:
        return unit_names[n]

def letter_count(s):
    '''Counts the number of letters in the number name'''
    return len(re.findall(r'[a-zA-Z]',s))

for num in range(1,1001):
    print [(english(num),letter_count(english(num)))]
    raw_input()

print sum(letter_count(english(num)) for num in range(1,1001))
