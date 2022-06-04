n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i != 2:
        print(i^2, end=' ')
    else:
        print(1, end=' ')

print()
