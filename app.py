from boardGenerator import *
import numpy as np
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return render_template("selection.html")

@app.route("/generate",methods=["GET"])
def generateRoute():
    difficulty = request.args.get('difficulty', 'easy')
    board = np.zeros((9,9),dtype=int)
    question,solution=generate(board.copy(),difficulty=difficulty)
    return render_template('output.html', question=question.tolist(), solution=solution.tolist())

if __name__ =="__main__":
    app.run()




