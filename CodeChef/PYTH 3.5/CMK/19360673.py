try:
    for _ in range(int(input())):
        a = 0
        n, k = map(int, input().split())
        
        m = sorted(map(int, input().split()))[:k]
        c = sorted(map(int, input().split()), reverse=True)[:k][::-1]
    
        for i in range(k):
            if m[i] < c[i]:
                a += 1
    
        if a >= k:
            print('YES')
        else:
            print('NO')
except:
    pass