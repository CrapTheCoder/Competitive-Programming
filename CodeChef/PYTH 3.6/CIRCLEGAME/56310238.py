min = lambda x, y: x if x < y else y
max = lambda x, y: x if x > y else y

for _ in range(int(input())):
    k, x = map(int, input().split())

    if k == 1:
        print(*range(1, x+1))
        continue

    sol = [0]

    for i in range(2, x+1):
        if i >= k:
            sol.append(sol[-1])
            continue

        pre = sol[-1]
        rem = (k-1) % i

        if pre >= rem:
            pre += 1

        sol.append(pre)

    print(*[i+1 for i in sol])
