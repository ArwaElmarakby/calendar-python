import calendar
import datetime

def display_calendar():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    # Create a calendar object
    cal = calendar.monthcalendar(year, month)

    # Get the month name
    month_name = calendar.month_name[month]

    # Print the calendar header
    print(f"\n{month_name} {year}")
    print("Mo Tu We Th Fr Sa Su")

    # Print the calendar
    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end=" ")
            else:
                print(f"{day:2d}", end=" ")
        print()

    # Display current date
    today = datetime.date.today()
    print(f"\nToday's date: {today.strftime('%B %d, %Y')}")

# Run the calendar function
display_calendar()
