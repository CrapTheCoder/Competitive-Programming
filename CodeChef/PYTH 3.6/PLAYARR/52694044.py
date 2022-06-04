n = int(input())
a = list(map(int, input().split()))

s = set()
for i in a:
    if i in s:
        s.remove(i)
    else:
        s.add(i)

print(len(s))