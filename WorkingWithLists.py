# This program allows opening a text file and reading it line by line. 
# Each line is split into a list of words.
# Each word is added to a master list containing no duplicates and then this list is sorted
# in alphabetical order.

fname = input("Enter file name: ") # getting the file name from the user
fhandle = open(fname) # opening the file
wordlist = list() # creating the output list
for line in fhandle: # going through the lines of the file
  words = line.split() # # creating a list of the words of the line
  for word in words: # going throgh the list of words
    if word in wordlist: continue # checking if the word belongs to the output list and 
    # going back to the previous line if it does
    wordlist.append(word) # adding the word to the outout list
wordlist.sort() # sorting in alphabetical order (big letters come first)
print(wordlist) # getting the result   