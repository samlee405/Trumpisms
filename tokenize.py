import re

def tokenizeText(text):
    # add start and end
    cleanedText = lowerCase(text)
    cleanedText = removePunctuation(cleanedText)
    tokens = splitOnWhitespace(cleanedText)

    return tokens

def lowerCase(text):
    return text.lower()

def splitOnWhitespace(text):
    return re.split('\s+', text)

def removePunctuation(text):
    cleanedText = re.sub('[,.()]', '', text)
    cleanedText = re.sub('( \'| \"|\' |\" )', '', cleanedText)
    cleanedText = re.sub('--', ' ', cleanedText)

    return cleanedText

if __name__ == '__main__':
    textFile = open('cleanedText.txt', 'r')
    cleanedText = textFile.read()
    textFile.close()

    tokens = tokenizeText(cleanedText)
    print(tokens)
