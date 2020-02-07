from cs50 import get_string

# get string input
text = get_string("Text: ")

# count letters
letters = 0

# count sentences
sentences = text.count(".") + text.count("!") + text.count("?")

# count words
words = len(text.split())

# iterate over text
for i in range(len(text)):
    if text[i].isalpha():
        letters +=1

# where L is the average number of letters per 100 words
L = letters / words * 100

# where S is the average number of sentences per 100 words
S = sentences / words * 100

# plug in figures into Coleman-liaux index
index = 0.0588 * L - 0.296 * S - 15.8

# print index as an whole number
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade", int(round(index)))