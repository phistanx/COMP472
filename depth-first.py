def create_boards():
    f=open("input-text/initial.txt", "r")
    contents =f.read()
    x = contents.split()
    size = x[0]
    max_d = x[1]
    max_l = x[2]
    numbers = x[3]
    i=0
    board = []

    for height in range(int(size)):
        rows = []
        for width in range(int(size)):
            rows.append(int(numbers[i]))
            i = i+1
        board.append(rows)
    return board

def success(board):
    is_successful = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] != 0):
                is_successful = False
    return is_successful

def DFS():
    open_list = []
    closed_list = []
print(create_boards())
c = [[1, 1, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
