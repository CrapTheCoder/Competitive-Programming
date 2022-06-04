n = int(input())
a = list(map(int, input().split()))
 
s = set()
 
l = []
 
for i in a[::-1]:
    if i not in s:
        l.append(i)
        s.add(i)
 
print(len(l))
print(*l[::-1])