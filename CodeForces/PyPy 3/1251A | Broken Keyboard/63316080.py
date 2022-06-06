for _ in range(int(input())):
s = input()
n = len(s)

x = set(range(n))

i = 0

while i < n - 1:
if s[i] == s[i+1]:
x.remove(i)
x.remove(i+1)

i += 1

i += 1

print(''.join(sorted(set((s[i] for i in x)))))