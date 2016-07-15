# ======================================================================
# PROJECT EULER PROBLEM NO. 12: HIGHLY DIVISIBLE TRIANGULAR NUMBER
# ----------------------------------------------------------------------
# Find the first triangular number with over 500 divisors (brute).
# ======================================================================

require 'prime'

i = 0

loop do
    divs = 1
    i += 1
    num = (i * (i + 1)) / 2
    factors = Prime.prime_division(num)
    factors.each {|x| divs *= x[1] + 1}
    puts "#{num} has #{divs} divisors!"
    break if divs > 500
end
