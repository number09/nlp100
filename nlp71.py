import sys

stop_words = {
    'I', 'a', 'about', 'an', 'are', 'as', 'at', 'be', 'by', 'com', 'for', 'from', 'how',
    'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the', 'this', 'to', 'was', 'what', 'when',
    'where', 'who', 'will', 'with', 'the', 'www'
}


def check_word(arg):

    if arg in stop_words:
        return True
    else:
        return False


if __name__ == '__main__':
    check_word(sys.argv[1])
