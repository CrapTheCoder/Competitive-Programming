for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = 0

    for i in range(n):
        m = max(
            m,
            a[(i-2)%n] + a[(i-1)%n] + a[i],
            a[(i-1)%n] + a[i] + a[(i+1)%n],
            a[i] + a[(i+1)%n] + a[(i+2)%n]
        )

    print(m)