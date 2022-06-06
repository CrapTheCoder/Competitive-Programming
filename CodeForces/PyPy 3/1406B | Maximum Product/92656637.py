for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
 
    neg = a[:5]
    pos = a[-5:][::-1]
 
    maxi = -float('inf')
 
    for i in range(6):
        f = 1
 
        for j in range(i): f *= neg[j]
        for j in range(5-i): f *= pos[j]
 
        maxi = max(maxi, f)
 
    print(maxi)