# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
string_magic = 'abracadabra'
print(string_magic[5])
print(string_magic[-2])
print(string_magic.find('c'))

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[7:10])
print(alphabet[0:12:2])
print(alphabet[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote[-15:])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
text = "Python is fun. Fun is good. Good is subjective."
print(text[36:46])
print(text[::3])
print(text[::-1])


# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
star_wars = "MAY THE FORCE BE WITH YOU."
print(star_wars.replace("MAY THE FORCE BE WITH YOU." , "may the force be with you."))

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
motto = ["Make", "haste", "slowly."]
joined_sentence = " ".join(motto)
print(joined_sentence)
print(joined_sentence.split("a"))

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
sentence = "Life is what happens when you are busy making other plans."
modified_sentence = sentence.replace("busy","distracted").replace("plans","mistakes")
print(modified_sentence)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
word4 = "Iteration" * 7
print(word4)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quote_two = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print(quote.find("moonlight"))

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.
word1 = len("Supercalifragilisticexpialidocious")
print(word1)
