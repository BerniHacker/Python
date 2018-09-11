## Finding the 10 most common words
# This program reads a text file to find the 10 most common words and their occurrences
#
# Retrieving data
fname = input('Enter file name:') # Asking for user input
fhandle = open(fname) # Opening the file
# Building a dictionary
counts = dict() # Creating a dictionary
for line in fhandle: # Going through each line
    words = line.split() # Splitting the line into words
    for word in words: # Going through each word
        counts[word] = counts.get(word,0) + 1 # Counting the words and adding them in the dictionary
# Inverting the order of key and value tuples in the dictionary
lst = [] # Creating an empy list
for key, val in counts.items():
    newtup = (val, key) # Creating a new tuple inverting the order of key and value
    lst.append(newtup) # Adding the new tuple to the list
lst = sorted(lst, reverse=True) # Sorting the list in descending order
# Printing the result
print('The 10 most common words in the file', fname, 'are:')
for val, key in lst[:10] : # Selecting the first 10 entries
    print('Word:', key)
    print('Occurrence:', val)