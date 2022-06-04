n = int(input())

h = 1000 * (n // 500)

n -= 500 * (n // 500)

h += 5 * (n // 5)

print(h)