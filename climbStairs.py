def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n
    # prev2 = ways to reach step (i-2)
    # prev1 = ways to reach step (i-1)
    
    p2 = 1
    p1 = 2

    for i in range(3, n+1):
        current = p2+p1
        p2 = p1
        p1 = current
    return p1


def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, a + b
    return b