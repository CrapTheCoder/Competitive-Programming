for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []

    for i in range(n):
        c = 0

        for j in range(i+1, n):
            if a[j] > a[i]:
                c += 1

        b.append(c)

    print(*b)
