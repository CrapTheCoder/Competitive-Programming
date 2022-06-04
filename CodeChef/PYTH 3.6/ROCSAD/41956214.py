for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))

    j = 0
    d = float('inf')

    for i in range(n):
        while j < n and a[i] >= b[j]:
            d = min(d, abs(a[i] - b[j]))
            j += 1
            
        if j < n:
            d = min(d, abs(a[i] - b[j]))

    print(d)
