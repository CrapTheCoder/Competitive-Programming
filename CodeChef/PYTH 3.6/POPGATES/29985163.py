for _ in range(int(input())):
    n, k = map(int, input().split())
    a = input().split()

    flip = False

    for _ in range(k):
        x = a.pop()

        if flip:
            x = 'HT'[x == 'H']

        if x == 'H':
            flip = not flip

    print(a.count('HT'[flip]))