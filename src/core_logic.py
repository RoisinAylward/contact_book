#importing modules to allow for csv files, locating files, and using regular expressions for error handling:
import csv
import os
import re


#checks if a csv file already exists to prevent overwriting, and creates one if it doesn't:
def ensure_csv_file():
  #conditional statement that executes the code within if the file does not exist:
  if not os.path.exists("contacts.csv"):
    #enables error handling for IOError if the code within does not work:
    try:
      #creates contacts.csv by opening it in write mode:
      with open("contacts.csv", mode="w") as file:
        #variable "writer" contains a defined row with 4 columns:
        writer = csv.DictWriter(file, fieldnames=["Name", "Number", "Email", "Address"])
        #writes the "writer" as the header row in the csv file:
        writer.writeheader()
    #executes if an IOError occurs:
    except IOError:
      #alerts the user of the problem and what they need to do:
      print("Error: Unable to create the 'contacts.csv' file.")



"""Valid Input functions:"""
#checks that the length of the input name is valid:
def valid_name_len(name):
  #returns the boolean of whether the length of the name input is at least 1 and no greater than 20:
  return 1 <= len(name) <= 20


#checks that all of the characters in the input phone number are valid:
def valid_number_char(number):
  #variable pattern that contains a format: ^ = start, + = 1+ occurrences, ? = optional, $ = end:
  pattern = r'^[+]?[0-9\-\(\) ]+$'
  #returns the boolean of the number containing digits and optionally hyphens, plus symbol, brackets, or spaces:
  return bool(re.match(pattern, number))

#checks that the length of the input phone number is valid:
def valid_number_len(number):
  #empty list called digits:
  digits = []
  #for loop with temporary variable "char" that indexes each character in the given number:
  for char in number:
    #conditional statement that executes the code within if the given character is a digit:
    if char.isdigit():
      #adds character to the list of digits:
      digits.append(char)
  #returns the boolean of the length of the digits being between 3(for numbers like 112 or 999) and 15:
  return 3 <= len(digits) <= 15

#checks that the input phone number is unique:
def valid_number_uniq(number):
  #opens contacts.csv file in reading mode:
  with open("contacts.csv", "r") as file:
    #variable "reader" contains the contents of the csv file:
    reader = csv.DictReader(file)
    #for loop that iterates each row in reader:
    for row in reader:
      #conditional statement that executes the code within if the data in the "number" column and the given row is a match to the input number:
      if row["Number"] == number:
        #returns a False boolean:
        return False
  #returns a True boolean if none of the rows contains a match to the input number:
  return True


#checks that all of the characters in the input email address are valid:
def valid_email_char(email):
  #variable pattern that contains a format: ^ = start, + = 1+ occurrences, ? = optional, $ = end:
  pattern = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  #returns the boolean of the email containing :
  return bool(re.match(pattern, email))

#checks that the length of the input email address is valid:
def valid_email_len(email):
  #returns the boolean of the email address having at least 6 characters and no more than 254 characters:
  return 6 <= len(email) <= 254 #(longest email length can be 254 characters according to RFC 2821)

#checks that the input email address is unique:
def valid_email_uniq(email):
  #opens contacts.csv file in reading mode:
  with open("contacts.csv", "r") as file:
    #variable "reader" contains the contents of the csv file:
    reader = csv.DictReader(file)
    #for loop that iterates each row in reader:
    for row in reader:
      #conditional statement that executes the code within if the data in the "email" column and the given row is a match to the input email:
      if row["Email"] == email:
        #returns a False boolean:
        return False
  #returns a True boolean if none of the rows contains a match to the input email:
  return True



"""operations functions:"""
#option 1, which displays all of the contact's name, number, email address, and address:
def view():
  #enables error handling if the code within does not work:
  try:
    #opens contacts.csv file in reading mode:
    with open("contacts.csv", "r") as file:
      #variable named "reader" that stores the file contents with a function to read the file:
      reader = csv.reader(file)
      #for loop that iterates each row in reader:
      for row in reader:
        #prints each row by joining its columns with a comma and a space in between:
        print(", ".join(row))
  #executes if a FileNotFoundError occurs:
  except FileNotFoundError:
    #alerts users of error:
    print("Error: The file 'contacts.csv' does not exist.")
  #executes if an error occurs:
  except Exception as e:
    #alerts users of error:
    print("Error:", e)

