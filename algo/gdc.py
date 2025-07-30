def gcd(a,b):
    a = abs(a)
    b = abs(b)

    #base case, if b is 0, a is gcd
    while b!= 0:
        a, b = b, a % b
        return b