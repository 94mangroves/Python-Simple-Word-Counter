# The purpose of this script is to count the occurrences of a word within a text document
# Make sure the text file is in the same folder as this script
#
# Note: the best way I found for this to work is by:
# First, downloading Python in Ubuntu https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
# Second, downloading and installing Wing IDE in Ubuntu https://wingware.com/doc/install/linux-installation-detail
# Third, install PIP on Ubuntu https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/
# Fourth, downloading and installing PrettyTables in Ubuntu https://pypi.org/project/prettytable/
#
# 


# This imports RegEx just in case we don't know the format the user choses and PrettyTable so the results are 

import re
from prettytable import PrettyTable

# This asks the user for their file

logFile = input("Please enter name of file to be analyzed: ")

# This function takes in the file the user picked 

def worm_word_finder(word):
    with open(logFile) as f:
        data = f.read()
        items = re.findall(word, data)
    return len(items)

# This outputs the search results based on the file the user picked and the word they chose to search for

word = input("\n" 'Enter the word you wish to search for: ')

count = worm_word_finder(word)

# print("\n"'The word {} has been found {} times'.format(word, count))

print(' ')

# Create table
table = PrettyTable(['word','count'])
for x in range(0,1):
    table.add_row([word,count])
print(table)