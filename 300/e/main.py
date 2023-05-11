from functools import lru_cache

inverse_5 = pow(5, -1, 998244353)

@lru_cache(maxsize=None)
def count_dice_combinations(n):
    if n == 1:
        return 1
    total = 0
    for i in range(2, min(7, n + 1)):
        if n % i == 0:
            total += count_dice_combinations(n // i)
            total %= 998244353
    total *= inverse_5
    total %= 998244353
    return total

n = int(input())
print(count_dice_combinations(n))
