def solve(i=9, p=()):
    if sum(p) == n:
        return p
 
    if i <= 0 or sum(p) > n:
        return (1,) * 100
 
    return min(solve(i-1, p+(i,)), solve(i-1, p), key=lambda x: int(''.join(str(j) for j in sorted(x))))
 
for _ in range(int(input())):
    n = int(input())
    x = int(''.join(str(i) for i in sorted(solve())))
    print(x if x <= 200000000000 else -1)