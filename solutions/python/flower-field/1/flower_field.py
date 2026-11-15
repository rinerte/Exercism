def annotate(garden):
    # Function body starts here
    for index, row in enumerate(garden):
        if index > 0 and len(row) != len(garden[index - 1]):
            raise ValueError("The board is invalid with current input.")
        if set(row) > set(" *"):
            raise ValueError("The board is invalid with current input.")

    board = []
    for line in garden:
        board.append([0 if char == " " else "*" for char in line])
        
    rows_count = len(board)
    cols_count = len(board[0]) if rows_count > 0 else 0

    for i in range(rows_count):
        for j in range(cols_count):
            if board[i][j] == "*":
                for r, c in get_indexes(i, j, rows_count, cols_count):
                    if board[r][c] != "*":
                        board[r][c] += 1

    result = []
    for row in board:
        line = "".join(" " if cell == 0 else str(cell) for cell in row)
        result.append(line)

    return result
        

def get_indexes(row,col,rows,cols):
    indexes = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < rows and 0 <= j < cols:
                if i != row or j != col:
                    indexes.append((i, j))
    return indexes
    