for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    x = a[0]
    for i in a[1:]:
        x ^= i

    print(x)