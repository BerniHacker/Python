### Scraping Web Pages with Beautiful Soup

### To run this, download the file
### http://www.py4e.com/code3/bs4.zip
### and unzip it in the same directory as this file

### or install BeautifulSoup
### https://pypi.python.org/pypi/beautifulsoup4

### NOTE: for reasons of version compatibility,
### it is a bit harder to make this working with Jupyter Notebook.

### The program uses urllib to read HTML from a dynamically provided URL, 
### scans for an anchor tag that is in a dynamically provided position from the top of the page, 
### extracts the href= value from the tags and follows that link. 
### The program repeats the process a dynamically provided number of times and 
### prints the visible text behind the last found link.
### Validation of user input is performed and if it is negative the program asks again for input.

## Setup
# Importing the needed libraries
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

## Getting and validating user input
# Asking for the url input
url = input('Enter URL: ')
while True:
    # Asking for the wished tag position
    position = input('Enter the wished tag position (integer >= 1): ')
    try:
        pos = int(position) # Converting from string to integer
    except:
        print('Invalid input (not integer)') # Printing an error message if the user does not insert a integer number
        continue # Allowing a new attempt
    if pos < 1: # Validating the range
        print('Invalid range (negative number or zero)') # Printing an error message if the user does not insert a positive integer number
        continue # Allowing a new attempt
    # Asking for the wished number of iterations
    iterations = input('Enter the wished number of iterations (integer >= 1): ')
    try:
        iterat = int(iterations) # Converting from string to integer
    except:
        print('Invalid input (not integer)') # Printing an error message if the user does not insert a integer number
        continue # Allowing a new attempt
    if iterat < 1: # Validating the range
        print('Invalid range (negative number or zero)') # Printing an error message if the user does not insert a positive integer number
        continue # Allowing a new attempt
    break # Exiting the loop    

## Going to the url, getting the contained links and extracting the link in the wished position
# Initializing a counter
c = 0
while c < iterat:
    # Reading the all content of the provided url as a single string
    html = urllib.request.urlopen(url, context=ctx).read()
    # Parsing
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieving all of the anchor tags
    tags = soup('a')
    # Updating the value of the url for the next loop
    url = tags[pos - 1].get('href', None)
    # Incrementing the counter
    c += 1    

## Returning the visible text behind the selected link
content = tags[pos - 1].contents[0]
print(content)
