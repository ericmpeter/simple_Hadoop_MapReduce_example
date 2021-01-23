#!/usr/bin/env python
import sys
from sklearn.feature_extraction import stop_words
stops = set(stop_words.ENGLISH_STOP_WORDS)


# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    #change everything to lowercase
    line = line.strip().lower()
    
    # split the line into words; splits on any whitespace
    words = line.split()
    
    # remove stopwords, output tuples (word, 1) in tab-delimited format
    for word in words:
        table = string.maketrans("","")
        word1 = word.translate(table, string.punctuation)
        if word1 not in stops:
            print '%s\t%s' % (word1, "1")
