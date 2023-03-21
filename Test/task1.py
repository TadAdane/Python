import numpy as np
import matplotlib as plt

file_Galia = open('Galia.txt', 'r')
words = file_Galia.read()
line_of_words = words.splitlines()
# words_length = []
# words = []

for separate_words in line_of_words:
    number_words = len(words.split())
    number_signs = len(separate_words) #includes letters

    #Sign is including letters.
    print (line_of_words , "number of words: " , number_words , "numeber of signs: " , number_signs) #Only one line.

totalwords = sum(len(separate_words.split()))
totalsigns = sum(len(separate_words))
ave_wordsperline = totalwords / len(line_of_words)
ave_signsperword = totalsigns / totalwords

print("The average number of words/per line: " + str(ave_wordsperline))
print("The average number of signs/per word: " + str(ave_signsperword))
