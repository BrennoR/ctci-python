# Parens
# TODO: Implement better solution


# Brute force solution
def parens(n):
    if n == 1:
        return ['()']
    elif n == 2:
        return ['(())', '()()']

    ans = ['(())', '()()']
    seen = set()
    for _ in range(n - 2):
        new = []
        for idx in range(len(ans)):
            for i in range(len(ans[idx])):
                perm = ans[idx][:i] + '()' + ans[idx][i:]
                if perm not in seen:
                    new.append(perm)
                    seen.add(perm)
        seen.clear()
        ans = new

    return new


if __name__ == '__main__':
    print(parens(1))
    print(parens(2))
    print(parens(3))
    print(parens(4))
    print(len(parens(4)))
    print(parens(10))
    print(len(parens(10)))
