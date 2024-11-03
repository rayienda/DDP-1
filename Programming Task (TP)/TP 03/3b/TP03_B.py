'''
PA 03
Rayienda Hasmaradana
'''

# Imports
from htmlFunctions import * # Importing necessary functions from the htmlFunctions
from string import punctuation #
from operator import itemgetter

# Start of the program
print("""
Program to create word cloud from a text file
---------------------------------------------
The result is stored as an HTML file,
which can be displayed in a web browser.
""")

# Open the file
stop_words_file = "stopWords.txt" # File with list of words that won't be counted
stop_words = open(stop_words_file, "r").read().split("\n") # Open, read, and split the words in the file stopWords.txt

file_name = input("Please enter the file name: ")  # Prompt user to input the name of the file to open
print()

try:
    with open(file_name, "r") as open_speech:  # If the input is correct, open the file
        file_contents = open_speech.read()  # Read the entire contents of the file
        print(f"{file_name}: ")

except FileNotFoundError:  # If the inputted file name is not in the folder, print error and quit the program
    print(f"The file {file_name} can not be found.")
    quit()

# Join lines in the file contents and split into a list of words
paragraph = " ".join(line.strip() for line in file_contents.split('\n'))

unorganized_paragraph_list = paragraph.split(" ")  # Make the paragraph a word by word list
paragraph_list = []  # Empty list to store the words

for words in unorganized_paragraph_list:  # Iterate through each word
    words = words.lower()  # Make the word lowercase
    for punc in punctuation:  # Iterate through the punctuation character
        if punc in words:  # If the selected punctuation is in the word, strip it from the string
            words = words.replace(punc, "")

    if words not in stop_words:  # Check if the word is a stop word
        paragraph_list.append(words)  # If it's not a stop word, append it to the list

# Initialize a dictionary to store word frequencies
word_dict = {}  # Dictionary to store word frequencies

# Iterate through each word in the paragraph (excluding stop words)
for word in paragraph_list:
    word_dict[word] = word_dict.get(word, 0) + 1 # Update the word frequency in the dictionary

# Convert counted data into a list and sort it
sorted_word_list = sorted(word_dict.items(), key=itemgetter(1, 0), reverse=True)
top_60_words = sorted_word_list[:60]

print("60 words in frequency order as (count:word) pairs \n") # Display the top 60 words in frequency order

for i, (word, count) in enumerate(top_60_words):
    print(f"{count:>2}:{word:20s}", end="")
    if (i + 1) % 3 == 0:  # Print newline every 3 words
        print()

# get the words with the highest and lowest frequency
low_word_count = top_60_words[-1][1]  # Get the word which has the lowest amount of repetition
high_word_count = top_60_words[0][1]  # Get the word which has the highest amount of repetition
top_60_abc = sorted(top_60_words, key=itemgetter(0))  # Sort the top 60 words alphabetically

# HTML Generator
html_body = ""  # Empty string for storing the body of the HTML file
for word, count in top_60_abc:
    html_body += make_HTML_word(word, count, high_word_count, low_word_count) + " "  # Use the HTML functions to insert formatted words

html_box = make_HTML_box(html_body)  # Make a box out as a canvas of the words
print_HTML_file(html_box, f"A Word Cloud of {file_name}")  # Make the HTML file

# Print for the end of the program
print()
input("Please type Enter to exit ...")

# THE END