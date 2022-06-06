for _ in range(int(input())):
n = int(input())

i = 1
j = 2

c = 0

while j // 2 <= n:
c += i * ((n - j // 2) // j + 1)

i += 1
j *= 2

print(c)