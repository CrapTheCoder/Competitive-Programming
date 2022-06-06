for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(input())
 
    for i in range(k):
        c = set()
 
        for j in range(i, n, k):
            if a[j] != '?':
                c.add(a[j])
 
        if len(c) > 1:
            break
 
        if c:
            c = list(c)[0]
 
            for j in range(i, n, k):
                a[j] = c
 
    else:
        cs0 = a[:k].count('0')
        cs1 = a[:k].count('1')
 
        for i in range(k):
            if a[i] == '?':
                if cs0 < cs1:
                    cs0 += 1
                    a[i::k] = ['0'] * len(a[i::k])
                else:
                    cs1 += 1
                    a[i::k] = ['1'] * len(a[i::k])
 
        if a == (a[:k] * (n // k + 1))[:n] and cs0 == cs1:
            print('YES')
        else:
            print('NO')
 
        continue
 
    print('NO')