#option 2, which only displays contacts that contain a match to the query parameter:
def search(query):
  #enables error handling if code within does not work:
  try:
    #opens contacts.csv file in reading mode:
    with open("contacts.csv", "r") as file:
      #variable named "reader" that stores the file contents with a function to read the file:
      reader = csv.reader(file)
      #creates a false boolean:
      found = False
      #for loop that iterates each row in reader:
      for row in reader:
        #makes each row by joining its columns with a comma and a space in between:
        row_string = ", ".join(row)
        #conditional statement that executes the code within if the input query matches the given row string, with both variables being set to lowercase:
        if query.lower() in row_string.lower():  # Case-insensitive search
          #prints each row by joining its columns with a comma and a space in between:
          print(", ".join(row))
          #changes the value of the boolean found to true:
          found = True
      #conditional statement that executes the code within if the found boolean is still false after searching every row:
      if not found:
        #tells user that there are no contacts with their input query:
        print("No contacts found matching your search.")
  #executes if a FileNotFoundError occurs:
  except FileNotFoundError:
    #alerts the user of the error:
    print("Error: The file 'contacts.csv' does not exist.")
  #executes if an error occurs:
  except Exception as e:
    #alerts the user of the error:
    print("An error occurred:", e)

#option 3 which adds a contact with name, number, email, and address as the parameters:
def add(name, number, email, address):
  """checks validity of the inputs:"""
  #conditional statement that executes the code within if the boolean from executing the valid_name_len function with the input as the argument returned is false:
  if not valid_name_len(name):
    #throws a ValueError exception with an explanatory message to the user:
    raise ValueError("Invalid name. Please enter a name with a length between 1-20 characters")

  #conditional statement that executes the code within if the boolean from executing the valid_number_char function with the input as the argument returned is false:
  if not valid_number_char(number):
    #throws a ValueError exception with an explanatory message to the user:
    raise ValueError("Invalid phone number. Please enter a phone number which must contain digits and can optionally include hyphens, plus symbol, brackets, or spaces.")
  #conditional statement that executes the code within if the boolean from executing the valid_number_len function with the input as the argument returned is false:
  if not valid_number_len(number):
    #throws a ValueError exception with an explanatory message to the user:
    raise ValueError("Invalid phone number. Please enter a phone number with a length between 3-15 digits.")
  #conditional statement that executes the code within if the boolean from executing the valid_number_uniq function with the input as the argument returned is false:
  if not valid_number_uniq(number):
    #throws a ValueError exception with an explanatory message to the user:
    raise ValueError("Invalid phone number. Another contact already has that number.")

  #conditional statement that executes the code within if the boolean from executing the valid_email_char function with the input as the argument returned is false:
  if not valid_email_char(email):
    #throws a ValueError exception with an explanatory message to the user:
    raise ValueError("Invalid email address. Please enter an email address with the format user@example.com which can optionally include digits, underscores, and hyphens.")
  #conditional statement that executes the code within if the boolean from executing the valid_email_len function with the input as the argument returned is false:
  if not valid_email_len(email):
    #throws a ValueError exception with an explanatory message to the user:
    raise ValueError("Invalid email address. Please enter an email address with a length between 6-254 characters")
  #conditional statement that executes the code within if the boolean from executing the valid_number_uniq function with the input as the argument returned is false:
  if not valid_email_uniq(email):
    #throws a ValueError exception with an explanatory message to the user:
    raise ValueError("Invalid email address. Another contact already has that email address.")


  """actually adds the contact if no ValueError is raised:"""
  #enables error handling if the code within does not work:
  try:
    #opens contacts.csv file in append mode:
    with open("contacts.csv", "a") as file:
      #variable named "writer" that stores the file contents with a function to write the file:
      writer = csv.writer(file)
      #writes a row with name, number, email, and address as the columns:
      writer.writerow([name, number, email, address])
    #sends a message to the user to inform them that the contact has been added:
    print("Contact added.")
  #executes if an error occurs:
  except Exception as e:
    #alerts the error to the user:
    print("Error:", e)

