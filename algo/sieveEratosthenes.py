def sieve_of_eratosthenes(limit):
    """
    Generate all primes up to limit using sieve
    Time: O(n log log n), Space: O(n)
    """
    if limit < 2:
        return []
    
    is_prime = [True]*(limit+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i): # Mark multiples of i as not prime
                is_prime[j] = False
    return [i for i in range(2, limit+1), if is_prime[i]]
