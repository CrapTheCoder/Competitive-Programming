a = 1

x = [0]

for i in range(10 ** 5):
    x.append(x[-1] + a * (a+1) * (a+2) * (a+3))
    a += 1

for _ in range(int(input())):
    l, r = map(int, input().split())
    print((x[r] - x[l-1]) % (10 ** 9 + 7))
