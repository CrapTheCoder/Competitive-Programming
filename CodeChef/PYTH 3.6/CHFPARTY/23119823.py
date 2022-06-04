for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    x = 0

    for i in a:
        if x >= i:
            x += 1
        else:
            break

    print(x)