# Recursive Multiply


# Naive solution - O(min(a, b))
def naive_multiply(a, b):
    total = 0
    counter = min(a, b)
    adder = max(a, b)
    for _ in range(counter):
        total += adder

    return total


# TODO: finish better solution
# Better solution
def better_multiply(a, b):
    multiplier = min(a, b)
    adder = max(a, b)
    times = 0
    carry = 0
    while multiplier:
        times += 1
        carry += multiplier % 2
        multiplier = multiplier // 2

    total = adder
    for _ in range(times - 1):
        total = total << 1

    for _ in range(carry):
        total += adder

    return total


print(naive_multiply(10, 8))
print(better_multiply(100, 8))
print(naive_multiply(100, 300))
print(better_multiply(100, 300))
