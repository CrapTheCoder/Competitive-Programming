for _ in range(int(input())):
    activities, origin = input().split()
    activities = int(activities)

    laddus = 0

    for _ in range(activities):
        inputs = input().split()

        win_type = inputs.pop(0)

        if win_type == 'CONTEST_WON':
            rank = int(inputs[0])
            laddus += max(0, 20 - rank) + 300

        if win_type == 'TOP_CONTRIBUTOR':
            laddus += 300

        if win_type == 'BUG_FOUND':
            severity = int(inputs[0])
            laddus += severity

        if win_type == 'CONTEST_HOSTED':
            laddus += 50

    if origin == 'INDIAN':
        print(laddus // 200)
    else:
        print(laddus // 400)