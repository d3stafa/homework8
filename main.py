from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    today = datetime.now().date()

    # Створюємо словник для збереження іменинників за кожний день тижня
    birthdays_per_day = {i: [] for i in range(7)}

    # Заповнюємо словник іменинниками
    for user in users:
        birthday = user['birthday'].date()
        days_until_birthday = (birthday - today).days

        if 0 <= days_until_birthday <= 7:
            day_of_week = (today + timedelta(days_until_birthday)).weekday()
            birthdays_per_day[day_of_week].append(user['name'])

    # Виводимо результат
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day, celebrants in birthdays_per_day.items():
        day_name = days_of_week[day]
        if celebrants:
            print(f"{day_name}: {', '.join(celebrants)}")

# Тестовий список користувачів
users = [
    {'name': 'Bill', 'birthday': datetime(2023, 1, 4)},
    {'name': 'Jill', 'birthday': datetime(2023, 1, 6)},
    {'name': 'Kim', 'birthday': datetime(2023, 1, 7)},
    {'name': 'Jan', 'birthday': datetime(2023, 1, 8)}
]

# Викликаємо функцію для тестування
get_birthdays_per_week(users)