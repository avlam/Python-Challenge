# PyParagraph Exercise for UCB Extension Data Science Bootcamp, HW3
# Written by A. Lam

## Modules
import os
import csv
import re # for sentence splitting over multiple punctuation signs
import string # for complete punctuation list

# Prompt for filename
# sourceFile = input('Please input the source filename and extension: ')
sourceDir = 'raw_data'
sourceFile = 'paragraph_2.txt'
filePath = os.path.join(sourceDir,sourceFile)

# Initialize metrics
nSentences = [] # per paragraph
nWords = [] # per Sentence
nLetters = [] # per Word

# Create a mean function so as not to need numpy
def mean(arg):
    # assumes a list of numeric values in
    total = 0
    for item in arg:
        total += item
    average = total/len(arg)
    return average

# open file and extract data
with open(filePath,'r',newline='') as fileData:
    rawData = csv.reader(fileData,delimiter='\n')
    for text in rawData:
        for paragraph in text: #In the event multiple paragraphs are passed in a single file
            lines = re.split('(?<=[.!?]) +', paragraph)
            nSentences.append(len(lines))
            for sentence in lines:
                # print(sentence)
                words = sentence.split(' ')
                for word in words:
                    # trim punctuation off of the beginning or end of words
                    if word[-1] in string.punctuation:
                        word = word[:-1]
                    if word[0] in string.punctuation:
                        word = word[1:]   
                    # print(word)
                    nLetters.append(len(word))
                nWords.append(len(words))

# Generate Output  
outputText = [
    'Paragraph Analysis',
    '--------------------------------',
    'Approximate Word Count: ' + str(len(nLetters)),
    'Approximate Sentence Count: ' + str(len(nWords)),
    'Average Letter Count: ' + str(mean(nLetters)),
    'Average Sentence Length: ' + str(mean(nWords)),
    '\n\n\nData Sourcefile: ' + filePath
]

# Print to file and terminal
outputName = input('Please name analysis file: \n')
fileOutput = outputName + '.txt'
with open(fileOutput,'w') as fileOut:
    for line in outputText:
        print(line)
        fileOut.write(line + '\n')
