from string import ascii_uppercase

for _ in range(int(input())):
    n = int(input())

    for i in range(n):
        print((n-i-1) * ' ', end='')
        print(ascii_uppercase[:i+1], *list(range(1, i+2)), end='', sep='')
        print((n-i-1) * ' ', end='')
        print()