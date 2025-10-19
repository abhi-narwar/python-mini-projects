def menu():
    print("\n===== Journal Manager =====")
    print("1. Add Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Delete Entry")
    print("5. Exit")

def add_entry():
    date = input("Enter date (YYYY-MM-DD): ")
    title = input("Enter title: ")
    content = input("Write your journal:\n")

    with open("journal.txt", "a") as file:
        file.write(f"{date} | {title}\n")
        file.write(content + "\n")
        file.write("---\n")
    
    print("Entry added successfully!")
    
def add_entry():
    date = input("Enter date (YYYY-MM-DD): ")
    title = input("Enter title: ")
    content = input("Write your journal:\n")

    with open("journal.txt", "a") as file:
        file.write(f"{date} | {title}\n")
        file.write(content + "\n")
        file.write("---\n")
    
    print(" Entry added successfully!")
    
    
def view_entries():
    try:
        with open("journal.txt", "r") as file:
            data = file.read()
            if data.strip() == "":
                print("No entries found.")
            else:
                print("\n===== All Journal Entries =====")
                print(data)
    except FileNotFoundError:
        print("No journal file found.")

def search_entry():
    keyword = input("Enter date or title to search: ").lower()
    try:
        with open("journal.txt", "r") as file:
            data = file.read().split("---\n")
            found = False
            for entry in data:
                if keyword in entry.lower():
                    print("\n----- Found Entry -----")
                    print(entry)
                    found = True
            if not found:
                print("No matching entry found.")
    except FileNotFoundError:
        print("No journal file available.")

def delete_entry():
    keyword = input("Enter date or title of entry to delete: ").lower()

    try:
        with open("journal.txt", "r") as file:
            entries = file.read().split("---\n")
        
        new_entries = []
        deleted = False
        
        for entry in entries:
            if entry.strip() and keyword not in entry.lower():
                new_entries.append(entry)
            else:
                if entry.strip():
                    deleted = True
        
        with open("journal.txt", "w") as file:
            for entry in new_entries:
                file.write(entry + "\n---\n")
        
        if deleted:
            print("Entry deleted successfully!")
        else:
            print("No matching entry found.")
        
    except FileNotFoundError:
        print("No journal file available.")
        
while True:
    menu()
    choice = input("Enter option: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entry()
    elif choice == "4":
        delete_entry()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")


