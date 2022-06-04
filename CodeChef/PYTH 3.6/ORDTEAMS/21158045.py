for _ in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    for l1, l2 in ((a, b), (a, c), (b, c)):
        x = 0
        y = 0

        for i, j in zip(l1, l2):
            if i > j:
                x += 1
            if i < j:
                y += 1

        if (x == 0) == (y == 0):
            print('no')
            break
    else:
        print('yes')