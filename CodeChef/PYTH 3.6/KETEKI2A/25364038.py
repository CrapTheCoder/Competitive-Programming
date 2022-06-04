n = int(input())
a = list(map(int, input().split()))

print(-sum(a[:n // 2 + n % 2]) + sum(a[n // 2 + n % 2:]))