from string import ascii_uppercase

for _ in range(int(input())):
    n = int(input())
    s = list(range(1, n+1))

    for i in range(n // 2):
        print('*' * (i+1))

    print(ascii_uppercase[:n // 2 + 1])

    for i in range(n // 2 - 1, -1, -1):
        print('*' * (i+1))
