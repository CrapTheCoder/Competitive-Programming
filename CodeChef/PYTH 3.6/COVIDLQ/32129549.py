for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    followed = True

    last_person = -1  # -1 means there is no person yet

    for index in range(n):
        # If the current index has a person
        if a[index] == 1:
            # If there is a person till now
            if last_person != -1:
                # Check the gap between the current person and the last person
                if index - last_person < 6:
                    followed = False
                    break

            # Set the last_person to the current index
            last_person = index

    if not followed:
        print('NO')
    else:
        print('YES')
