# PyBoss Exercise for UCB Extension Data Science Bootcamp, HW3
# Written by A. Lam

# Notes: Input format: Emp ID, Name, DOB, SSN, State
# Output format: Emp Id, First Name, Last Name, DOB, SSN, State
# split Name into First and Last Name
# Reformat DOB from yyyy-mm-dd to mm/dd/yyyy
# Print SSN as ***-**-xxxx
# Change State from full name to abbreviation

# Modules
import os
import csv

import state_abbreviations as SA #dictionary of statenames to abbreviations.
# https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5

# Prompt for filename
# sourceFile = input('Please input the source filename and extension: ')
sourceDir = 'raw_data'
sourceFile = 'employee_data2.csv'
filePath = os.path.join(sourceDir,sourceFile)

# Create templates for output
templateOut = '{},{},{},{},{},{}'
templateDOB = '{}/{}/{}' # format as mm/dd/yyyy
templateSSN = '***-**-{}' # retain last 4 digits
outputText = []

# Insert Headers into outputText
outputText.append(templateOut.format('Emp ID','First Name','Last Name','DOB','SSN','State'))

# open file and extract data
with open(filePath,'r',newline='') as fileData:
    rawData = csv.reader(fileData,delimiter=',')
    next(rawData,'None') #Skip Headers
    for row in rawData:
        #print(row)
        empID = row[0]
        names = row[1].split(' ')
        DOB = row[2].split('-')
        SSN = row[3].split('-')
        State = row[4]
        outDOB = templateDOB.format(DOB[1],DOB[2],DOB[0])
        outSSN = templateSSN.format(SSN[2])
        outputText.append(templateOut.format(
            empID,names[0],names[1],outDOB,outSSN,SA.us_state_abbrev[State]
            ))


#for k,v in SA.us_state_abbrev.items():
    #print(k + ': ' + v)
    
# printing output to terminal and file
outputName = input('Please name analysis file: \n')
fileOutput = outputName + '.txt'
with open(fileOutput,'w') as fileOut:
    for line in outputText:
        #print(line)
        fileOut.write(line + '\n')

outputText.append('\n \n \nSource file: ' + filePath)
