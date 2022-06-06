n = int(input())

coinlist = list(input().split())
pocketlist = []

for pockets in range(n):
pock = 1

for coins in range(n):
if pockets == coins:
continue
if coinlist[pockets] == coinlist[coins]:
pock += 1

pocketlist.append(pock)

print(max(pocketlist))