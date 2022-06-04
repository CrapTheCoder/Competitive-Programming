INV = {1: 2, 2: 1}

for _ in range(int(input())):
    g = int(input())

    for _ in range(g):
        # 1 = HEAD
        # 2 = TAIL

        i, n, q = map(int, input().split())

        if n % 2 == 0:
            print(n // 2)
        else:
            print(n // 2 + (i != q))
