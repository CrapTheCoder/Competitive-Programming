m = input()
n = int(m[-2:])

if n % 4 == 0: print(m)
if n % 4 == 1: print(1)
if n % 4 == 2: print(int(m) + 1)
if n % 4 == 3: print(0)
