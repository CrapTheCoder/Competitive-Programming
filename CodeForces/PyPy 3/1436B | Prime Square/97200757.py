for _ in range(int(input())):
n = int(input())

for i in range(n):
l = [0] * n
l[i] = 1
l[(i+1) % n] = 1

print(*l)