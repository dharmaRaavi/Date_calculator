from datetime import datetime, timedelta


# To convert user's input from the console into date
def get_date():
    while True:
        try:
            date_str = input("Enter date (YYYY-MM-DD): ")
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("The date format entered is invalid! Please try using YYYY-MM-DD.")


# Function to find the number of days between two dates
def date_difference():
    print("\nLet's find out the difference between two dates!")
    date1 = get_date()
    date2 = get_date()
    diff = abs((date2 - date1).days)
    print(f"The difference is {diff} days.")


# Function to add or subtract days from a date
def add_subtract_days():
    print("\nLet's add or subtract days from a date!")
    date = get_date()
    days = int(input("Enter number of days (+ to add, - to subtract): "))
    new_date = date + timedelta(days=days)
    print(f"The new date is {new_date}.")


# Function to find which day of the week a particular date falls on
def find_weekday():
    print("\nLet's find out what day of the week a date falls on!")
    date = get_date()
    print(f"{date} is a {date.strftime('%A')}.")


# The main function to call everything
def main():
    print("\nWelcome to the Date Calculator!")

    while True:
        print("\nWhat do you want to do?")
        print("1. Find the number of days between two dates")
        print("2. Add or subtract days from a date")
        print("3. Find the day of the week for a date")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            date_difference()
        elif choice == "2":
            add_subtract_days()
        elif choice == "3":
            find_weekday()
        elif choice == "4":
            print("\nThanks for using the Date Calculator! Have a great day!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
