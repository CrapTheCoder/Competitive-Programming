from collections import Counter
 
for _ in range(int(input())):
    n, k = map(int,input().split())
    s = list(input())
 
    ans = 0
 
    for i in range(k):
        ans += len(s[i::k]) + len(s[n-i-1::-k]) - max(Counter(s[i::k] + s[n-i-1::-k]).values())
 
    print(ans // 2)