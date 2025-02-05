def sieve(n):
    """Generate a list indicating prime status for numbers up to n."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def count_primes_up_to(n, prime_list):
    """Count prime numbers up to n using a precomputed prime list."""
    return sum(prime_list[:n + 1])

def isWinner(x, nums):
    """Determine the winner of the prime number game."""
    if not nums or x < 1:
        return None
    
    max_n = max(nums)
    prime_list = sieve(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        prime_count = count_primes_up_to(n, prime_list)
        
        # Maria wins if the count of primes is odd, Ben wins if it's even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

