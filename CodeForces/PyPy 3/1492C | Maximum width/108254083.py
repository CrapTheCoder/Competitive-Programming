def sub(s, t):
    l = []
 
    i = 0
    for j in range(m):
        while i < n:
            if s[i] != t[j]:
                i += 1
                continue
 
            l.append(i)
            i += 1
 
            break
 
    return l
 
n, m = map(int, input().split())
s = input()
t = input()
 
s1 = sub(s, t)
s2 = sub(s[::-1], t[::-1])
 
for i in range(m):
    s2[i] = n - s2[i] - 1
 
s2.reverse()
 
maxi = float('-inf')
for i in range(m-1):
    maxi = max(maxi, abs(s1[i+1] - s1[i]), abs(s2[i+1] - s1[i]), abs(s1[i+1] - s2[i]), abs(s2[i+1] - s2[i]))
 
print(maxi)