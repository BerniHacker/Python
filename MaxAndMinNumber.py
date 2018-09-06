# This sript allows calculating the largest and the smallest values of a series of numbers.
# The script repeatedly prompts the user for integer or decimal numbers until the user enters 
# the string 'done'.
# Once 'done' is entered, it prints out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number, an errror message is returned.   
print('This program allows calculating the nimimum and maximim values of a series of numbers.')
print('The numbers shall be inserted as requested by the program.')
print('To terminate the list of numbers, type "done".')
largest = None # Initializing with Note Type flag value
smallest = None # Initializing with Note Type flag value
while True:
    num = input("Enter a number: ") # Getting the number in string format
    if num == "done" : # Checking if the user wants to terminate the list
      break # Quitting the loop
    try:
      fnum = float(num) # converting the number into floating point format
    except:
      print('Invalid input. Insert an integer or a decimal number.') # Printing an error message
        # if the user does not insert a number
      continue # Allowing a new attempt to insert a number (going to the start of the loop)                                                  
    if smallest is None : # Replacing the None value with a number in the first loop
      smallest = fnum
    if largest is None : # Replacing the None value with a number in the first loop
      largest = fnum  
    if fnum < smallest: # Updating the result
      smallest = fnum
    if fnum > largest: # Updating the result
      largest = fnum  
print('The minimum value is', smallest) # Returning the result
print('The maximum value is', largest) # Returning the result
