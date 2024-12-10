def is_safe(row, col, board, n):
    dup_row = row
    dup_col = col

    while col >= 0 and row >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    row = dup_row
    col = dup_col
    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1

    col = dup_col
    row = dup_row

    while row < n and col >= 0:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1

    return True

def solve_n_queen(n):
    ans = []
    board = [['.' for _ in range(n)] for _ in range(n)]  # Initialize the board as a 2D list

    def helper(col, board):
        if col == n:  # If all queens are placed
            ans.append([''.join(row) for row in board])  # Convert each row to a string
            return

        for row in range(n):
            if is_safe(row, col, board, n):
                board[row][col] = 'Q'  # Place queen
                helper(col + 1, board)  # Recurse to the next column
                board[row][col] = '.'  # Backtrack by removing the queen

    helper(0, board)  
    return ans

# Test the solution for n = 4
n = 4
ans = solve_n_queen(n)
print(ans)
