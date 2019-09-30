"""
Program: textanalysis.py
Author: Ken
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
"""

# Take the inputs
# fileName = input("Enter the file name: ")
fileName = "eeny-meeny.txt"
inputFile = open(fileName, 'r')  # opening a file and assigning it to a fileobject of the name inputFile
textStr = inputFile.read()  # use the read method to read in all of the file's contents.
print(textStr)
# Count the sentences
no_sentences = textStr.count('.') + textStr.count('?') + \
               textStr.count(':') + textStr.count(';') + \
               textStr.count('!')

print("The text that we read in has %d sentences" % no_sentences)
print(textStr.split())
# # Count the words
lst_words = textStr.split()
no_words = len(lst_words)
print("The number of words in our text is: %d" % len(lst_words))
print("The character ',' appears %d times in the text." % textStr.count(","))
#
# Count the syllables
no_syllables = 0
vowels = "aeiouAEIOU"
for word in lst_words:
    for vowel in vowels:
        no_syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            no_syllables -= 1
    if word.endswith('le'):
        no_syllables += 1

print("The number of syllables in our text is: %d" % no_syllables)
# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (no_words / no_sentences) - \
        84.6 * (no_syllables / no_words)
print("The Flesch index is: %f" % index)
level = int(round(0.39 * (no_words / no_sentences) + 11.8 * \
                  (no_syllables / no_words) - 15.59))
print("The grade level is: %d" % level)

# # Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")

