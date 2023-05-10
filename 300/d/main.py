N = int(input())


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes

primes = sieve(int(N ** 0.5) + 1)  # Nの平方根までの素数を列挙
ans = 0
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        a = primes[i]
        b = primes[j]
        if N // (a ** 2 * b) < b:
            break
        for k in range(j + 1, len(primes)):
            c = primes[k]
            if N < a ** 2 * b * c ** 2:
                break
            ans += 1
print(ans)
