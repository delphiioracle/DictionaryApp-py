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
    Menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        Add()
    elif choice == '2':
        Delete()
    elif choice == '3':
        Edit()
    elif choice == '4':
        View()
    elif choice == '6':
        print("Exiting Dictionary App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

        def Add():
    word = input("Enter the word to add: ")
    definition = input("Enter the definition: ")
    dictionary[word] = definition
    print("Word added to the dictionary.")

    def Delete():
    word = input("Enter the word to delete: ")
    if word in dictionary:
        del dictionary[word]
        print("Word deleted from the dictionary.")
    else:
        print("Word not found in the dictionary.")
while True:
    Menu()
    choice = input("Enter your choice: ")

    def Edit():
    word = input("Enter the word to edit: ")
    if word in dictionary:
        new_definition = input("Enter the new edit: ")
        dictionary[word] = new_definition
        print("Word edited successfully.")
    else:
        print("Word not found in the dictionary.")
while True:
    Menu()
    choice = input("Enter your choice: ")

    def View():
    print("\nDictionary Contents:")
    for word, definition in dictionary.items():
        print(f"{word}: {definition}")
        while True:
    Menu()
    choice = input("Enter your choice: ")


    


