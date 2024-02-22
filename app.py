from boardGenerator import *
import numpy as np
from flask import Flask,Response

app=Flask(__name__)
import json

app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return("<h1>Go to /generate to get your sudoku boards</h1>")

@app.route("/generate",methods=["GET"])
def generateRoute():
    board = np.zeros((9,9),dtype=int)
    question,solution=generate(board.copy(),"hard")
    jsonData = {
        "question":question.tolist(),
        "solution":solution.tolist()
    }
    jsonData = json.dumps(jsonData,indent=4)
    return Response(jsonData,status=200,mimetype="application/json")

if __name__ =="__main__":
    app.run()




