for _ in range(int(input())):
    c = 0

    for i in range(10):
        for j in list(map(int, input().split())):
            c += j <= 30

    print(['yes', 'no'][c < 60])