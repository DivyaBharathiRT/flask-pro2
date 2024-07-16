#import flask
from  flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<div style='background:pink'><h1>DOGS LIFE:</h1><p>The dog is a pet animal. A dog has sharp teeth so that it can eat flesh very easily, it has four legs, two ears, two eyes, a tail, a mouth, and a nose. It is a very clever animal and is very useful in catching thieves. It runs very fast, barks loudly and attacks the strangers. A dog saves the life of the master from danger. One can find dogs everywhere in the world. Dogs are a very faithful animal. It has a sharp mind and a strong sense of hearing smelling the things. It also has many qualities like swimming in the water, jumping from anywhere, good smelling sense.A dog has a strong power of smell. They are more liked by people because of their faithfulness. They are intelligent, they are watchfulness. The dogs have many colors such as grey, white, black, brown and red. They are of many kinds such as bloodhound, greyhound, german shepherd, Labrador, Rottweiler, bulldog poodle, etc</p></div>"
if __name__=='__main__':
    app.run(debug=True)
