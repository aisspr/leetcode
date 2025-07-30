def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n% i == 0 or n %(i+2) == 0:
            return False
        i += 6
    return True

"""
Key Insights:

All primes > 3 are of the form 6k ± 1i i
Only check divisors up to √n - if n has a divisor > √n, it must also have one < √n
Skip even numbers after checking n % 2

Time Complexity: O(√n)
Space Complexity: O(1)
"""