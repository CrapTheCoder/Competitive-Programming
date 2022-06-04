import datetime

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

for _ in range(int(input())):
    year = int(input())
    day = datetime.date(year, 1, 1).weekday()

    print(days[day])