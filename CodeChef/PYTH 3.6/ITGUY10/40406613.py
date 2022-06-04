pref = []

for i in range(10 ** 5 + 10):
    b = bin(i)[2:]
    if not any(b[j] == b[j+1] == '1' for j in range(len(b) - 1)):
        pref.append(i)
    else:
        pref.append(pref[-1])

for i in range(int(input())):
    print(pref[int(input())])
