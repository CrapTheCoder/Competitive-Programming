n = int(input())

a = sorted(set(map(int, input().split())))

if len(a) == 1:
    print(0)
else:
    print(a[-2])
