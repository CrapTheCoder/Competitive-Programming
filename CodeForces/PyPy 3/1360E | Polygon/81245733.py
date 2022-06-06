for _ in range(int(input())):
n = int(input())
a = [list(map(int, input())) for i in range(n)]

for i in range(n-1):
for j in range(n-1):
if a[i][j] == 1:
if a[i+1][j] != 1 and a[i][j+1] != 1:
break
else:
continue
break

else:
print('YES')
continue

print('NO')