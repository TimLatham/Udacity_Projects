# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(board):
    if check_int(board) == False:
        return False
    if check_unique(board) == False:
        return False
    board_sum = 0
    for i in range(len(board)+1):
        board_sum = board_sum + i
    if check_row(board, board_sum) and check_column(board, board_sum) == True:
        return True
    return False
    
def check_row(board, board_sum):
    count_row = 0
    while count_row < len(board):
        calculated_board_sum = 0
        count_column = 0
        while count_column < len(board):
            calculated_board_sum = calculated_board_sum + board[count_row][count_column]
            count_column += 1
        #print board_sum, calculated_board_sum
        if board_sum != calculated_board_sum:
            return False
        count_row += 1
    return True
    
def check_column(board, board_sum):
    count_column = 0
    while count_column < len(board):
        calculated_board_sum = 0
        count_row = 0
        while count_row < len(board):
            calculated_board_sum = calculated_board_sum + board[count_row][count_column]
            count_row += 1
        #print board_sum, calculated_board_sum
        if board_sum != calculated_board_sum:
            return False
        count_column += 1
    return True

    
def check_int(board):
    count_row = 0
    while count_row < len(board):
        count_column = 0
        while count_column < len(board):
            #print board[count_row][count_column], count_row, count_column, type(board[count_row][count_column])
            if type(board[count_row][count_column]) != int:
                return False
            count_column += 1
        count_row += 1
    return True

def check_unique(board):
    counter = 0
    while counter < len(board):
        if len(set(board[counter])) != len(board[counter]):
            return False
        counter += 1
    return True


print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False


