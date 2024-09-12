from text_utils import count_words
import math

file = open('sample.txt', 'r') # opens the txt file and assigns it to a variable: file
line_count = len(file.readlines()) # Puts all the lines onto a list and len counts them all
file.seek(0) # resets the read position to the beginning of the file
word_count = count_words(file.read()) # reading the file and using my count_words function to count the amount of words
avg = math.floor(word_count/line_count) # math.floor rounds down and it divides the amount of words by the amount of lines to get the average
file.close() # closes the file
print(f"Average words per line: {avg}") # uses an fstring to print "Average words per line:" and the average which is stored in the avg'

"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""