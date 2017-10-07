from findSentence import sentenceGrab
from phoneticWords import findPhonetics
from phoneticIndex import findPhoneticIndex
from random import randint
from math import floor
import sys


def main():
    library = sys.argv[1]
    subject = sys.argv[2]
    dictionary = "/usr/share/dict/words"

    phonetics = findPhonetics(subject, dictionary)
    nearPhoneticNum = floor((phonetics[0][1] + phonetics[len(phonetics)-1][1]) / 2)
    phonetics = [i for i in phonetics if i[1] <= nearPhoneticNum]

    sentences = []
    tries = 10
    index = 0
    while len(sentences) == 0 and index <= tries:
        if len(phonetics) == 0:
            print("No more phonetic words. Ending")
            return
        index += 1
        punWord = phonetics[randint(0, floor(len(phonetics)/2))][0]
        print(punWord)
        sentences = sentenceGrab(punWord, library, True)
        if len(sentences) == 0:
            phonetics = [i for i in phonetics if i[0] != punWord]
            print("Could not find sentence... Trying again")

    if index >= tries:
        print("Reached maximum tries. Ending")
        return

    punSentence = sentences[randint(0, len(sentences) - 1)]

    sentenceIndex = punSentence.find(punWord)
    punIndex = findPhoneticIndex(subject, punWord)
    punSentence = punSentence[0:sentenceIndex + punIndex] + subject + punSentence[sentenceIndex + punIndex + len(subject):len(punSentence)]
    
    print(punSentence)

if __name__ == "__main__":
    main()
