import sys
import os
from random import shuffle
import re

def sentenceGrab(subject, directory, firstOccurence):
    bookshelf = os.listdir(directory)
    sentences = []

    for file in bookshelf:
        if (file.endswith(".txt")):
            with open(os.path.join(directory, file), "r") as f:
                text = f.read()
                re.sub(r'(M\w{1,2})\.', r'\1', text) # Get rid of Mr./Mrs.
                sentenceList = re.split(r' *[\.\?!][\'"\)\]]* *', text) # Split into sentences
                for sentence in sentenceList:
                    wordList = sentence.split()
                    for word in wordList:
                        if subject.lower() == word.strip().lower():
                            sentences.append(sentence.strip())
                            if firstOccurence:
                                return sentences
    return sentences
                    

def main():
    subject = sys.argv[1]
    bookDirectory = sys.argv[2]
    sentences = sentenceGrab(subject, bookDirectory)
    print(sentences)

if __name__ == '__main__':
    main()
