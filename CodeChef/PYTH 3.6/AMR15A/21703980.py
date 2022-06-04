n = int(input())
a = list(map(int, input().split()))

x = sum(not i % 2 for i in a)
y = n - x

print('READY FOR BATTLE' if x > y else 'NOT READY')