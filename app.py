from flask import Flask
import sample
import os

app = Flask(__name__)

@app.route('/')
def getWord():
    return sample.sample()

@app.route('/<num>')
def getSentence(num):
    sentence = ""
    for _ in range(int(num)):
        sentence += sample.sample() + " "
        
    return sentence.strip()

if (__name__) == ('__main__'):
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host = '0.0.0.0', port=port)
