for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    n = len(s)
 
    if '1' not in s:
        print((n-1) // (k+1) + 1)
        continue
 
    l = -1
    c = 0
 
    for i, j in enumerate(s):
        if j == '1':
            if l == -1:
                c += i // (k+1)
            else:
                d = i-l-1
                c += max(0, (d - k * 2 - 1) // (k+1) + 1)
 
            l = i
    
    c += (n-l-1) // (k+1)
    
    print(c)