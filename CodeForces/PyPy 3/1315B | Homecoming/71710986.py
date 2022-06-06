for _ in range(int(input())):
    a, b, p = map(int, input().split())
    s = input()[:-1] + 'X'
 
    n = len(s)
 
    l = [None] * n
 
    l[-1] = 0
 
    for i in range(n - 2, -1, -1):
        l[i] = l[i+1]
 
        if s[i+1] != s[i]:
            if s[i] == 'A': l[i] += a
            if s[i] == 'B': l[i] += b
 
    if l[0] < p:
        print(1)
        continue
 
    if l[-2] > p:
        print(n)
        continue
 
    for i in range(n - 1, -1, -1):
        if l[i] > p:
            print(i + 2)
            break
    else:
        print(1)