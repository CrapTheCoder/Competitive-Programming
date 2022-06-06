def solve(a):
    n = len(a)
 
    if a == sorted(a):
        return n
 
    return max(solve(a[:n//2]), solve(a[n//2:]))
 
n = int(input())
a = list(map(int, input().split()))
 
print(solve(a))