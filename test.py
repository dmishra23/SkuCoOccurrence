from collections import Counter
import itertools

import sys
import re

# Function get_combinations takes the input text line and set size
# Definiton | Function Param : text refers to the line containing set of skus
# Defintion | Function Param : n refers to set size
def get_combinations(text,n):
    # print "F: get_combinations"
    linelist = sorted(text.split(' '))
    return [entry for entry in itertools.combinations(linelist, n)]

# Function filter_counter takes the input list of ngrams with their occurrence freq from all lines in the file
# Definiton | Function Param : xlist refers to counter list of ngrams with their occurrence frequencies in the file
# Defintion | Function Param : minThreshold refers to co-occurrence frequency threshold provided to script param
# Defintion | Function Param : outputFile refers to the output file with expected results
def filter_counter(xlist,minThreshold,outputFile):
    # print "F: filter_counter"
    f = open(outputFile, 'w')
    for key, cnts in list(xlist.items()):  # list is important here
        if int(cnts) >= int(minThreshold):
            skus = len(key)
            # print str(skus) + "," + str(cnts) + "," + ','.join(key)
            print >> f, str(skus) + "," + str(cnts) + "," + ','.join(key)

    f.close()

# Function filter_counter takes the input list of ngrams with their occurrence freq from all lines in the file
# Definiton | Function Param : inputFile refers to the input file passed to the script
# Definiton | Function Param : minSetSize
# Definiton | Function Param : minThreshold
# Definiton | Function Param : outputFile refers to the output file with expected results
def getSkuFreq(inputFile,minSetSize,minThreshold,outputFile):
    # print "F: getSkuFreq"
    with open(inputFile) as f:
        #Setup Counter for co-occurring tokens
        x = Counter()
        i = 1
        for line in f:
            print "Processing : [" + str(i) + "]"
            line = line.rstrip()
            tokens = line.split(' ')
            print "========================================================"
            print tokens
            maxSetSize = len(tokens)
            print "minSetSize : " + str(minSetSize) + "| maxSetSize : " + str(maxSetSize)
            if maxSetSize >= minSetSize:
                count = minSetSize
                # Loop through all possible set sizes starting with minimum set size
                while (count <= maxSetSize):
                    # Update counter for SKU combination
                    print "minSetSize : " + str(minSetSize) + "| maxSetSize : " + str(maxSetSize) + " | Add set size : " + str(count)
                    x.update(get_combinations(line, count))
                    count += 1
            else:
                print "SKIP | Line : " + line
        i += 1
        # print x
        filter_counter(x,minThreshold,outputFile)

# Input parameters : <filename> <sigma>
# <filename> : Input filename containing transaction log
# <sigma> : co-occurrence frequency in the input filename
inputFile = sys.argv[1]
sigma = sys.argv[2]
print "Input File : " + inputFile
print "Co-Occurrence Freq. : " + sigma

# Script Variable
minItemSetSize=3
outputFile = inputFile.split('.')[0] + "_" + str(sigma) + ".out"
print "Output File : " + outputFile
getSkuFreq(inputFile,minItemSetSize,sigma,outputFile)