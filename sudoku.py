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
    #Reads a line in file name 9 times
    #Iterator vars to keep track of game index
    i = 0
    #Checks the line for the text document exactly 9 times.
    #All that is needed to load sudoku into python application
    for x in range(9):
        #take line from txt and turn it into a list
        row = f.readline()
        row = row.split(' ')
        #j must reset after a row has been completed
        j = 0
        #For each item in row put it according the game index using i, j vars
        for item in row:
            game[i][j] = row[j]
            print(game[i][j]),
            j += 1         
        #Used to know where game is in the loop
        i += 1


        
def main():
    loadgame()
main()