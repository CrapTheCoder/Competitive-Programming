from string import ascii_lowercase

d = {i: 0 for i in range(10)}

for i in ascii_lowercase:
    d[(ord(i)-ord('a')) % 10] += 1

for _ in range(int(input())):
    s = input().strip()
    f = 1

    for i in s:
        f *= d[int(i)]

    print(f)