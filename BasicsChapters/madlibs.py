# Mad Libs program from Ch. 9

import re

# Open the file and pull in the sentence
sentenceFile = open('C:\\Users\\aschon1\\Documents\\madlibs.txt')
sentence = sentenceFile.read()
sentenceFile.close()

# Find the words we'll be replacing
wordsFound = re.findall('ADJECTIVE|NOUN|VERB|ADVERB', sentence)
replacements = []

# Ask the user what words they want to insert
for i in range(len(wordsFound)):
    replacements.append(input("Please enter your %s: " % (wordsFound[i])))

# Make the replacements
for i in range(len(wordsFound)):
    findWord = re.compile(wordsFound[i])
    sentence = findWord.sub(replacements[i], sentence, count=1)

# Print our new sentence
print(sentence)

# Reopen the file and write our new sentence
sentenceFile = open('C:\\Users\\aschon1\\Documents\\new_madlibs.txt', 'w')
sentenceFile.write(sentence)
sentenceFile.close()
