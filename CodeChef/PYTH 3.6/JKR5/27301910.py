m = [1, 2, 4, 7]
lm = 4

for _ in range(int(input())):
    n = int(input()) - 1

    if n < lm:
        print(m[n])
    else:
        while lm <= n:
            m.append(m[-1] + m[-2] + m[-3])
            lm += 1

        print(m[-1])