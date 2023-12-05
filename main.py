from datetime import datetime, timedelta

def get_birthdays_per_week(users):

    today = datetime.now().date()

    birthdays_per_day = {i: [] for i in range(7)}


    for user in users:
        birthday = user['birthday'].date()
        days_until_birthday = (birthday - today).days

        if 0 <= days_until_birthday <= 7:
            day_of_week = (today + timedelta(days_until_birthday)).weekday()
            birthdays_per_day[day_of_week].append(user['name'])


    for day, celebrants in birthdays_per_day.items():
        day_name = datetime(2023, 1, 1).date().replace(day=day + 1).strftime('%A')
        if celebrants:
            print(f"{day_name}: {', '.join(celebrants)}")

users = [
    {'name': 'Bill', 'birthday': datetime(2023, 1, 4)},
    {'name': 'Jill', 'birthday': datetime(2023, 1, 6)},
    {'name': 'Kim', 'birthday': datetime(2023, 1, 7)},
    {'name': 'Jan', 'birthday': datetime(2023, 1, 8)}
]


get_birthdays_per_week(users)
