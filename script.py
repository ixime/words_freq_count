#!/usr/bin/env python3
# Usage
# ./script.py <txt file>
# output: <txt filename>_freq_count.csv

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
import sys
import os


nltk.download("stopwords")
filename = sys.argv[1]

# open file
with open(filename) as f:
    lines_list = f.read().splitlines()

# separate text into words
tokenizer = nltk.tokenize.RegexpTokenizer("\w+")
tokens_list = []
for line in lines_list:
    tokens_list += tokenizer.tokenize(line)

# convert upper letters into lower letters
words = []
for word in tokens_list:
    words.append(word.lower())
    
# get rid of words that are not important 
sw = stopwords.words("english")
words_ns = []
for word in words:
    if word not in sw:
        words_ns.append(word)

# do lemmatitaion
stemmer = PorterStemmer()
words_ns_st = []
for word in words_ns:
    words_ns_st.append(stemmer.stem(word))

# count word stems
words_dict = {}
for word in words_ns_st:
    if word in words_dict.keys():
        words_dict[word] += 1
    else:
        words_dict[word] = 1
        
# prepare lines for csv file
ordered_counts_list = [k + ", " + str(v) for k, v in sorted(words_dict.items(), key=lambda item: item[1])][::-1]

# write csv file
with open(os.path.splitext(filename)[0] + "_freq_count.csv", "w") as f:
    f.write("word_stem, count\n")
    for line in ordered_counts_list:
        f.write(line)
        f.write("\n")
