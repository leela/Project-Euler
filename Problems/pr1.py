"""Multiples of 3 & 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiplesof3or5(num):
    return [i for i in range(1, num) if i%3 == 0 or i%5 == 0]

print sum(multiplesof3or5(1000))

