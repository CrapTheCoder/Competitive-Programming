dates = []

for _ in range(int(input())):
    date, month, year = map(int, input().split('/'))
    dates.append((date, month, year))

dates.sort(key=lambda x: x[0])
dates.sort(key=lambda x: x[1])
dates.sort(key=lambda x: x[2])

print(*[f'{date}/{month}/{year}' for date, month, year in dates], sep='\n')
