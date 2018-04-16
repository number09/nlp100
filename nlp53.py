import re


def main():

    with open('nlp.txt.xml', 'r') as infile:
        for line in infile:
            print_word(line)


def print_word(line):
    r_word = re.compile(r'<word>(.*)</word>')

    w = r_word.search(line)
    if w:
        print(w.group(1))


if __name__ == '__main__':
    main()
