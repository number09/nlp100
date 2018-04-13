import json
import re


def main():

    with open('nlp.txt', 'r') as infile:
        for line in infile:
            split_pattern(line)

def split_pattern(word):

    reg_sep = re.compile(r'[.;:?!] (?:[A-Z])')

    i = reg_sep.search(word)
    if i is not None:
        #print(word[:i.start()])
        split_words(word[:i.start()])
        split_pattern(word[i.end()-1:])
    else:
        if word.strip():
            #print(word)
            split_words(word)

def split_words(sentence):

    words = sentence.split(' ')
    for w in words:
        print(w)


if __name__ == '__main__':
    main()