#option 4, which deletes a contact with query as its parameter:
def delete(query):
  #enables error handling ifthe  code within does not work:
  try:
    #opens contacts.csv file in reading mode:
    with open("contacts.csv", "r") as file:
      #variable named "reader" that stores the file contents with a function to read the file:
      reader = csv.reader(file)
      #data type "rows" containing file contents casted into a list to process all rows at once:
      rows = list(reader)
      #conditional statement that executes the code within if the amount of rows is only one, containing the header:
      if len(rows) <= 1:
        #tells the user that there are no contacts stored:
        print("The contact list is empty.")
        #ends the function by returning nothing:
        return
      #boolean "found" with False as the value until later changed to True if there is a number in "rows" that matches the input query:
      found = False
      #for loop with the range starting on the second row after the first row (header) and ending after the last row:
      for i in range(1, len(rows)):
        #conditional statement that executes the code within if the given row in the second (Number) column matches the input query:
        if rows[i][1] == query:
          #removes the given row from "rows":
          rows.pop(i)
          #value of boolean "found" changed to True as a number in rows matches input query:
          found = True
          #ends the loop before more reiteration:
          break
    #conditional statement that executes code within if the found boolean value is changed to True because the input query DID match a number:
    if found:
      #opens contacts.csv file in reading mode:
      with open("contacts.csv", "w") as file:
        #variable named "writer" that stores the file contents with a function to overwrite the file:
        writer = csv.writer(file)
        #the csv file is overwritten with the list "rows" that no longer contains the deleted contact:
        writer.writerows(rows)
      #user is told that the contact has been deleted:
      print("Contact deleted successfully.")
    #conditional statement that executes code within if the found boolean value is still False because the input query did NOT match a number:
    else:
      #user is told that the contact has not been deleted as it never existed:
      print("No contacts found matching your search.")
  #executes if a FileNotFoundError occurs:
  except FileNotFoundError:
    #alerts the user of the error:
    print("Error: The file 'contacts.csv' does not exist.")
  #executes if an error occurs:
  except Exception as e:
    #alerts the user of the error:
    print("Error:", e)

