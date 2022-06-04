s = input()
b = bin(int(s))[2:]

b = b.replace('0', '')

print(int(b, 2))