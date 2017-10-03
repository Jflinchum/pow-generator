import sys
import numpy

def levenshtein(word1, word2):
    d = numpy.zeros((len(word1)+1, len(word2)+1))

    for i in range(1, len(word1)+1):
        d[i, 0] = i

    for j in range(1, len(word2)+1):
        d[0, j] = j

    for j in range(1, len(word2)+1):
        for i in range(1, len(word1)+1):
            if word1[i-1] == word2[j-1]:
                cost = 0
            else:
                cost = 1
            d[i, j] = numpy.amin((d[i-1, j] + 1, d[i, j-1] + 1, d[i-1, j-1] + cost))
    return d[len(word1), len(word2)]


def main():
    subject = sys.argv[1]
    word2 = sys.argv[2]

    print(levenshtein(subject, word2))
    return


if __name__ == '__main__':
    main()
