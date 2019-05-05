import timeit
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

    a, b, c = 1, 2, 4
    for _ in range(n - 4):
        d = a + b + c
        a = b
        b = c
        c = d

    return a + b + c


# Solution Check
print("Recursive Solution:", triple_step_recursive(10))
print("Memoization Solution", triple_step_memoization(10))
print("Dynamic Solution", triple_step_dynamic(10))

# Time Comparison
print("Recursive Solution:",
      timeit.timeit('triple_step_recursive(15)',
                    setup="from __main__ import triple_step_recursive", number=10000))
print("Memoization Solution:",
      timeit.timeit('triple_step_memoization(15)',
                    setup="from __main__ import triple_step_memoization", number=10000))
print("Dynamic Solution:",
      timeit.timeit('triple_step_dynamic(15)',
                    setup="from __main__ import triple_step_dynamic", number=10000))
