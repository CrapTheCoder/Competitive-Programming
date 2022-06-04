types = {
    0: "Beginner",
    1: "Junior Developer",
    2: "Middle Developer",
    3: "Senior Developer",
    4: "Hacker",
    5: "Jeff Dean",
}

for i in range(int(input())):
    l = list(map(int, input().split()))
    print(types[l.count(1)])