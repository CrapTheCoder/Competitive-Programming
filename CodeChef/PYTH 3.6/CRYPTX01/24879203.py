s = input().replace(' ', '')
l = len(s)

x = int(l ** 0.5)

r = ''

for i in range(x+1):
    r += s[i::x+1] + ' '

print(r[:-1])