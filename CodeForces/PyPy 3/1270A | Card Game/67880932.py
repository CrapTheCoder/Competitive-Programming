for _ in range(int(input())):
n, k1, k2 = map(int, input().split())

a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

if a[-1] > b[-1]:
print('YES')
else:
print('NO')