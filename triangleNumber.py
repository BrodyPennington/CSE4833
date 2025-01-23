import math

def countDivisors(n):
    # returns number of divisors n

    # Counter for divisors
    divisors = 0
    
    # Find square root of n and convert to integer
    sqrt_n = int(math.sqrt(n))

    # iterate from 1 to the square root of n
    for i in range(1, sqrt_n + 1):
        # if i divides n evenly, its a divisor
        if n % i == 0:
            # i is a divisor, so is n // i
            divisors += 2 if i != n // i else 1

    return divisors

def findTriangleNum(minDivisors):
    # finds first triangle number with more than (n) divisors
    n = 1
    triangle = 0
    while True:
        triangle += n    # calculate the nth triangle number
        n += 1

        if countDivisors(triangle) > minDivisors:
            return triangle
        

result = findTriangleNum(500)

print("Number is: ", result)


