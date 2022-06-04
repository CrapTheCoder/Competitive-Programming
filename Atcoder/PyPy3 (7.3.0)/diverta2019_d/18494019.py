n = int(input())
c = 0
for i in range(1, int(n ** 0.5) + 2):
    if n % i == 0 and (n // i - 1 != 0):
        if n // (n // i - 1) == n % (n // i - 1):
            c += n // i - 1

print(c)
