from boardGenerator import *
import numpy as np
from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return("<h1>Go to /generate to get your sudoku boards</h1>")

@app.route("/generate",methods=["GET"])
def generateRoute():
    board = np.zeros((9,9),dtype=int)
    question,solution=generate(board.copy(),"hard")
    return jsonify({
        "question":question.tolist(),
        "solution":solution.tolist()
    })

if __name__ =="__main__":
    app.run()




