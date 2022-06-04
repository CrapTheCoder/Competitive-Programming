for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = n

    for i in range(n):
        s = p = a[i]

        for j in range(i+1,n):
            s += a[j]
            p *= a[j]

            if s == p:
                c += 1
    print(c)