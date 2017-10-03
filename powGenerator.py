from findSentence import sentenceGrab
from phoneticWords import findPhonetics
from random import randint
from math import floor
import sys


def main():
    subject = sys.argv[1]
    library = sys.argv[2]

    phonetics = findPhonetics(subject, "/usr/share/dict/web2") 
    #nearPhoneticNum = phonetics[0][1]
    #nearestPhonetics = [i for i in phonetics if i[1] == nearPhoneticNum]

    sentences = []
    tries = 10
    index = 0
    while len(sentences) == 0 and index <= tries:
        index += 1
        punWord = phonetics[randint(0, floor(len(phonetics)/2))][0]
        print(punWord)
        sentences = sentenceGrab(punWord, library, True)
        if len(sentences) == 0:
            phonetics = [i for i in phonetics if i[0] != punWord]
            print("Could not find sentence... Trying again")

    if len(sentences) == 0:
        print("Reached maximum tries. Ending")
        return

    punSentence = sentences[randint(0, floor(len(sentences)/2))]

    punIndex = punSentence.find(punWord)
    punSentence = punSentence[0:punIndex] + subject + punSentence[punIndex+len(subject):len(punSentence)]
    
    print(punSentence)

if __name__ == "__main__":
    main()
