# This program reads a e-mail file and finds out who has sent the greatest number of messages. 
# An example of such a file can be found at http://www.py4e.com/code3/mbox-short.txt
# 
# Retrieving data
fname = input('Enter file name:') # Asking for user input
fhandle = open(fname) # Opening the file
# Building a dictionary
counts = dict() # Creating a dictionary
for line in fhandle: # Going through each line of the file
    if not line.startswith('From: '): continue # Filtering out non target lines (non "From:" lines)
    words = line.split() # Splitting the line into a list of words
    person = words[1] # Extracting the sender's mail address from the line
    counts[person] = counts.get(person,0) + 1 # Adding the sender's mail address to the 
                                              # dictionary with a count of the number of times
                                              # the address appears in the file
# Running a maximum loop to find the most frequest e-mail address
totcount = None # Initializing the variable containing the final counter
totperson = None # Initializing the variable containing the most frequent person
for person,count in counts.items(): # Going through each tuple of the dictionary
    if totcount is None or count > totcount: # If is is the first word or if the counter 
                                             # for the word is bigger than the final counter
        totperson = person # Update the final variable
        totcount = count # Update the final variable
# Printing the result
print('The most common e-mail address is:', totperson)
print('The address has appeared:', totcount, 'times')