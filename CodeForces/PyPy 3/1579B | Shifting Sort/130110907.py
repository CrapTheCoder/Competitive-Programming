for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
 
    f = []
 
    for i in range(n):
        d = 0
        while a[i] != b[i]:
            a = a[:i] + a[i+1:] + [a[i]]
            d += 1
 
        if d != 0:
            f.append(f'{i+1} {n} {d}')
 
    print(len(f))
    print(*f, sep='\n')