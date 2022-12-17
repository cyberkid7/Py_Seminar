# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным

print("Enter the day of the week from 1 to 7: ")
day_week = int(input())
if day_week == 6 or day_week == 7:
    print("It's WEEKEND!")
elif day_week < 6:
    print("It's WORKDAY!")
elif day_week > 7:
    print("You entered the wrong number. There are only 7 days in a week. Enter the day of the week from 1 to 7")
elif day_week == str:
    print("There are only 7 days in a week. Enter the day of the week from 1 to 7")

