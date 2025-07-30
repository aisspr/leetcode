def lcm(a,b):
    if a == 0 or b == 0:
        return 0 # LCM(0, x) = 0, LCM(0, 0) = 0
    return abs(a * b) // gcd (a,b)

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return b
    