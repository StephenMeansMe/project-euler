# ======================================================================
# PROJECT EULER PROBLEM NO. : COUNTING SUNDAYS
# ----------------------------------------------------------------------
# How many first-day Sundays between 1901/01/01 and 2000/12/31?
# ======================================================================

import datetime

sundays = 0

for year in range(1901,2001):
    for month in range(1,13):
        if datetime.date(year,month,1).weekday() == 6:
            sundays += 1

print sundays
