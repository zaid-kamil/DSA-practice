# Given the string representations of two integers, return the string representation of the sum of those integers.

# For example:

# sumStrings('1','2') // => '3'
# A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

# I have removed the use of BigInteger and BigDecimal in java

# Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
from decimal import *

setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))
int = Decimal
def sum_strings(x, y):
    if not x:
        x = '0'
    if not y:
        y = '0'
    x = int(x) + int(y)
    
    return str(x)

# Example usage
print(sum_strings("0", ""))  # "0"
print(sum_strings("123", "456"))  # "579"
print(sum_strings("", "789"))  # "789"
print(sum_strings("1" * 1000000, "2" * 1000000))  # Very large numbers
print(sum_strings("131151201344081895336534324866", "0"))  # "131151201344081895336534324866"