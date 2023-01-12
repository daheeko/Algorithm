days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
m, d = map(int, input().split())
week = "SUN, MON, TUE, WED, THU, FRI, SAT".split(", ")
print(week[(sum(days[:m])+d)%7])
    