# Euclid's Algorithm
# This algorithm find the greatest common divisor for two number
# Implemented in two different but similar ways. Method 2 is slightly faster.

# Assumes that m >= n, but will compensate if entered incorrectly
def GCD_Method1(m, n):
    gcd = 0

    # get the lowest number of the two
    if m > n:
        lowestNum = n
    else:
        lowestNum = m

    # Run from 1 up to and including lowest number (the max GCD possible)
    for iter2 in range(1, lowestNum + 1):
        if m % iter2 is 0 and n % iter2 is 0:  # If iter is a divisible by both numbers with no remainder
            gcd = iter2  # Update GCD

    return gcd

# Assumes that n1 >= n2, but will compensate if entered incorrectly
def GCD_Method2(n1, n2):
    # Set m to the large number and n to the smaller number
    if n1 > n2:
        m = n1
        n = n2
    else:
        n = n1
        m = n2

    # while the smaller num is not 0, find the remainder of m mod n, then update variables till n = 0.
    while (n is not 0):
        rem = m % n
        m = n
        n = rem

    return m

if __name__ == '__main__':
    print("Testing GCD function:")
    print(GCD_Method1(10,15))
    print(GCD_Method2(10, 15))