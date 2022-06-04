for _ in range(int(input())):
    n, k = map(int, input().split())
    m = 0

    for i in range(1, k + 1):
        b = n % i
        
        if b > m:
            m = b

    print(m)