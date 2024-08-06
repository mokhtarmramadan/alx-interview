#!/usr/bin/python3
''' prime game '''


def isWinner(x, nums):
    ''' Return: name of the player that won the most rounds '''
    def sieve(n):
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p] is True:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = []
        for p in range(2, n + 1):
            if is_prime[p]:
                primes.append(p)
        return primes

    def count_primes(n, primes):
        count = 0
        for prime in primes:
            if prime <= n:
                count += 1
        return count

    if x == 0:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n, primes)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
