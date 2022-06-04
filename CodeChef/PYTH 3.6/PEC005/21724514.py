for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if a[i] >= a[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    print(max(lis))
