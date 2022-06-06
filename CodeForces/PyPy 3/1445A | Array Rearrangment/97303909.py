for _ in range(int(input())):
    asd = input()
    if not asd:
        asd = input()
 
    n, x = map(int, asd.split())
 
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()), reverse=True)
 
    if not all(a[i] + b[i] <= x for i in range(n)):
        print('No')
    else:
        print('Yes')