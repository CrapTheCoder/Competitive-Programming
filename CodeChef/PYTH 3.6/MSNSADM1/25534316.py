for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    m = max(*(a[i] * 20 - b[i] * 10 for i in range(n)), 0)

    print(m)