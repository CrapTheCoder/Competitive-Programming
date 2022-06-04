# crap_the_coder

for _ in range(int(input())):
    s = input()
    print(int(''.join(sorted(s, reverse=True)), 2))