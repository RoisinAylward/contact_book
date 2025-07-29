#imports all (*) functions from core_logic.py withtin the same folder /src:
from core_logic import *

#executes the function from core_logic.py that ensures the contacts.csv exists to prevent it from being overwritten, and creates one if it does not:
ensure_csv_file()

#Creates a while loop that runs while the condition is true (forever until the break command is executed):
while True:
  #prints the options of the contact book menu with a number key to the user's screen:
  print("\nContact Book Menu:")
  print("1. View Contacts")
  print("2. Search Contact")
  print("3. Add Contact")
  print("4. Delete Contact")
  print("5. Update Contact")
  print("6. Exit")

  #variable "option" that stores user input to be used to determine the option:
  option = input("Choose an option: ")

  #allows for handling exceptions in error cases:
  try:

    #allows for handling exceptions in a specific error case of a non-integer being the input:
    try:
      #casts input string into an integer:
      option = int(option)
    #executes the code within if the string cannot be cast into an integer because the input was not a whole number:
    except ValueError:
      #throws a ValueError exception with an explanatory message to the user:
      raise ValueError("Invalid input. Please enter a whole number between 1-6.")

    #conditional statement that executes the code within it if the input is less than 1 or greater than 6:
    if option < 1 or  option > 6:
      #throws a ValueError exception with an explanatory message to the user:
      raise ValueError("Invalid input. Please enter a number between 1-6.")

    #conditional statement that executes the code within it if the input by the user is equivalent to 1, which corresponds to the selection View Contacts:
    elif option == 1:
      #executes the view function from core_logic.py:
      view()

    #conditional statement that executes the code within it if the input by the user is equivalent to 2, which corresponds to the selection Search Contact:
    elif option == 2:
      #variable "query" that stores user input to be used as an index in the list of contacts:
      query = input("Search for contact either by name, phone number, email address or address: ")
      #executes the search function from core_logic.py using query as argument:
      search(query)

    #conditional statement that executes the code within it if the input by the user is equivalent to 3, which corresponds to the selection Add Contact:
    elif option == 3:
      #variable "name" that stores user input to be used as the first element in a row of the list of contacts:
      name = input("Enter contact name: ")
      #variable "number" that stores user input to be used as the second element in a row of the list of contacts:
      number = input("Enter contact phone number: ")
      #variable "email" that stores user input to be used as the third element in a row of the list of contacts:
      email = input("Enter contact email address: ") #MAKE OPTIONAL AS WELL??
      #variable "address" that stores user input to be used as the fourth element in a row of the list of contacts:
      address = input("Enter contact address: ")
      #executes the add function from core_logic.py using name, number, email, and address as arguments:
      add(name, number, email, address)

    #conditional statement that executes the code within it if the input by the user is equivalent to 4, which corresponds to the selection Delete Contact:
    elif option == 4:
      #variable "query" that stores user input to be used as an index in the list of contacts:
      query = input("Enter the phone number of the contact to be deleted: ")
      #executes the delete function from core_logic.py using query as argument:
      delete(query)

    #conditional statement that executes the code within it if the input by the user is equivalent to 5, which corresponds to the selection Update Contact:
    elif option == 5:
      #variable "query" that stores user input to be used as an index in the list of contacts:
      query = input("Enter the phone number of the contact to be updated: ")
      #executes the update function from core_logic.py using query as argument:
      update(query)

    #conditional statement that executes the code within it if the input by the user is equivalent to 6, which corresponds to the selection Exit:
    elif option == 6:
      print("Exiting...")
      #ends the loop:
      break

  #executes if a ValueError occurs:
  except ValueError as e:
    #alerts the user of the problem and what they need to do:
    print("Error:", e)
    #ends the current iteration and starts the next one:
    continue
