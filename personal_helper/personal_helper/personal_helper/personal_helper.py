from .address_book.address_book import main as address_book
from .notes.notes import main as notes
from .sort.sort import main as sort
from prettytable import PrettyTable

def main():
    print("\nHello, this is Personal Helper")

    table = PrettyTable(["Command", "instruction"])
    table.add_rows(
        [
            ["1", "Go to Address Book"],
            ["2", "Go to Notes"],
            ["3", "Go to Sorter"],
            ["4", "Exit the program"],
        ]
    )
    
    while True:
        print("\nPersonal Helper Menu:")
        print(table)
        string = input("Enter command to Personal Helper: ").lower()

        if string == "1":
            print("\n\nYou went to Address Book")
            address_book() 
            print("\n\nYou went to Personal Helper")
        elif string == "2":
            print("\n\nYou went to Notes")
            notes()
            print("\n\nYou went to Personal Helper")
        elif string == "3":
            print("\n\nYou went to Sorter")
            sort()
            print("\n\nYou went to Personal Helper")
        elif string == "4":
            print("Good bye!")
            break
        else:
            print("invalid command")

if __name__ == "__main__":
    main()