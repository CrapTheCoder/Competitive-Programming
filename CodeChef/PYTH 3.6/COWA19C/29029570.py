def solve(i=0):
    if i == m:
        return 1

    return solve(i + 1) * (divs[i] + 1)

for _ in range(int(input())):
    n = int(input())

    divs = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)

            if n // i != i:
                divs.append(n // i)

    m = len(divs)

    print((solve() - 1) % (10 ** 9 + 7))