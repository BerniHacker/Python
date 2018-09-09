# This program allows opening and reading a file to look for lines of a certain form: 
# (X-DSPAM-Confidence:    0.8475)
# The program returns the average floating point values from each of the lines.
# The used file is available at http://www.py4e.com/code3/mbox-short.txt 

fname = input("Enter the file name: ") # Getting the file name
fhandle = open(fname) # Opening the file
count = 0 # Initializing the line counter
tot = 0 # Initializing the value for the sum
for line in fhandle: # Going through the lines
  if line.startswith('X-DSPAM-Confidence:'): # Selecting the lines
    pos = line.find(':') # Defining a marker for extracting a substring
    subs = line[pos+1:] # Defining the substring
    subs = subs.lstrip() # Removing the writespaces
    subs = float(subs) # Concerting the substring to a floating number
    tot = tot + subs
    count = count + 1 # Increasing the line counter
avg = tot / count # Computing the average
print('Average spam confidence:', avg) # Printing the result