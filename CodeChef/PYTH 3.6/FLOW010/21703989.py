types = {
    'b': 'BattleShip',
    'c': 'Cruiser',
    'd': 'Destroyer',
    'f': 'Frigate'
}

for _ in range(int(input())):
    s = input().lower()

    print(types[s])