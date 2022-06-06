for _ in range(int(input())):
    n, k = map(int, input().split())
    x = sorted(map(int, input().split()), reverse=True)
 
    s = n
    c = 0
 
    for i in range(k):
        s -= n - x[i]
        if s <= 0:
            break
 
        c += 1
 
    print(c)