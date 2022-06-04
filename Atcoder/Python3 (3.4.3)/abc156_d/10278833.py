n = int(input())
a = list(map(int, input().split()))

x = round(sum(a) / n)

print(sum((i - x) ** 2 for i in a))