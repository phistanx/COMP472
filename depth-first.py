def create_boards():
    f = open("input-text/initial.txt", "r")
    contents = f.read()
    x = contents.split()
    size = x[0]
    max_d = x[1]
    max_l = x[2]
    numbers = x[3]
    i = 0
    board = []

    for height in range(int(size)):
        rows = []
        for width in range(int(size)):
            rows.append(int(numbers[i]))
            i = i + 1
        board.append(rows)
    return board


def success(board):
    is_successful = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] != 0):
                is_successful = False
    return is_successful


def DFS():
    open_list = []
    closed_list = []


print(create_boards())
initial_board = create_boards()
open_stack = []
open_stack.append(initial_board)

current_node = open_stack.pop()

# for i in range(len(current_node)):
#     for j in range(len(current_node)):

# for i in range(1):
#     for j in range(1):
for i in range(len(current_node)):
    for j in range(len(current_node)):
        if current_node[i][j] == 1:
            current_node[i][j] = 0
        else:
            current_node[i][j] = 1
        print(current_node)

        try:
            if current_node[i + 1][j] == 1:
                current_node[i + 1][j] = 0
            else:
                current_node[i + 1][j] = 1
        except:
            print("first if")

        try:
            if i - 1 < 0:
                raise Exception('A very specific bad thing happened.')
            if current_node[i - 1][j] == 1:
                current_node[i - 1][j] = 0
            else:
                current_node[i - 1][j] = 1
        except:
             print("fourth if")

        try:
            if current_node[i][j + 1] == 1:
                current_node[i][j + 1] = 0
            else:
                current_node[i][j + 1] = 1

        except:
            print("second if")

        try:
            if j - 1 < 0:
                raise Exception('A very specific bad thing happened.')
            if current_node[i][j - 1] == 1:
                current_node[i][j - 1] = 0
            else:
                current_node[i][j - 1] = 1
        except:
            print("third if")

        print(current_node)
