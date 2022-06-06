for _ in range(int(input())):
n = int(input())
s = input()

if s[:4] == '2020': print('YES')
elif s[:3] == '202' and s[-1:] == '0': print('YES')
elif s[:2] == '20' and s[-2:] == '20': print('YES')
elif s[:1] == '2' and s[-3:] == '020': print('YES')
elif s[-4:] == '2020': print('YES')
else: print('NO')