for _ in range(int(input())):
    n = int(input())

    a = input()
    b = input()
    w = list(map(int, input().split()))

    c = sum(a[i] == b[i] for i in range(n))

    if c == n: print(w[n])
    else: print(max(w[:c + 1]))
