from datetime import datetime
import calendar


class Test:
    def __init__(self, year, monthly_allowance):
        self.occurrences = []
        self.year = year
        self.monthly_allowance = monthly_allowance
        self.remaining_allowance = monthly_allowance

    def add_event(self, reason, occurrence_datetime, amount_spent=0): # this one adds to the dictionary
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

    def view_occurrences(self): # shows the records
        if not self.occurrences:
            print("No monthly allowance change.")
            return

        print("All occurrences of monthly allowance spent: ")
        print(f"Monthly allowance left: ₱{self.remaining_allowance}")
        for occ in self.occurrences:
            print(f"{occ['datetime']}, {occ['day']} - Reason: {occ['reason']} | Amount spent: ₱{occ['amount_spent']}")

    def add_eventt(self): # this one asks for the input that then adds to the add_event function
        # i didnt have a better way to name it
        date = input("Enter occurrence date and time (MM-DD HH:MM 24hr base): ")
        reason = input("Enter reason of deduction: ")
        try:
            amount_spent = int(input("Enter the amount spent: "))
            if amount_spent > self.remaining_allowance:
                print("Amount exceeds remaining allowance. Please enter a valid amount.")
                return
            occurrence_datetime = datetime.strptime(f"{self.year} {date}", "%Y %m-%d %H:%M")
            self.add_event(reason, occurrence_datetime, amount_spent)
        except ValueError:
            print("Invalid date and time format. Please try again.")


def display_calendar(year, month): # displays the calendar for specific month and year asked
    # just helps the user keep track of what day and date it is lmao
    try:
        if 1 <= month <= 12:
            calendar.setfirstweekday(calendar.SUNDAY)
            print("\n", calendar.month(year, month))
        else:
            print("Invalid month. Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter numeric values for year and month.")


def end_program():
    print("Program ended.")
    exit()


def menu(options):
    print()
    print("\n".join([f"{key} - {value[1]}" for key, value in options.items()]))


def main():
    # asks for the users input for the given year, month, and allowance
    print("Monthly allowance recorder: ")
    year = int(input("Enter the year (e.g., 2024): "))
    month = int(input("Enter the month (1-12): "))
    monthly_allowance = int(input("Enter your monthly allowance: ₱"))
    display_calendar(year, month)
    test_instance = Test(year, monthly_allowance)

    menu_options = {
        1: [test_instance.add_eventt, "Add an occurrence"],
        2: [test_instance.view_occurrences, "View occurrences"],
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
