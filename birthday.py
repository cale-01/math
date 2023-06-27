def calculate_day_of_birth(day, month, year):
    if month == 1 or month == 2:
        month += 12
        year -= 1

    q = day
    m = month
    K = year % 100
    J = year // 100

    h = (q + 13*(m+1)//5 + K + K//4 + J//4 + 5*J) % 7

    days_of_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    day_of_week = days_of_week[h]

    return day_of_week


# birth_day = 25
# birth_month = 12
# birth_year = 1990

# Input for birthdate
birth_day = int(input("Enter the birth day (1-31): "))
birth_month = int(input("Enter the birth month (1-12): "))
birth_year = int(input("Enter the birth year (e.g., 1990): "))

day_of_birth = calculate_day_of_birth(birth_day, birth_month, birth_year)
print("You were born on a", day_of_birth)