#option 5, which updates a contact witha  query as its parameter:
def update(query):
  #enables error handling if code within does not work:
  try:
    #opens contacts.csv file in reading mode:
    with open("contacts.csv", "r") as file:
      #variable named "reader" that stores the file contents with a function to read the file:
      reader = csv.reader(file)
      #data type "rows" containing file contents casted into a list to process all rows at once:
      rows = list(reader)
      #conditional statement that executes the code within if the amount of rows is only one, containing the header:
      if len(rows) <= 1:
        #tells the user that there are no contacts stored:
        print("The contact list is empty.")
        #ends the function by returning nothing:
        return
      #boolean "found" with False as the value until later changed to True if there is a number in "rows" that matches the input query:
      found = False
      #for loop with the range starting on the second row after the first row (header) and ending after the last row:
      for i in range(1, len(rows)):
        #conditional statement that executes the code within if the given row in the second (Number) column matches the input query:
        if rows[i][1] == query:
          #prints if the number is found:
          print("Contact:")
          #prints the name (column 0), phone number (column 1), email address (column 2), and address (column 3) in the given row (i):
          print("Name:", rows[i][0], ", Number:", rows[i][1], ", Email:", rows[i][2], ", Address:", rows[i][3])

          #variable "name" that either stores typed in user input or the current value if the user just presses enter, to be used as the first column in the row:
          name = input("Enter new contact name or press enter without typing to keep current name [" + rows[i][0] + "]: ") or rows[i][0]
          #conditional statement that executes the code within if the boolean from executing the valid_name_len function with the input as the argument returned is false:
          if not valid_name_len(name):
            #throws a ValueError exception with an explanatory message to the user:
            raise ValueError("Invalid name. Please enter a name with a length between 1-20 characters")

          #variable "number" that either stores typed in user input or the current value if the user just presses enter, to be used as the second column in the row:
          number = input("Enter new contact phone number or press enter without typing to keep current phone number [" + rows[i][1] + "]: ") or rows[i][1]
          #conditional statement that executes the code within if the boolean from executing the valid_number_char function with the input as the argument returned is false:
          if not valid_number_char(number):
            #throws a ValueError exception with an explanatory message to the user:
            raise ValueError("Invalid phone number. Please enter a phone number which must contain digits and can optionally include hyphens, plus symbol, brackets, or spaces.")
          #conditional statement that executes the code within if the boolean from executing the valid_number_len function with the input as the argument returned is false:
          if not valid_number_len(number):
            #throws a ValueError exception with an explanatory message to the user:
            raise ValueError("Invalid phone number. Please enter a phone number with a length between 3-15 digits.")
          #conditional statement that executes the code within if the input number does not match the current value, and if the boolean from executing the valid_number_uniq function with the input as the argument returned is false:
          if number != rows[i][1] and not valid_number_uniq(number):
            #throws a ValueError exception with an explanatory message to the user:
            raise ValueError("Invalid phone number. Another contact already has that number.")

          #variable "email" that either stores typed in user input or the current value if the user just presses enter, to be used as the third column in the row:
          email = input("Enter new contact email address or press enter without typing to keep current email address [" + rows[i][2] + "]: ") or rows[i][2]
          #conditional statement that executes the code within if the boolean from executing the valid_email_char function with the input as the argument returned is false:
          if not valid_email_char(email):
            #throws a ValueError exception with an explanatory message to the user:
            raise ValueError("Invalid email address. Please enter an email address with the format user@example.com which can optionally include digits, underscores, and hyphens.")
          #conditional statement that executes the code within if the boolean from executing the valid_email_len function with the input as the argument returned is false:
          if not valid_email_len(email):
            #throws a ValueError exception with an explanatory message to the user:
            raise ValueError("Invalid email address. Please enter an email address with a length between 6-254 characters")
          #conditional statement that executes the code within if the input email does not match the current value, and if the boolean from executing the valid_email_uniq function with the input as the argument returned is false:
          if email != rows[i][2] and not valid_email_uniq(email):
            #throws a ValueError exception with an explanatory message to the user:
            raise ValueError("Invalid email address. Another contact already has that email address.")

          #variable "address" that either stores typed in user input or the current value if the user just presses enter, to be used as the fourth column in the row:
          address = input("Enter new contact address or press enter without typing to keep current address [" + rows[i][3] + "]: ") or rows[i][3]

          #overwrites the given row in "row" with the new inputs (including the unchanged):
          rows[i] = [name, number, email, address]
          #value of boolean "found" changed to True as a number in rows matches input query:
          found = True
          #ends the loop before more reiteration:
          break
    #conditional statement that executes code within if the found boolean value is changed to True because the input query DID match a number:
    if found:
      #opens contacts.csv file in reading mode:
      with open("contacts.csv", "w") as file:
        #variable named "writer" that stores the file contents with a function to overwrite the file:
        writer = csv.writer(file)
        #the csv file is overwritten with the list "rows" that no longer contains the updated contact:
        writer.writerows(rows)
      #user is told that the contact has been updated:
      print("Contact updated successfully.")
    #conditional statement that executes code within if the found boolean value is still False because the input query did NOT match a number:
    else:
      #user is told that the contact has not been updated as it never existed:
      print("No contacts found matching your search.")
  #executes if a FileNotFoundError occurs:
  except FileNotFoundError:
    #alerts the user of the error:
    print("Error: The file 'contacts.csv' does not exist.")
  #executes if an error occurs:
  except Exception as e:
    #alerts the user of the error:
    print("Error:", e)
