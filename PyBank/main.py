# PyBank Exercise for UCB Extension Data Science Bootcamp, HW3
# Written by A. Lam

# Modules
import os
import csv

# Prompt for filename
# sourceFile = input('Please input the source filename and extension: ')
sourceDir = 'raw_data'
sourceFile = 'budget_data_2.csv'
filePath = os.path.join(sourceDir,sourceFile)

# initialize values for file data
nMonths = 0 
totalRevenue = 0
hiMonth = ''
loMonth = ''
hiRevenue = 0
loRevenue = 0
differences = []
prevRevenue = 0

# average solver
def average(arg):
    total = 0
    for item in arg:
        total += item
    return (total/len(arg))

# open file and extract data
with open(filePath,'r',newline='') as fileData:
    rawData = csv.reader(fileData,delimiter=',')
    next(rawData,'None') #Skip Headers
    for row in rawData:
        # print(row)
        totalRevenue += int(row[1])
        nMonths += 1 #assumes each row in the file is a unique month
        differences.append(int(row[1]) - prevRevenue)
        prevRevenue = int(row[1]) 
        if int(row[1]) > hiRevenue:
            hiRevenue = int(row[1])
            hiMonth = row[0]
        if int(row[1]) < loRevenue:
            loRevenue = int(row[1])
            loMonth = row[0]
# cleanup of differences
differences = differences[1:]



# template of output
outputText = []
outputText.append('Financial Analysis')
outputText.append('---------------------------------')
outputText.append('Total Months: ' + str(nMonths))
outputText.append('Total Revenue: $' + str(totalRevenue//nMonths))
outputText.append('Average Revenue Change: $' + str(round(average(differences),2)))
outputText.append('Greatest Increase in Revenue: ' + hiMonth + ' ($' + str(hiRevenue) + ')') 
outputText.append('Greatest Decrease in Revenue: ' + loMonth + ' ($' + str(loRevenue) + ')')
outputText.append('\n \n \nSource file: ' + filePath)


# print to terminal
outputName = input('Please name analysis file: \n')
fileOutput = outputName + '.txt'
with open(fileOutput,'w') as fileOut:
    for line in outputText:
        print(line)
        fileOut.write(line + '\n')