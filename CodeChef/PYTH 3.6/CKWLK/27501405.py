i = 0

l = []

while 20 ** i <= 10 ** 18:
    l.append(20 ** i)
    i += 1

for _ in range(int(input())):
    n = input()

    for i in range(len(l)):
        k = str(l[i])

        if n.startswith(k) and set(n[len(k):]) in [{'0'}, set()]:
            print('Yes')
            break
    else:
        print('No')
