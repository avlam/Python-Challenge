# PyBoss Exercise for UCB Extension Data Science Bootcamp, HW3
# Written by A. Lam

# Modules
import os
import csv

# Prompt for filename
# sourceFile = input('Please input the source filename and extension: ')
sourceDir = 'raw_data'
sourceFile = 'election_data_2.csv'
filePath = os.path.join(sourceDir,sourceFile)

# open file and extract data
# Note: format is in  Voter ID, County, Candidate

# Initialize variables to track
voters = []
candidates = {}
nVotes = 0
duplicateVotes = []

with open(filePath,'r',newline='') as fileData:
    rawData = csv.reader(fileData,delimiter=',')
    next(rawData,'None') #Skip Headers
    for row in rawData:
        # print(row)
        # if row[0] not in voters:
            #voters.append(row[0])
            if row[2] not in candidates.keys():
                candidates[row[2]] = 1
            else:
                candidates[row[2]] += 1
            nVotes += 1
        #else:
            #duplicateVotes.append(row[0])

# calculate the winner
winner = max(candidates, key=candidates.get)

# Create output string
lineBreak = '--------------------------------------'
outputText = []
outputText.append('Election Results')
outputText.append(lineBreak)
outputText.append('Total Votes: ' + str(nVotes))
outputText.append(lineBreak)
for k,v in candidates.items():
    outputText.append(k + ': ' + str(round((100*v/nVotes),2)) + '% (' + str(v) + ')')
outputText.append(lineBreak)
outputText.append('Winner: ' + winner)
outputText.append(lineBreak)
outputText.append('\n\n\nSource file: ' + filePath)

# print to terminal and text file
outputName = input('Please name analysis file: \n')
fileOutput = outputName + '.txt'
with open(fileOutput,'w') as fileOut:
    for line in outputText:
        print(line)
        fileOut.write(line + '\n')


