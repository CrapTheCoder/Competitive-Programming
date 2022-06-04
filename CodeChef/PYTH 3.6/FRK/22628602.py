c = 0

for _ in range(int(input())):
    s = input()
    c += any(i in s for i in ['ch', 'he', 'ef'])

print(c)