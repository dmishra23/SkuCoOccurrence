from collections import Counter
from nltk import FreqDist, word_tokenize
from nltk.util import ngrams

import sys
import re

# Function get_ngrams takes the input text and results ngram tokens
# Definiton | Function Param : text refers to the original sentence to be tokenized in ngrams (bigrams, trigrams, ...)
# Defintion | Function Param : n refers to the number of tokens in the ngram (n=2 means bigram, n=3 means trigram , ...)
def get_ngrams(text, n ):
    n_grams = ngrams(word_tokenize(text), n)
    return [ ' '.join(grams) for grams in n_grams]


# Function filter_counter takes the input list of ngrams with their occurrence freq from all lines in the file
# Definiton | Function Param : xlist refers to counter list of ngrams with their occurrence frequencies in the file
# Defintion | Function Param : minThreshold refers to co-occurrence frequency threshold provided to script param
# Defintion | Function Param : outputFile refers to the output file with expected results
def filter_counter(xlist,minThreshold,outputFile):
    f = open(outputFile, 'w')
    for key, cnts in list(xlist.items()):  # list is important here
        # print str(cnts) + " : " + key

        if int(cnts) >= int(minThreshold):
            # print str(cnts) + "|" + str(minThreshold)
            skus = len(word_tokenize(key))
            print >> f, str(skus) + "," + str(cnts) + "," + re.sub(" ",",",key)

    f.close()

# Function filter_counter takes the input list of ngrams with their occurrence freq from all lines in the file
# Definiton | Function Param : inputFile refers to the input file passed to the script
# Definiton | Function Param : minSetSize
# Definiton | Function Param : minThreshold
# Definiton | Function Param : outputFile refers to the output file with expected results
def getSkuFreq(inputFile,minSetSize,minThreshold,outputFile):
    with open(inputFile) as f:
        i = 0
        valid = 0

        #Setup Counter for co-occurring tokens
        x = Counter()
        for line in f:
            tokenize = word_tokenize(line)
            words = len(tokenize)
            if words >= minSetSize:
                maxSetSize = words
                # print "Row [" + str(i) + "] | MinSetSize : " +str(minSetSize) + " | MaxSetSize : " + str(words)
                for n in range(minSetSize,maxSetSize):
                    # print str(n) + "-gram"
                    # print get_ngrams(line,n)
                    # print "_______________________________"
                    x.update(get_ngrams(line,n))
                    # print x
                    # print "_______________________________"
                valid+=1
            i+=1

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

