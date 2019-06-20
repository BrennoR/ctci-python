# Permutations without Dups


def perm_wo_dups(string):
    if not string:
        return

    perms = [string[0]]
    for c in string[1:]:
        for idx in range(len(perms)):
            for i in range(1, len(perms[idx]) + 1):
                perms.append(perms[idx][:i] + c + perms[idx][i:])
            perms[idx] = c + perms[idx]

    return perms


if __name__ == '__main__':
    print(perm_wo_dups("abcd"))
    print(perm_wo_dups("abc"))
    print(perm_wo_dups("ab"))
    print(perm_wo_dups("a"))
    print(perm_wo_dups(""))
