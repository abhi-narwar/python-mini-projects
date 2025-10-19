
FILENAME = 'journal.txt'

def write_entry():
   
    entry = input('Write your journal entry: ') + '\n'
    
    with open(FILENAME, 'a') as file:
        file.write(entry)

def read_all():
    
    try:
        
        with open(FILENAME, 'r') as file:
            print('\nAll Journal Entries:')
           
            print(file.read())
    except FileNotFoundError:
        
        print("\nJournal file not found. Try adding an entry first.")

def search():

    keyword = input('Enter keyword to search: ')
    try:
        with open(FILENAME, 'r') as file:
            
            all_lines = file.readlines()
            for line in all_lines:
                
                if keyword.lower() in line.lower():
                    
                    print(line.strip())
                    
                    return
            
            print('No matching entries.')
    except FileNotFoundError:
        print("\nJournal file not found. Try adding an entry first.")

def main_menu():
    
    while True:
        print('\n==== File Journal Menu ====')
        print('1. Add Entry')
        print('2. Read All Entries')
        print('3. Search Entries')
        print('4. Exit')

        choice = input('Choose option (1-4): ')

        if choice == '1':
            write_entry()
        elif choice == '2':
            read_all()
        elif choice == '3':
            search()
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice.')


if __name__ == "__main__":
    main_menu()