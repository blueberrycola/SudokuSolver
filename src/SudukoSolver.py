from numpy import array, genfromtxt
from itertools import permutations
#                  (cell)
#                 |_|_|_|  <---- Row ---->
#                 |_|_|_|  ^
#                 |_|_|_|  | (col)
#                          v

# The puzzle class is responsible for taking a data entry from
# sudoku.csv found from kaggle.com and convert it into a readable 2d
# array. Once it becomes a 2d array it is then solved through
# backtracking and permutations

class Puzzle:
    #!!! Possible temporary data. 
    # Used to see what is going on for permli()

    #Read testcase and fill array w data
    def __init__(self, basestr):
        #Create 2d list for sudoku game
        self.arr = [[0 for i in range(9)] for j in range(9)]
        self.basestr = basestr #Base String is ALWAYS 81 chars
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
    def getarr(self): #return entire 2d array inside puzzle obj
        return self.arr
    #Returns array of numbers for a specified row (0-8)
    def getrow(self, n):
        if (n > 8 or n < 0):
            print('invalid param: seerow')
        else:
            return self.arr[n]
    #Returns array of numbers for a specified column (0-8)
    def getcol(self, n): 
        if (n > 8 or n < 0):
            print('invalid param: seecol')
        else:
            temp = []
            for iter in range(9):
                temp.append(self.arr[iter][n])
            return temp
    #Returns numbers contained in one of the sudoku cubes (0-8)
    def getcube(self, n):
        coordList = [] #Takes zero, one, two
        zero = [0,1,2]
        one = [3,4,5]
        two = [6,7,8]
        coordList.append(zero)
        coordList.append(one)
        coordList.append(two)
        #Used to print get values displayed inside a specific cube: arr(i,j)
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
    #Will permute a list of numbers, n = row number,
    def permuteli(self, n):
        standard = ['1','2','3','4','5','6','7','8','9']    #standard - row = list used to solve row via permutation
        row = self.getrow(n)
        #remove matching nums for standard and row
        for element in row:
            if element != '0':
                standard.remove(element)
        perm = permutations(standard, len(standard))    #Create all possible permutations
        for i in perm:
            print(i)
            
            
            
                

            

        
        


def main():
    #Load testcases and answerkeys
    testcases = genfromtxt('../resources/sudoku.csv', dtype='str', delimiter=',', usecols=0, skip_header = 1)
    #answerkey = genfromtxt('../resources/sudoku.csv', dtype='str', delimiter=',', usecols=1, skip_header = 1)

    puzzle = Puzzle(testcases[0])
    p = puzzle.permuteli(0)
    
main()