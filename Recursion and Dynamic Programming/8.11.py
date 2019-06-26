# Coins


def coins(n):
    count = 1

    if n < 5:
        return count

    for num in range(5, n + 1):
        if num % 5 == 0:
            count += 1
        if num % 10 == 0:
            count += 1
        if num % 25 == 0:
            count += 1

    return count


if __name__ == '__main__':
    print(coins(1))
    print(coins(5))
    print(coins(10))
    print(coins(25))
    print(coins(100))
    print(coins(300))
    print(coins(400))
