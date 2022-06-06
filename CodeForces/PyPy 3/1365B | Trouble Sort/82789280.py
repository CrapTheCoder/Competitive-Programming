from sys import stdin
input = stdin.readline

for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if len(set(b)) == 2:
print('Yes')
continue

if a == sorted(a):
print('Yes')
else:
print('No')