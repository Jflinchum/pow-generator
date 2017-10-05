import sys
from phonetics import metaphone

def findPhoneticIndex(subject, word):
    subjectPhone = metaphone(subject)

    for i in range(0, len(word)):
        wordPhone = metaphone(word[i:len(word)])
        if subjectPhone == wordPhone[0:len(subjectPhone)]:
            return i

def main():
    subject = sys.argv[1]
    word = sys.argv[2]
    
    print(findPhoneticIndex(subject, word))


if __name__ == "__main__":
    main()
