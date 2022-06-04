t = 0

for _ in range(int(input())):
    s = input()

    c0 = c1 = 0

    for i in s:
        if i.isupper():
            c0 += 1
        if i.islower():
            c1 += 1

    t += abs(c0 - c1)

print(t)