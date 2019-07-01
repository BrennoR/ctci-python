# Coins
# TODO: Implement solution once again


# Solution taken from ctci-solutions repository by w-hat
def coins(cents):
    count = 0
    for c in range(cents, -1, -25):
        count += coins_helper(c)

    return count


def coins_helper(cents):
    count = 0
    for c in range(cents, -1, -10):
        count += (c // 5) + 1

    return count


if __name__ == '__main__':
    print(coins(1))
    print(coins(5))
    print(coins(10))
    print(coins(25))
    print(coins(100))
    print(coins(300))
    print(coins(400))
