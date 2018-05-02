import random


def main():

    sentiment = []

    with open('rt-polarity.neg', 'r', encoding='iso-8859-1') as neg:
        for nline in neg:
            sentiment.append('-1 ' + nline.strip() + '\n')

    with open('rt-polarity.pos', 'r', encoding='iso-8859-1') as pos:
        for pline in pos:
            sentiment.append('+1 ' + pline.strip() + '\n')

    with open('sentiment.txt', 'w') as file:
        file.writelines(random.sample(sentiment, len(sentiment)))


if __name__ == '__main__':
    main()
