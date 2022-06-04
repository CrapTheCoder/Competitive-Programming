# crap_the_coder

for _ in range(int(input())):
    n = int(input())
    if (n % 4 == 0) and ((n // 4) % 2 == 0):
        print(n // 4)
    else:
        print(-1)