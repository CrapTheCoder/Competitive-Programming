from math import gcd

MAX = 10 ** 5 + 1

n = int(input())
arr = map(int, input().split())

mobius = [1] * (MAX + 1)
divisors = [[] for _ in range(MAX + 1)]

for i in range(1, MAX):
    for j in range(i, MAX,i):
        divisors[j].append(i)

for i in range(1, MAX):
    for d in divisors[i]:
        if d == 1: continue
        if i % (d**2) == 0 or mobius[i] == 0: mobius[i] = 0
        elif len(divisors[i]) == 2: mobius[i] = -1
        else: mobius[i] = mobius[d] * mobius[i // d]


numbers = set(arr)

for i in arr:
    for d in divisors[i]:
        numbers.add(d)

numbers = sorted(list(numbers), reverse=True)
stack = []

cnt = [0] * (MAX + 1)

for i in numbers:
    stack.append(i)

    for d in divisors[i]:
        cnt[d] += 1

ans = 0

for x in numbers:
    num_co_prime = sum(cnt[d] * mobius[d] for d in divisors[x])
    while num_co_prime > 0:
        a = stack.pop()
        for d in divisors[a]:
            cnt[d] -= 1
            
        if gcd(a, x) > 1:
            continue
            
        ans = max(a*x,ans)
        num_co_prime-=1

print(ans)
