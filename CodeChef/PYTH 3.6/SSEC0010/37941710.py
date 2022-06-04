x = """S
S S
S S E
S S E C
S S E
S S
S""".split('\n')

for _ in range(int(input())):
    n = (int(input()) - 1) % 7

    print(*[ord(i) for i in x[n].split()])