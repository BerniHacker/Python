#### This program prompts for a URL, reads the XML data from that URL, extracts
### some data and does some calculation.
### The data consists of a number of names and counts as follows: 
### <comment>
###   <name>Matthias</name>
###   <count>97</count>
### </comment>
### The program computes the sum of all the counts.
### It can be tested for example with the following URL: http://py4e-data.dr-chuck.net/comments_133458.xml

## Setup
# Importing the necessary libraries
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

## Getting and parsing the URL content
# Getting the URL from user input
address = input('Enter URL: ')
# Reading the all content of the provided url as a single string
content = urllib.request.urlopen(address, context=ctx).read()    
# Convert the XML content into a tree    
tree = ET.fromstring(content)

## Finding the count tags and summing the content
# Find all tags named 'count'
lst = tree.findall('.//count')
# Sum the content of each count tag
total = 0 # initializing a variable
for element in lst:
    # For each element of the list of count tags, get the content, convert it into an integer
    # and sum it to the total
    total = int(element.text) + total
print(total)
