for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    s = [0]
 
    for i in range(1, n):
        s.append((a[i] & a[i-1]) ^ a[i-1])
        a[i] ^= (a[i] & a[i-1]) ^ a[i-1]
 
    print(*s)