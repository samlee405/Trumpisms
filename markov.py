import histogram
import tokenize
import histogram
import random

def getTokens():
    textFile = open('cleanedText.txt', 'r')
    cleanedText = textFile.read()
    textFile.close()

    return tokenize.tokenizeText(cleanedText)

def createMarkov(order):
    markovModel = {}
    tokens = getTokens()

    for index in range(0, len(tokens) - order):
        window = tuple(tokens[index : index + order])
        # add the word the comes after the previous set of words (window)
        if window in markovModel:
            markovModel[window].update([tokens[index + order]])
        else:
            markovModel[window] = histogram.Dictogram([tokens[index + order]])

    return markovModel

# need to implement tokenization method that denotes words that begin sentences.
def walkMarkov(markovModel, numOfWords):
    words = []

    startKey = random.choice(markovModel.keys())

    for index in range(numOfWords):


    print(start)

    return " ".join(words)

if __name__ == '__main__':
    markov = createMarkov(2)
    sentence = walkMarkov(markov, 10)
