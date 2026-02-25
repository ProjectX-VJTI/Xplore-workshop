# Valid Sudoku
def valid(board):
    # check rows
    for r in range(9):
        nums = []
        for c in range(9):
            if board[r][c] != 0:
                if board[r][c] in nums:
                    return False
                nums.append(board[r][c])

    # check columns
    for c in range(9):
        nums = []
        for r in range(9):
            if board[r][c] != 0:
                if board[r][c] in nums:
                    return False
                nums.append(board[r][c])

    # check 3x3 boxes
    for sr in range(0, 9, 3):
        for sc in range(0, 9, 3):
            nums = []
            for r in range(sr, sr+3):
                for c in range(sc, sc+3):
                    if board[r][c] != 0:
                        if board[r][c] in nums:
                            return False
                        nums.append(board[r][c])
    return True


# input
board = []
for i in range(9):
    row = list(map(int, input().split()))
    board.append(row)

# output 
if valid(board):
    print("Valid")
else:
    print("Invalid")




