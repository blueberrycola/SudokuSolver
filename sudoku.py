###       Sudoku Solver       ###
### Written by Chase Johnston ###
###     Version 0.1           ###
import operator
#TODO:
    #Create a function to print the game object X
    #Create a function to load various sudoku puzzles from text X
    #Create function to solve sudoku
    #Create function to check horizontally, vertically, and by each cell.

#Game variables
cellformat = "|  | " #Used to make a cell in sudoku, use index 2 to replace with num
cell = 9
game = [[0]*cell]*cell # The game is made of 9x9 rows and cols [0,80]
                       # It is a 2d list to make vertical and horizontal row checking easier
                       # functions are made to check the indiviual cells

#Loads a text document containing data about sudoku. game is read from left to right, not indiviudal cells.
#Simply enter blank tiles as 0 and others 1-9. delimited by space and newline
def loadgame():
    filename = input("Please enter the filename that is inside the directory: ")
    if(filename == 'debug'):
        filename = "test0_data.txt"
    print(filename)
    f = open(filename, "r")
    
    newgame = f.read().splitlines()
    i = 0
    for x in newgame:
        array = x.split(' ')
        game[i] = array
        i += 1
def printgame():
    i = 0
    counter = 0
    for r in game:
        j = 0
        for c in r:
            if(counter < 9):
                if(counter % 3 == 0 and counter != 0):
                    print(f' . ', end='')                
            if(counter == 9):
                counter = 0
            print(f'| {game[i][j]} |', end='')
            j += 1
            counter += 1
        i += 1
        print()
        if(i == 3 or i == 6):
            print("= - - - - - - - + - - - - - - - - + - - - - - - - =")
#Returns array of each cube inside given sudoku puzzle
def countarray():
    count = []
    count.append(countcube(0))
    count.append(countcube(1))
    count.append(countcube(2))
    count.append(countcube(3))
    count.append(countcube(4))
    count.append(countcube(5))
    count.append(countcube(6))
    count.append(countcube(7))
    count.append(countcube(8))
    return count

upper = [0, 1, 2]
mid = [3, 4, 5]
lower = [6, 7, 8]
#Returns int that contain the count for how many nums are already filled. Used to find the one with the most numbers
def countcube(cubeindex):

    count = 0
    
    if(cubeindex == 0):
        for num in upper:
            for num2 in upper:
                if(game[num][num2] != '0'):
                    count += 1
    if(cubeindex == 1):
        for num in upper:
            for num2 in mid:
                if(game[num][num2] != '0'):
                    count += 1
    if(cubeindex == 2):
        for num in upper:
            for num2 in lower:
                if(game[num][num2] != '0'):
                    count += 1
    if(cubeindex == 3):
        for i in mid:
            for j in upper:
                if(game[i][j] != '0'):
                    count += 1
    if(cubeindex == 4):
        for i in mid:
            for j in mid:
                if(game[i][j] != '0'):
                    count += 1
    if(cubeindex == 5):
        for i in mid:
            for j in lower:
                if(game[i][j] != '0'):
                    count += 1
    if(cubeindex == 6):
        for i in lower:
            for j in upper:
                if(game[i][j] != '0'):
                    count += 1
    if(cubeindex == 7):
        for i in lower:
            for j in mid:
                if(game[i][j] != '0'):
                    count += 1
    if(cubeindex == 8):
        for i in lower:
            for j in lower:
                if(game[i][j] != '0'):
                    count += 1
    
    return count                
#function that finds the max value for the given array. Returns index that goes in order of how to solve
def findseq(arr):
        #default sequence is all nums listed, used as stop condition for while loop
        def_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        cube_seq = []
        done = False
        while(not done):
            #stop condition
            if (def_seq == [-1, -1, -1, -1, -1, -1, -1, -1, -1]):
                #print("array empty yo")
                break
                done = True
            #find max inside arr
            index, value = max(enumerate(arr), key=operator.itemgetter(1))
            #print(f'index: {index} value: {value}')
            cube_seq.append(index)
            #Mark def_seq index as already used. (since any cube will never have -1 numbers inside)
            def_seq[index] = -1
            arr[index] = 0
        return cube_seq
#Returns boolean value if a horizontal row (i) has all nums [1-9]
def checkhorizontal(i):
    numlist = []
    correctlist = [1,2,3,4,5,6,7,8,9]
    for tile in game[i]:
        if(tile == '0'):
            return False
        else:
            numlist.append(tile)
    if(numlist == correctlist):
        return True
    #if num list not equal return false
    return False
#Returns boolean value if a vertical column (j) has all nums [1-9]
def checkvertical(j):
    numlist = []
    correctlist = [1,2,3,4,5,6,7,8,9]
    i = 0
    done = False
    while(not done):
        if(game[i][j] == '0'):
            return False
        else:
            numlist.append(game[i][j])
        i += 1
        if(i == 9):
            done = True
            break
    if(numlist == correctlist):
        return True
    else:
        return False

#Used for get indexes
def checkpair(i, j):
    pair = []
    pair.append(i)
    pair.append(j)
    return pair
#Returns array of pairs for a given cube
def cubeindexes(cubeindex):
    index_pairs = []
    if(cubeindex == 0):
        for num in upper:
            for num2 in upper:
                    if(game[num][num2] != '0'):
                        index_pairs.append(checkpair(num, num2))
                    
        return index_pairs
    if(cubeindex == 1):
        for num in upper:
            for num2 in mid:
                    if(game[num][num2] != '0'):
                        index_pairs.append(checkpair(num, num2))
    if(cubeindex == 2):
        for num in upper:
            for num2 in lower:
                    if(game[num][num2] != '0'):
                        index_pairs.append(checkpair(num, num2))
    if(cubeindex == 3):
        for num in mid:
            for num2 in upper:
                    if(game[num][num2] != '0'):
                        index_pairs.append(checkpair(num, num2))
    if(cubeindex == 4):
        for num in mid:
            for num2 in mid:
                    if(game[num][num2] != '0'):
                        index_pairs.append(checkpair(num, num2))
    if(cubeindex == 5):
        for num in mid:
            for num2 in lower:
                    if(game[num][num2] != '0'):
                        index_pairs.append(checkpair(num, num2))
    if(cubeindex == 6):
        for num in lower:
            for num2 in upper:
                    if(game[num][num2] != '0'):
                        index_pairs.append(checkpair(num, num2))
    if(cubeindex == 7):
        for num in lower:
            for num2 in mid:
                    if(game[num][num2] != '0'):
                        index_pairs.append(checkpair(num, num2))
    if(cubeindex == 8):
        for num in lower:
            for num2 in lower:
                    if(game[num][num2] != '0'):
                        index_pairs.append(checkpair(num, num2))
    

#Solves a given cube via its index inside the actual params
def solvecube(index):
    full_nums = []
    cube_seq = cubeindexes(index)
    print(cube_seq)       


def main():
    loadgame()
    printgame()
    cube_array = countarray()
    print(f'Cube Index [0-8]: {cube_array}')
    #We start with the cubes with the most nums since they are the easiest to solve
    #In order to do this we must find the solving sequence for each cube. Sorting by cubes with most numbers
    solve_sequence = findseq(cube_array)
    print(f'Solving sequence: {solve_sequence}')
    #Now that we have a solving sequence we run solvecube() for each index in solve_sequence
    solvecube(0)
    
    
    
main()