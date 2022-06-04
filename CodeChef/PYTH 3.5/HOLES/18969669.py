t = int(input())
for tes in range(t):
    ans = 0
    name = input()
    for j in range(len(name)):
        if name[j - 1] == 'A':
            ans += 1
        elif name[j - 1] == 'B':
            ans += 2
        elif name[j - 1] == 'D':
            ans += 1
        elif name[j - 1] == 'O':
            ans += 1
        elif name[j - 1] == 'P':
            ans += 1
        elif name[j - 1] == 'Q':
            ans += 1
        elif name[j - 1] == 'R':
            ans += 1
    print(ans)