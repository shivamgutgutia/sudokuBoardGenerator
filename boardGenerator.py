import numpy as np


def fillDiagonal(board):
    def generateDiagonal():
        arr=np.arange(1,10)
        for i in range(3):
            np.random.shuffle(arr)
            yield arr.reshape((3,3))

    out=generateDiagonal()
    board[:3,:3]=next(out)
    board[3:6,3:6]=next(out)
    board[6:,6:]=next(out)
    return(board)

def isValid(num,row,col,board):

        #row check
        rowCheck = num in board[row,:]

        #column check
        columnCheck = num in board[:,col]

        #subgrid check
        subgridCheck = num in board[3*(row//3):3*((row//3)+1),3*(col//3):3*((col//3)+1)]

        if rowCheck or columnCheck or subgridCheck:
            return False
        return True

def emptyCell(board):
        for i in range(9):
            for j in range(9):
                if board[i,j]==0:
                    return i,j
                
        return None

def solve(board):
    location=emptyCell(board)
    if not location:
        return True
    row,col=location

    count=0
    for num in range(1,10):
        if(isValid(num,row,col,board)):
            board[row,col]=num
            if solve(board):
                return True
            else:
                board[row,col]=0

    return False

def countSolve(board,count):
    location=emptyCell(board)
    if not location:
        count[0]+=1
        return
    row,col=location
    for num in range(1,10):
        if(isValid(num,row,col,board)):
            board[row,col]=num
            if countSolve(board,count):
                return True
            else:
                board[row,col]=0
    
      

def generateQuestion(solution,difficulty,count):
    if difficulty == "easy":
        n= np.random.randint(36,39)
    elif difficulty == "medium":
        n = np.random.randint(39,42)
    else:
        n = np.random.randint(42,46)

    question = solution.flatten()
    remove=np.random.choice(question.size,n,replace=False)
    question[remove]=0
    question = question.reshape(solution.shape)
    countSolve(question.copy(),count)
    return question

def generate(board,difficulty="easy"):
    solve(fillDiagonal(board))
    while(True):
        count=[0]
        question = generateQuestion(board,"easy",count)
        if count[0]==1:
            return question,board
    
