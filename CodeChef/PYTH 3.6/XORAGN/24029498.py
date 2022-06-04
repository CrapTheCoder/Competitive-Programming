for _ in range(int(input())):
    n = int(input())
    a = input().split()
    k = 0

    for i in range(n):
        k = k ^ 2 * int(a[i])

    print(k)
