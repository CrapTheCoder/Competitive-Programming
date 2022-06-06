for _ in range(int(input())):
    n, k = map(int, input().split())
    l = [1] * (k-3)
    n -= k-3
 
    if n < 3:
        if n == 1:
            l[0] += 1
        elif n == 2:
            l[0] += 1
            l[1] += 1
 
        print(*l)
 
    else:
        if n % 2:
            print(*l, 1, n // 2, n // 2)
        else:
            if (n // 2) % 2:
                print(*l, n // 2 - 1, n // 2 - 1, 2)
            else:
                print(*l, n // 2, n // 4, n // 4)