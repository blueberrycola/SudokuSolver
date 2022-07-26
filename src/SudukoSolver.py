from numpy import genfromtxt
#TODO:                                              (cell)
#   Create Puzzle Object, fmt str                   |_|_|_|  <---- Row ---->
#   Create seeRow, seeCol, and seeCell              |_|_|_|  ^
#   Find some backtracking algos to try             |_|_|_|  | (col)
#                                                            v
#   fmt str: 
        #getrow
        #getcol
        #getcube
#
#

class Puzzle:
    #Read testcase and fill array w data
    def __init__(self, basestr):
        #Create 2d list for sudoku game
        self.arr = [[0 for i in range(9)] for j in range(9)]
        self.basestr = basestr #Always 81 chars total
        #i,j => (row, col)
        i = 0
        j = 0
        for element in basestr:
            self.arr[i][j] = element
            if j == 8:
                j = 0
                i += 1
            else:
                j += 1
    def getarr(self): #return entire 2d array
        return self.arr
    def getrow(self, n): #return a specified row
        if (n > 8 or n < 0):
            print('invalid param: seerow')
        else:
            return self.arr[n]
    def getcol(self, n): #return a specified column
        if (n > 8 or n < 0):
            print('invalid param: seecol')
        else:
            temp = []
            for iter in range(9):
                temp.append(self.arr[iter][n])
            return temp
    #FIXME: GET CUBE!!!

def main():
    #Load testcases and answerkeys
    testcases = genfromtxt('../resources/sudoku.csv', dtype='str', delimiter=',', usecols=0, skip_header = 1)
    #answerkey = genfromtxt('../resources/sudoku.csv', dtype='str', delimiter=',', usecols=1, skip_header = 1)

    puzzle = Puzzle(testcases[0])
    a = puzzle.getarr()
    r = puzzle.getrow(0)
    print(r)
    c = puzzle.getcol(0)
    print(c)
    print(a)
    #print(answerkey[0])
main()