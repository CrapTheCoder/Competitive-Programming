n = int(input())
a = sorted(map(int, input().split()), reverse=True)

print(sum(a[i] * (i + 1) for i in range(n)) - sum(a))
