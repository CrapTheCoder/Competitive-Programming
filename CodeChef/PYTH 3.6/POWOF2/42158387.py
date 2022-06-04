for _ in range(int(input())):
    n = int(input())

    c = 0
    while n:
        x = 0
        while n % 2 == 0:
            n //= 2
            x += 1

        if n != 1:
            break

        c += 1
        n = x

    print(max(0, c-1))
