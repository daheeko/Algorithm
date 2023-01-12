def day_of_month(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 28

def get_days(month, day):
    days = 0
    for i in range(1, month):
        days += day_of_month(i)
    days += day
    return days

def day_of_week(days):
    week = "SUN, MON, TUE, WED, THU, FRI, SAT".split(", ")
    return week[days%7]

if __name__ == "__main__":
    month, day = map(int, input().split())
    print(day_of_week(get_days(month, day)))