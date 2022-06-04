n = input().strip()
l = len(n)

print('Yes' if all(int(n[:i+1]) % (l - i) == 0 for i in range(l)) else 'No')
