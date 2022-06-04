from string import ascii_lowercase

alps = ascii_lowercase

for _ in range(int(input())):
    s = input()

    for i in s:
        print(alps[(ord(i) - ord('a') + len(s)) % 26], end='')

    print()