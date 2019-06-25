# Permutations with Dups
# TODO: Fix and improve 


def perm_w_dups(string):
    if not string:
        return

    memo = set()
    perms = [string[0]]
    for c in string[1:]:
        for idx in range(len(perms)):
            for i in range(1, len(perms[idx]) + 1):
                perm = perms[idx][:i] + c + perms[idx][i:]
                if perm not in memo:
                    perms.append(perm)
                    memo.add(perm)
            perms[idx] = c + perms[idx]

    return perms


if __name__ == '__main__':
    print(perm_w_dups("abcc"))

