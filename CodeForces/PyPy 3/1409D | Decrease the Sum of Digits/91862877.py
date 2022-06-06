for _ in range(int(input())):
n, s = map(int, input().split())
r = list(map(int, str(n)))[::-1]
d = sum(r)

if d <= s:
print(0)
continue

for i in range(1, len(r)):
x = r[:i+1]

if x[-1] == 9:
continue

if d - sum(x) + x[-1] + 1 <= s:
nr = r.copy()
nr[:i] = [0] * len(nr[:i])
nr[i] = x[-1] + 1

print(int(''.join(str(i) for i in nr)[::-1]) - n)
break
else:
print(int('1' + '0' * len(r)) - n)