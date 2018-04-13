import json
import re


def main():

    with open('nlp.txt', 'r') as infile:
        for line in infile:
            split_pattern(line)

def split_pattern(str):

    reg_sep = re.compile(r'[.;:?!] (?:[A-Z])')

    i = reg_sep.search(str)
    if i is not None:
        print(str[:i.start()])
        split_pattern(str[i.end()-1:])
    else:
        print(str)


if __name__ == '__main__':
    main()
