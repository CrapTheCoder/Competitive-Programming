n, p = map(int, input().split())
a = list(map(int, input().split()))
print(sum(i < p for i in a))