# SudokuSolver
A python program that can load sudoku puzzles and solve them for you.

The dataset for creation and unit testing was found via kaggle.com
Inside this dataset there are two different columns. One is the puzzle itself and the next is it's solution.
For every puzzle and solution entered it is read by the computer left to right.
Which means for every 9 numbers a new row is made.

The most viable way to solve a sudoku puzzle as a computer scientist is to take advantage of using a
backtracking algoritm that will find permutations of the numbers that are not filled in.

In order for a row to be correct it must equal 45. Why 45? Because 1+2+3+4+5+6+7+8+9=45

#File Structure:
resources/ -> testing and puzzle data
src/ ->
       SudokuSolver.py: pulls puzzle data from resources and solves a given puzzle.
       SudokuTester.py: pulls solution data from resources and ensures SudokuSolver is working correctly.
       ...
       
TODO:
  define function to find indices of a given row that doesn't have 0's
    -> Take indices of filled spaces and begin permutation work.
      -> if permutation of row = 45. then save it as a viable row
      -> Once 3 rows are complete check their cubes
      -> if cubes all = 45 then move onto the next 3
  Unit testing
