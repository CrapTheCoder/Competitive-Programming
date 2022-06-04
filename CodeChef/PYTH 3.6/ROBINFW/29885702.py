s = input().strip()

orient = 0

p = 0, 0
x, y = 0, 0

for _ in range(6):
    for i in s:
        if i == 'G':
            if orient == 0: y += 1
            if orient == 1: x += 1
            if orient == 2: y -= 1
            if orient == 3: x -= 1

        if i == 'L': orient = (orient - 1) % 4
        if i == 'R': orient = (orient + 1) % 4

        if y <= 0:
            print(1)
            exit()

print(0)