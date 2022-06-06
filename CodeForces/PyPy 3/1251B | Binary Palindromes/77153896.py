for _ in range(int(input())):
    n = int(input())
 
    l = 0
    c0 = c1 = 0
 
    for i in range(n):
        s = input()
 
        l += len(s) // 2
        c0 += s.count('0')
        c1 += s.count('1')
 
    if c0 // 2 + c1 // 2 >= l:
        print(n)
    else:
        print(n-1)