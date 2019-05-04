# Triple Step


# Recursive implementation
def triple_step_recursive(n: int) -> int:
    if n == 1 or n == 2:
        return n
    elif n == 3:
        return 4

    return triple_step_recursive(n - 1) + triple_step_recursive(n - 2) + triple_step_recursive(n - 3)


# Top-down dynamic programming (memoization)
def memoization(n: int, memo: [int]) -> int:
    if n == 1 or n == 2:
        return n
    elif n == 3:
        return 4

    if memo[n] == 0:
        memo[n] = memoization(n - 1, memo) + memoization(n - 2, memo) + memoization(n - 3, memo)

    return memo[n]


def triple_step_memoization(n: int) -> int:
    return memoization(n, [0] * (n + 1))


# Bottom up dynamic programming
def triple_step_dynamic(n: int) -> int:
    if n == 1 or n == 2:
        return n
    elif n == 3:
        return 4

    a, b, c = 1, 2, 4
    d = 0
    for _ in range(n - 3):
        d, a, b, c = a + b + c, b, c, d

    return d


print(triple_step_dynamic(5))
