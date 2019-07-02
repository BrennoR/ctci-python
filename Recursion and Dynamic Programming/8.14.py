# Boolean Evaluation
# TODO: Rework solution


# Solution taken from w-hat ctci-solutions repository
def catalan_number(n):
    number = 1
    n = int(n)
    for i in range(n + 1, n * 2 + 1):
        number *= i
    for i in range(1, n + 2):
        number /= i
    return number


def count_eval(expr, value, memo=None):
    if len(expr) % 2 == 0:
        raise Exception("Malformed expression")
    if len(expr) == 1:
        return int((expr == "0") ^ value)
    if memo is None:
        memo = {}
    elif expr in memo:
        counts = memo[expr]
        return counts[int(value)]
    true_count = 0
    for opix in range(1, len(expr) - 1, 2):
        left, op, right = expr[:opix], expr[opix], expr[opix + 1:]
        if op == "&":
            true_count += count_eval(left, True, memo) * count_eval(right, True, memo)
        elif op == '|':
            true_count += count_eval(left, True, memo) * count_eval(right, True, memo)
            true_count += count_eval(left, False, memo) * count_eval(right, True, memo)
            true_count += count_eval(left, True, memo) * count_eval(right, False, memo)
        elif op == '^':
            true_count += count_eval(left, True, memo) * count_eval(right, False, memo)
            true_count += count_eval(left, False, memo) * count_eval(right, True, memo)
        else:
            raise Exception("Unknown operator")
    total_count = catalan_number((len(expr) - 1) / 2)
    false_count = total_count - true_count
    counts = (false_count, true_count)
    memo[expr] = counts
    return counts[int(value)]


if __name__ == '__main__':
    print(count_eval("0&0&0&1^1|0", True))
    print(count_eval("1^0|0|1", True))
