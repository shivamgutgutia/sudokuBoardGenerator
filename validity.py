from boardGenerator import *
import numpy as np

count=[0]
board=np.zeros((9,9))
#board=np.array([[1,6,5,0,2,0,8,0,0],[3,2,0,7,0,8,4,1,0],[7,0,0,6,0,1,2,3,5],[2,0,0,0,8,0,0,0,7],[0,9,0,0,7,0,3,8,4],[6,8,0,3,0,9,5,0,0],[9,0,6,8,1,0,0,4,0],[0,1,2,0,3,7,0,0,0],[8,7,0,0,6,4,0,9,2]])
countSolve(board,count)
print(count)