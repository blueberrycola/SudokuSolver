###       Sudoku Solver       ###
### Written by Chase Johnston ###
###     Version 0.1           ###

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
#Returns array that contain the count for how many nums are already filled. Used to find the one with the most numbers
def countcube(cubeindex):
    upper = [0, 1, 2]
    mid = [3, 4, 5]
    lower = [6, 7, 8]
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
    
        
def main():
    loadgame()
    printgame()
    print(countcube(0))
    print(countcube(1))
    print(countcube(2))
    print(countcube(3))
    print(countcube(4))
    print(countcube(5))
    print(countcube(6))
    print(countcube(7))
    print(countcube(8))
    
    
    
main()