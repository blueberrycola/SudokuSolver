from numpy import array, genfromtxt
#TODO:                                              (cell)
#   Create Puzzle Object, fmt str                   |_|_|_|  <---- Row ---->
#   Create seeRow, seeCol, and seeCell              |_|_|_|  ^
#   Find some backtracking algos to try             |_|_|_|  | (col)
#   Implement testing                                                         v
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
    def getcube(self, n):

        coordList = []
        zero = [0,1,2]
        one = [3,4,5]
        two = [6,7,8]
        coordList.append(zero)
        coordList.append(one)
        coordList.append(two)
        i = []
        j = []
        if(n >= 0 and n <= 2): #upper cubes
            i = zero
            j = coordList[0]
            if(n == 1):
                j = coordList[1]
            elif(n ==2):
                j = coordList[2]
        elif(n >= 3 and n <= 5): #middle cubes
            i = one
            j = coordList[0]
            if(n == 4):
                j = coordList[1]
            elif(n == 5):
                j = coordList[2]
        elif(n >= 6 and n <= 8): #lower cubes
            i = two
            j = coordList[0]
            if(n == 7):
                j = coordList[1]
            elif(n == 8):
                j = coordList[2]
        else:
            print('fixme: throw exception')
        temp = []
        for e in i:
            for element in j:
                temp.append(self.arr[e][element])
        return temp
        
        


def main():
    #Load testcases and answerkeys
    testcases = genfromtxt('../resources/sudoku.csv', dtype='str', delimiter=',', usecols=0, skip_header = 1)
    #answerkey = genfromtxt('../resources/sudoku.csv', dtype='str', delimiter=',', usecols=1, skip_header = 1)

    puzzle = Puzzle(testcases[0])
    cube = puzzle.getcube(0)
    print(cube)
    cubetwo = puzzle.getcube(1)
    print(cubetwo)

main()