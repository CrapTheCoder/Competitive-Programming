for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
 
    c = n // 2
 
    i = 1
    while c > 0:
        print(a[i], a[0])
        i += 1
        c -= 1