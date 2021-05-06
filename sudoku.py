###       Sudoku Solver       ###
### Written by Chase Johnston ###
###     Version 0.1           ###

#TODO:
    #Create a function to print the game object

#Game variables
cellformat = "|  | " #Used to make a cell in sudoku, use index 2 to replace with num
cell = 9
game = [[0]*cell]*cell # Each cell contains 9 cells
#prints a cell and uses |  | to format each cell. Actual param example game[0], game[2], etc
def printcell(cell):
    cellstart = "| "
    cellend = " |"
    i = 0
    for num in cell:
        if(i == 3):
            print(" ")
            i = 0
        
        print(cellstart),
        print(num),
        print(cellend),
        i += 1
#sets a cell based on the newarray, must be size 9
def setcell(cell, newarray):
    i = 0
    for num in cell:
        cell[i] = newarray[i]
        i += 1




    


def main():
    #printcell(game[0])
    setcell(game[0], [1, 2, 3, 4, 5, 6, 7, 8, 9])
    printcell(game[0])
    

main()



