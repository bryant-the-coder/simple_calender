import calendar

year = int(input("Please type in your desire year: "))
month = int(input("Please type in your desire month: "))

while month > 12:
    print("That isnt a valid month")
    month = int(input("Please retype in your desire month: "))

print("\n", calendar.month(year, month))
