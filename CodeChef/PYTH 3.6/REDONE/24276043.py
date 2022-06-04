mod = 10 ** 9 + 7
a = {}
d = 1

for i in range(1, 10 ** 7 + 1):
  d = (d * i) % mod
  a[i] = d

for _ in range(int(input())):
    n = int(input())
    print(a[n + 1] - 1)