for _ in range(int(input())):
    year, month, date = map(int, input().split(':'))

    count = 1
    last = date % 2

    while True:
        days_in_months = {
            1: 31,
            2: 28 + (not year % 4 if year % 100 else not year % 400),
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        date += 2

        if date > days_in_months[month]:
            date -= days_in_months[month]
            month += 1
        if month > 12:
            year += 1
            month = 1

        if date % 2 != last:
            break
        else:
            count += 1

    print(count)