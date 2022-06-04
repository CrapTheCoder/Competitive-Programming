for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    s = sum(a)

    print(' '.join(str(i) for i in [s - i for i in a]))