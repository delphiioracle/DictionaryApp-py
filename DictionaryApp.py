dictionary = {}

def Menu():
    print("\nDictionary App Menu:")
    print("1. Add a Word")
    print("2. Delete a Word")
    print("3. Edit a Word")
    print("4. View Dictionary")
    print("5. Search for a Word")
    print("6. Exit")

Menu()

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_word()

     elif choice == '6':
        print("Exiting Dictionary App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

        def add_word():
    word = input("Enter the word to add: ")
    definition = input("Enter the definition: ")
    dictionary[word] = definition
    print("Word added to the dictionary.")


    


