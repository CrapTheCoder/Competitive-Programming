def max_counter(a):
    d = {}
 
    for i in a:
        d[i] = d.get(i, 0) + 1
 
    return max(d.values())
 
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
 
    ans = 0
 
    for i in range(k):
        ans += len(s[i::k]) + len(s[n - i - 1::-k]) - max_counter(s[i::k] + s[n-i-1::-k])
 
    print(ans // 2)