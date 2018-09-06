# This script allows calculating the gross weekly pay based on the number of hours and the rate per hour.
# The hourly rate for any hour above 40 hours is 150% the basic rate.
# The script prompts the user for the amount of hours and for the rate per hour. 
# The input shall be in numeric format.
# An error is returned when the user provides invalid input.

print('This program allows calculating the weekly gross pay based on the number of hours and the rate per hour.')
def computepay(h,r): # Defining a function to make the calculation
  if h < 40: # Calculating the gross pay in case of no overtime
    gp = h * r
  else: # Calculating the gross pay in case of overtime
    gp = h * r + (h-40) * 0.5 * r # hours above 40 are payed 50% more
  return gp
print('Provide the work hours and the rate as positive (integer or decimal) numbers.')
hrs = input('"Enter Hours: ') # Getting the amount of hours
rate = input('Enter Rate: ') # Getting the hourly rate
try:
  h = float(hrs)
except: # Setting h to a negative value in case of non numerical input
  h = -1
try:
  r = float(rate)
except: # Setting h to a zero value in case of non numerical input
  r = 0
if h >= 0: # Checking that proper input (numerical and non negative) has been given for the hours
  if r > 0: # Checking that proper input (numerical and positive) has been given for the rate
    result = computepay(h,r) # Calling the function
    print("Weekly Pay:", result) # Returning the result
  else: # Action to be taken in case of invalid rate input
    print('Invalid Rate Input')
else: # Action to be taken in case of invalid hours input
  print('Invalid Hours Input') 