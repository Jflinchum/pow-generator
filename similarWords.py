import sys
from levenshtein import levenshtein


def main():
    subject = sys.argv[1]
    dictionary = open("/usr/share/dict/web2")
    levenNumber = 2
    
    similar = []

    for line in dictionary:
        line = line.split("\n")[0]
        if subject != line and subject[0] == line[0] and levenshtein(subject, line) <= levenNumber:
            similar.append(line)

    print(similar)

if __name__ == '__main__':
    main()
