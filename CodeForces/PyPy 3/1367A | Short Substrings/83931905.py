for _ in range(int(input())):
s = input()

print(s[0] + s[1:-1][::2] + s[-1])