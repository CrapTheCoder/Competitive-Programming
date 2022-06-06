from sys import stdin
input = stdin.readline
 
# max = lambda x, y: x if x > y else y
# min = lambda x, y: x if x < y else y
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    l, r = 0, 2 * 10 ** 9
 
    maxi2 = 0
    while l < r:
        m = (l+r+1) // 2
 
        b = a.copy()
        for i in range(n-1, 1, -1):
            d = min(max(0, (b[i] - m) // 3), a[i] // 3)
 
            b[i-2] += 2*d
            b[i-1] += d
            b[i] -= 3*d
 
        maxi = min(b)
        if m <= maxi:
            l = m
        else:
            r = m-1
 
    print(l)