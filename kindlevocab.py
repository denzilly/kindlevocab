import csv


#in order to make this package work
#you need to go to python console and:
# 1 . import nltk
# 2 . nltk.download('wordnet')
from nltk.corpus import wordnet

wordlist = []

#read the wordlist from CSV
#Words is just a list of words, one per row.
with open('WORDS.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        wordlist.append(str(row))

csv_file.close()

#alphabetise wordlist
wordlist.sort()

#print(wordlist)


def define(word):
    print(word)
    word = word.split('\'')[1]
    print(word)
    test = wordnet.synsets(word)
    print(test)
    try:
        definition = test[0].definition()
        definition = definition[0].upper() + definition[1:]
    except:
        definition = "Probably a Dutch word, no support yet."
    return word, definition




f = open("definitions.md", "w+")

f.write("## Kindle Vocabulary List\n")
f.write("| Word   | Definition     |\n")
f.write("| :------------- | :------------- |\n")
for x in range(1,len(wordlist)):

    output = define(wordlist[x])

    f.write("|")
    f.write(output[0])
    f.write("|")
    f.write(output[1])
    f.write("|\n")
