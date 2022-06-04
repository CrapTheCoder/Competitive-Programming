for _ in range(int(input())):
    n = int(input())

    l = list(range(n))

    for i in range(n):
        print(*l, sep='')

        for j in range(i+1):
            l[j] += 1

        for j in range(i+1, n):
            l[j] -= 1
