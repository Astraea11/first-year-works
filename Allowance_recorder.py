from datetime import datetime
import calendar
import re


class Recorder:
    def __init__(self, month, year, monthly_allowance):
        self.occurrences = []
        self.month = month
        self.year = year
        self.monthly_allowance = monthly_allowance
        self.remaining_allowance = monthly_allowance

    def record_event(self, reason, occurrence_datetime, amount_spent=0):  # this one adds to the dictionary
        day = calendar.day_name[occurrence_datetime.weekday()]
        if amount_spent <= 0:
            print("No deduction detected.")
        else:
            self.occurrences.append(
                {"reason": reason, "day": day, "datetime": occurrence_datetime, "amount_spent": amount_spent})
            self.remaining_allowance -= amount_spent
            print("Successfully added to the list of monthly spending.")

            if self.remaining_allowance < 1000:
                print(f"Warning: Your allowance is running low. Only ₱{self.remaining_allowance} left.")

    def view_occurrences(self):  # shows the records
        if not self.occurrences:
            print("No monthly allowance change.")
            return

        print("All occurrences of monthly allowance spent: ")
        print(f"Monthly allowance left: ₱{self.remaining_allowance}")
        for occ in self.occurrences:
            print(f"{occ['datetime']}, {occ['day']} - Reason: {occ['reason']} | Amount spent: ₱{occ['amount_spent']}")

    def add_event(self):  # this one asks for the input that then adds to the record_event function
        date = input("Enter occurrence date: ")
        while date.isdigit() is False or int(date) > number_of_days_in_month(self.year, self.month):
            date = input("Please enter a valid occurrence date: ")
        time = input("Enter occurrence time (hh:mm 24hr base): ")
        while is_valid_time(time) is False:
            time = input("Please enter a valid occurrence time (hh:mm 24hr base): ")
        reason = input("Enter reason of deduction: ")
        try:
            amount_spent = int(input("Enter the amount spent: "))
            if amount_spent > self.remaining_allowance:
                print("Amount exceeds remaining allowance. Please enter a valid amount.")
                return
            occurrence_datetime = datetime.strptime(f"{self.year} {self.month}-{date} {time}", "%Y %m-%d %H:%M")
            self.record_event(reason, occurrence_datetime, amount_spent)
        except ValueError:
            print("Invalid date and time format. Please try again.")


def display_calendar(year, month):  # displays the calendar for specific month and year asked
    try:
        if 1 <= month <= 12:
            calendar.setfirstweekday(calendar.SUNDAY)
            print("\n", calendar.month(year, month))
        else:
            print("Invalid month. Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter numeric values for year and month.")


def is_valid_time(timestamp):  # it uses the regex engine for validating time
    pattern = r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'
    return bool(re.match(pattern, timestamp))


def is_valid_year(year, min_year=2000, max_year=2030):  # validates the year if it fits the min and max requirement
    if year.isdigit():
        year = int(year)
        if min_year <= year <= max_year:
            return True
    return False


def number_of_days_in_month(year, month):
    # monthrange returns a tuple where the second value is the number of days in the month
    # returns the number of days starting from 1 in the tuple
    return calendar.monthrange(year, month)[1]


def end_program():
    print("Program ended.")
    exit()


def menu(options):
    print()
    print("\n".join([f"{key} - {value[1]}" for key, value in options.items()]))


def main():
    # asks for the users input for the given year, month, and allowance
    # also checks and validates if the year and month given are reasonable
    print("Monthly Allowance Recorder: ")
    year_str = input("Enter the year (e.g., 2024): ")
    while not is_valid_year(year_str):
        year_str = input("Please input a valid year from 2000 to 2030: ")
    year = int(year_str)
    month_str = input("Enter the month (1-12): ")
    while not (month_str.isdigit() and 1 <= int(month_str) <= 12):
        month_str = input("Please enter a valid month: ")
    month = int(month_str)
    monthly_allowance = int(input("Enter your monthly allowance: ₱"))
    while monthly_allowance <= 0:
        monthly_allowance = int(input("Please enter a valid monthly allowance: ₱"))
    display_calendar(year, month)
    recorder_instance = Recorder(month, year, monthly_allowance)

    menu_options = {
        1: [recorder_instance.add_event, "Add an occurrence"],
        2: [recorder_instance.view_occurrences, "View occurrences"],
        3: [end_program, "Exit"]
    }

    while True:
        menu(menu_options)
        choice = input(f"\nEnter choice(1-{len(menu_options)}): ").strip()
        if choice.isdigit() and int(choice) in menu_options:
            menu_options[int(choice)][0]()
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
