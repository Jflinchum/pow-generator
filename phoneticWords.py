import sys
from phoneticIndex import findPhoneticIndex
from levenshtein import levenshtein
from phonetics import metaphone

def findPhonetics(subject, bookshelf):
    dictionary = open(bookshelf)
    try: 
        subPhonetic = metaphone(subject)
    except TypeError:
        print("Soundex broke")
        return

    levenNumber = 0  
    similar = []

    for line in dictionary:
        if "-" not in line:
            line = line.split("\n")[0]
            try:
                linePhonetic = metaphone(line)
                if line != subject and linePhonetic.find(subPhonetic) != -1:
                    subjectIndex = findPhoneticIndex(subject, line) 
                    similar.append((line, levenshtein(line[subjectIndex:subjectIndex+len(subject)], subject)))

            except TypeError: 
                #print("Broke on " + line + "... Continuing")
                continue
    
    similar.sort(key=lambda tup: tup[1])
    return similar

def main():
    subject = sys.argv[1]
    bookshelf = sys.argv[2]
    similar = findPhonetics(subject, bookshelf)
    print(similar)

if __name__ == '__main__':
    main()
