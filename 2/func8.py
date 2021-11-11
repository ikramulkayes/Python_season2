def timeconverter(days):
    years = days // 365
    days = days % 365
    months = days // 30
    days = days % 30


    print(f"{years} years, {months} months and {days} days")

days = input("Enter number of days: ")
days = int(days)
timeconverter(days)