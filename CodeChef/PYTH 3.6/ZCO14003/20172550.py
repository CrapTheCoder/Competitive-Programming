n = int(input())
print(max(j * (n - i) for i, j in enumerate(sorted(int(input()) for i in range(n)))))