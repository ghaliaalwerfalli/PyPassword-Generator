import random

still_working = True
while still_working:

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  #Propmts user input for number of desired number, letters and symbols 
  #Input gets stored in its associated variable
  print("Welcome to the PyPassword Generator!")
  user_letters= int(input("How many letters would you like in your password?\n")) 
  user_symbols = int(input("How many symbols would you like?\n"))
  user_numbers = int(input("How many numbers would you like?\n"))


  #empty variables that are converted to string
  ## will be used to turn letters, numbers and symbols lists all into strings
  looped_letters = str()
  looped_numbers = str()
  looped_symbols = str()


  #each for loop loops through one of the lists, selects one item randomly (import random)
  ### for each number in range of user's input (example: user input 4) will loop through related list 4 times picking a random item
  ### and adding that item in looped_letters (example: 4 loops with random picks = 8374 final number)
  for letter in range(user_letters):
    looped_letters += random.choice(letters)
  for number in range(user_numbers):
    looped_numbers += random.choice(numbers)
  for symbol in range(user_symbols):
    looped_symbols += random.choice(symbols)


  #concatenates all three looped variables together
  # shuffles randomly between each string in the concatenated variables
  all_loops = looped_letters + looped_numbers + looped_symbols
  shuffled_loops =''.join(random.sample(all_loops,len(all_loops)))
  print(f"Your randomly generated password is: {shuffled_loops}")


  #Prompts user to wether they wish to exit the application or to re-use it again to generate better password
  user_continue = input("Do you like that password or do you want to generate another one? [Y/n]: ").lower()
  if user_continue == 'n':
    still_working = False
    print("Thank you for using PyPassowrd Generator :)")
  else:
    still_working = True
    print("\n")