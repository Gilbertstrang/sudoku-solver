board_ex = [  [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
  ]


def solver(board):

    empty = empty_finding(board)
    
    if not empty:                                                       #if there are no zeros(empty positions) return, otherwise take the coordinates of the empty positions      
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if is_valid(board, i, (row,col)):                               #if its valid, add the number to the position   
            board[row][col] = i                                                     

            if solver(board):                                           #if our values we inserted are valid, this should return True(recursion madness), if not then we will backtrack (below code)
                return True
            
            board[row][col] = 0                                         #if you couldn't find a valid number to the position, backtrack and change it to zero (empty)
    
    return False



def is_valid(board, value, position):                                   #value is the number we are inserting, position is (row, column)
    for i in range(len(board[0])):                                      #checks rows
        if board[position[0]][0] == value and position[1] != i:         #checks if each value in row equal to the value we are adding, ignore the position you just inserted     
            return False

    for i in range(len(board)):                                         #checks columns
        if board[i][position[1]] == value and position[0] != i:         #checks if each value in column equal to the value we are adding, ignore the position you just inserted 
            return False
    
    grid_x = (position[1] // 3) * 3                                     #grid_x and grid_y are the positions of the 3x3 grids (x,y), takes the row and column and finds the grind
    grid_y = (position[0] // 3) * 3                                     #we multiply it with 3  to get access to indexes in that grid i.e. top right grid starts with 6th number

    for i in range(grid_y, grid_y + 3):                                 # +3 is there because there are only 3 numbers in a row/in a column in one grid                 
        for j in range(grid_x, grid_x + 3):
            if board[i][j] == value and (i, j) != position:             #this checks if are there any other same values added, ignore the position you just inserted
                return False
    
    return True

def print_board(board):                                                  #prints the board to the console
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:                                        #separates 3x3 grids  horizontally 
            print("---------------------")
        
        for j in range(len(board[0])):                                   #separetes 3x3 grids vertically
            if j % 3 == 0 and j != 0 :
                print ("| ", end="")

            if j == 8:                                                   #just for putting space after the number
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def empty_finding(board):                                                #checks if there any zeros in board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)                                            #returns row and column, if no zeros returns none
    return None                         


print_board(board_ex)
solver(board_ex)
print("************************SOLUTION**************************")
print_board(board_ex)