n = int(input())
s = input()

for i in [s[i:i+2] for i in range(n - 1)]:
if len(set(i)) == 2:
print('YES')
print(i)
break
else:
print('NO')