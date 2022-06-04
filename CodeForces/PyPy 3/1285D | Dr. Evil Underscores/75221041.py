def solve(a, b=32):
    if b == -1:
        return 0
 
    a1 = []
    a2 = []
 
    n = len(a)
 
    for i in range(n):
        if (a[i] // (2 ** b)) % 2 == 1:
            a1.append(a[i])
        else:
            a2.append(a[i])
 
    if len(a1) == 0:
        return solve(a2, b - 1)
 
    elif len(a2) == 0:
        return solve(a1, b - 1)
 
    else:
        return 2 ** b + min(solve(a1, b - 1), solve(a2, b - 1))
 
n = int(input())
a = list(map(int, input().split()))
 
print(solve(a))