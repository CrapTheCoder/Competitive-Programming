l = [1, 2, 3]

for i in range(100):
    l.append(l[-1] + l[-3])

for _ in range(int(input())):
    print(l[int(input()) - 1])