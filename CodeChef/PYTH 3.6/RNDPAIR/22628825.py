for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    z = []

    for i in range(n):
        for j in range(i+1, n):
            z.append(l[i] + l[j])

    print('%.8f' % (z.count(max(z)) / (n * (n - 1) // 2)))