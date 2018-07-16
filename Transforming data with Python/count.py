""" This script looks for words appear most often in the headlines 
"""
import read
from collections import Counter

data = read.load_data()

#Makes sure all elemnts in data['headline'] are strings
data['headline'] = data['headline'].astype(str)

#This moves the elements in data['headline'] to a list 
string_lists = data['headline']

#This then joins the strings to make one long string
long_string = " ".join(string_lists)

#This makes all the elementsin the string lowercase
long_string = long_string.casefold()

#This splits the long string into individual words
words = long_string.split(' ')

#This counts the 100 words that occur the most in the data
word_count = Counter(words).most_common(100)

print(word_count)