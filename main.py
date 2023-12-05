from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    today = datetime.today()
    next_week = today + timedelta(days=7)
    for i in range(7):
        day = today + timedelta(days=i)
        if day.weekday() == 6:
            continue
        print(f"{weekdays[i]}: ", end="")
        for user in users:
            if user['birthday'].weekday() == i:
                print(f"{user['name']}, ", end="")
        print()
        if day == next_week:
            break
users = [
        {'name': 'Bill', 'birthday': datetime(2023, 1, 4)},
        {'name': 'Jill', 'birthday': datetime(2023, 1, 6)},
        {'name': 'Kim', 'birthday': datetime(2023, 1, 7)},
        {'name': 'Jan', 'birthday': datetime(2023, 1, 8)}
    ]

get_birthdays_per_week(users)
