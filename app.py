from flask import Flask
import markov
import os

app = Flask(__name__)

@app.route('/')
def getWord():
    markov = markov.createMarkov(3)
    sentence = markov.walkMarkov(markov, 10)

    return sentence

@app.route('/<num>')
def getSentence(num):
    # sentence = ""
    # for _ in range(int(num)):
    #     sentence += sample.sample() + " "
    #
    # return sentence.strip()

if (__name__) == ('__main__'):
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host = '0.0.0.0', port=port)
