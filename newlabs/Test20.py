#!/usr/bin/env python3

##########

##########
# Note that the function returns the value of a
# This is the last number displayed, as "new a value = b"
#
# If changed to b, then it displays "new b value, a + b"
##########
def fib(n):
    a, b = 0,1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b