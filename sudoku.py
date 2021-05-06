###       Sudoku Solver       ###
### Written by Chase Johnston ###
###     Version 0.1           ###

#TODO:
    #Create a function to print the game object

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
            print("- - - - - - - - - - - - - - - - - - - - - - - - -")



        
def main():
    loadgame()
    printgame()
    
    
main()