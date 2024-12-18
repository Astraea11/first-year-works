import os

# CONSTANTS
MINIMUM_GRADE = 65
MAXIMUM_GRADE = 100
HEADER = "Name, Grade:\n"


def open_record():
    filename = input("Enter the file name: ").strip()
    filename += ".txt" if not filename.endswith(".txt") else ""
    if os.path.exists(filename):
        return filename
    else:
        print("File does not exist")


def create_file():
    filename = input("Enter the file name: ").strip()
    filename += ".txt" if not filename.endswith(".txt") else ""
    if filename:
        with open(filename, 'w') as file:
            file.write(HEADER)
        print(f"{filename} successfully created!")


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def add_grade():
    filename = open_record()
    if not filename:
        return
    name = input("Enter name of the student: ").strip()
    grade = input("Enter their grade: ").strip()
    while is_number(grade) == False:
        grade = input("Please enter a number for their grade: ").strip()
    grade = float(grade)
    if MINIMUM_GRADE < grade < MAXIMUM_GRADE:
        with open(filename, 'a') as file:
            file.write(f"{name} - {grade}\n")
        print("Student and grade added successfully!\n")
    else:
        print(f"Grade must be between {MINIMUM_GRADE} and {MAXIMUM_GRADE}")


def delete_record():
    filename = open_record()
    if not filename:
        return

    with open(filename) as file:
        lines = file.readlines()

    line_number = int(input("Enter the line you wish to delete").strip())

    if line_number <= len(lines) and line_number >= 1 :
        del lines[line_number - 1]
        print("Student record deleted successfully!")

        with open(filename, 'w') as file:
            for line in lines:
                file.write(line)

    else:
        print(f"line {line_number} not found in file.")


def perma_delete_record():
    filename = open_record()

    if filename:
        os.remove(filename)
        print("Record permanently deleted")


def wipe_record():
    filename = open_record()

    if filename:
        with open(filename, 'w') as file:
            file.write(HEADER)
        print("Record has been wiped.")


def perma_delete_all_records():
    [os.remove(file) for file in os.listdir() if file.endswith(".txt")]
    print("All records have been permanently deleted.")


def display_record():
    filename = open_record()
    if not filename:
        return
    if filename:
        with open(filename, 'r') as file:
            print(file.read())


def display_all_records():
    active_files = [record for record in os.listdir() if record.endswith(".txt")]
    print("All active records")
    print("\n".join(active_files) or "No records found")


def end_program():
    print("Program ended")
    exit()


def menu(options):
    print()
    print("\n".join([f"{key} - {value[1]}" for key, value in options.items()]))


MENU_OPTIONS = {  # Number - Function call - Description for menu
    1: [create_file, "Create a new record"],
    2: [add_grade, "Add to record"],
    3: [delete_record, "Delete a record"],
    4: [display_record, "Display a record"],
    5: [display_all_records, "Display all current records"],
    6: [wipe_record, "Wipe a record"],
    7: [perma_delete_record, "Permanently delete a record"],
    8: [perma_delete_all_records, "Permanently delete all records"],
    9: [end_program, "Exit"]
}


def main():
    print("Teacher Grade Appender")
    while True:
        menu(MENU_OPTIONS)
        choice = input(f"\nEnter choice(1-{len(MENU_OPTIONS)}): ").strip()  # automatically format!
        if choice.isdigit() and int(choice) in MENU_OPTIONS:
            MENU_OPTIONS[int(choice)][0]()
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
