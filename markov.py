# import specific functions instead of entire libraries
import histogram
import tokenize
import histogram
import random
import collections

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

# need to implement tokenization method that denotes words that begin & end sentences.
def walkMarkov(markovModel, numOfWords):
    words = []

    currentWindow = random.choice(markovModel.keys())

    # implement enqueue & dequeue
    # also maybe implement a system to not use number of words but instead a character count as to ascribe to tweet standards
    for index in range(numOfWords):
        currentWord = getNextWord(markovModel[currentWindow])
        words.append(currentWord)

        listToTuple = [currentWindow[1], currentWindow[2], currentWord] # needs to be dynamic (queue)
        currentWindow = tuple(listToTuple)
        # print(currentWindow)

    return " ".join(words)

def getNextWord(histogram):
    # Get total count of words
    wordCount = 0
    for key, value in histogram.iteritems():
        wordCount += value

    # Generate a random number from 1 - wordCount
    randomValue = random.randint(1, wordCount)

    # Iterate to find the chosen word
    sumTotal = 0
    for key, value in histogram.iteritems():
        sumTotal += value
        if randomValue <= sumTotal:
            return key

if __name__ == '__main__':
    markov = createMarkov(3)
    sentence = walkMarkov(markov, 10)
    print(sentence)
