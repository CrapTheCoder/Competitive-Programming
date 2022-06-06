n = int(input())
s = list(input())

for d in range(1, n+1):
if not n % d:
s[:d] = s[:d][::-1]

print(''.join(s))