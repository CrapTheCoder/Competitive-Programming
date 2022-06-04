from sys import stdin
input = stdin.readline

MAX = 2000013
pf = [True] * MAX
pf[0] = pf[1] = False

ps = []
for i in range(2, MAX):
    if pf[i]:
        ps.append(i)
        for j in range(i*i, MAX, i):
            pf[j] = False

for _ in range(int(input())):
    n = int(input())
    on = n

    for i in range(len(ps)):
        if n % ps[i] == 0:
            n //= ps[i]
            n *= ps[i]+1
            break
    else:
        print(n+1)
        continue

    print(n)