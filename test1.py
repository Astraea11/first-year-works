import os
import logo

#-----------------------ALL MAIN FUNCTIONS BELOW-----------------------

def search_file():
    # guard clause function, returns None if no filename was found, returns filename if it was found
    name = input("Enter the file name (without .txt): ")
    filename = name + '.txt'
    if not os.path.exists(filename): # if file doesn't exist, return None
        print("Specified file does not exist.")
        return None
    return filename # if it exists, return filename.txt

def create_file():
    # creates a new file
    name = input("Enter file name (without .txt): ")
    if os.path.exists(name + '.txt'): # if filename already exists, leave function to prevent duplicate files
        print("Please choose another file name. This file already exists.")
        return
    with open(name + '.txt', "a") as f:
        text = input("Enter your text:\n> ")
        f.write(text)
    f.close()

def read_file():
    # read entire file
    filename = search_file()
    if not filename: # if file doesn't exist, leave function
        return
    with open(filename, "r") as f:
        print(f"> {f.read()}")
    f.close()

def edit_file():
    # edit file with two options, rewrite file or replace word
    filename = search_file()
    if not filename: # if file doesn't exist, leave function
        return
    option = int(input("Choose an option\n1. Rewrite everything\n2. Replace a specific word\n> "))
    if option == 1: # rewrites everything
        with open(filename, 'w') as f:
            f.write(input("Enter your text:\n> "))
        print("File updated successfully.")
    elif option == 2: # replace a specific word by getting all text into a single variable and splitting into a list
        with open(filename, 'r') as f:
            text = f.read() # get all text into a single variable
        all_words = text.split() # split all the text so we have all words inside a list
        max_index_width = len(str(len(all_words))) # Calculate the width needed for formatting index numbers
        print("Original Text:")
        for i, word in enumerate(all_words, start=1): # prints out original text with index number in front of every word
            print(f"{i:>{max_index_width}} {word}", end=" ")
        print()

        word_index = int(input("Enter the number of the word you want to replace\n> "))
        if len(all_words) < word_index or word_index < 1: # guard clause to prevent out of bounds indexing
            print("Invalid word index.")
            return
        new_word = input("Enter the replacement word:\n> ")
        all_words[word_index - 1] = new_word # replaces the word at the index with the new word
        with open(filename, 'w') as f: # rewrite entire file with updated replaced word
            f.write(' '.join(all_words))
        print("Word replaced successfully.")

def delete_file():
    # delete file using os
    filename = search_file()
    if filename: # if filename exists
        os.remove(filename)
        print("File deleted successfully!")

def wipe_out():
    # delete all text files using list comprehension
    files = [file for file in os.listdir() if file.endswith(".txt")] # get all files that end with .txt inside the current directory inside list
    for file in files:
        os.remove(file)
    print("All diaries have been deleted!")

def end_program():
    # end program with logo card
    print()
    logo.end_card()
    exit()

def print_active_files():
    # prints all active text files, or "No current files" if None
    cwd = os.getcwd()
    active_files = [file for file in os.listdir(cwd) if file.endswith(".txt")] # get all files that end with .txt inside the current directory inside list
    print("........................\nLogs:")
    print("\n".join(active_files) or "No current files")
    print("........................")

def display_menu(options):
    # displays menu with options
    print("--------------------")
    for key, value in options.items():
        print(f"{key}. {value[1]}")
    print("--------------------")

#-----------------------ALL MAIN FUNCTIONS ABOVE-----------------------

options = { # Dictionary storing function calls and description for menu
    1: [create_file, "Write a Diary"],
    2: [read_file, "Read your Diary"],
    3: [edit_file, "Edit your Diary"],
    4: [delete_file, "Delete your Diary"],
    5: [wipe_out, "Delete all Diaries"],
    6: [end_program, "End Program"]
}

def main():
    logo.title()
    print("Welcome to your diary!")
    while True:
        print()
        print_active_files()
        display_menu(options)
        choice = input("Enter your choice: ")
        if choice.isdigit() and int(choice) in options:
            options[int(choice)][0]() # uses dictionary to call functions instead of multiple if-else statements
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
