month = int(input())

if month == 12 or month == 1 or month == 2:


    print("зима")
elif 3 <= month <= 5:


    print("весна")
elif 6 <= month <= 8:


    print("лето")
elif 9 <= month <= 11:


    print("осень")
else:
    print("Введите номер месяца")
