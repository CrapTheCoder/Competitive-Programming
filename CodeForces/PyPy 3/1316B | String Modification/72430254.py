for _ in range(int(input())):
    n = int(input())
    s = input()
 
    c = ''
    k = 0
 
    for i in range(n + 1):
        t = s[i:]
 
        if i % 2 != n % 2:
            t += s[:i][::-1]
        else:
            t += s[:i]
 
        if not c or t < c:
            c = t
            k = i
 
    print(c)
    print(k + 1)