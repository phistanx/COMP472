import copy


class Node:
    state: []
    depth: int

    def __init__(self, state, depth):
        self.state = state
        self.depth = depth

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


def findChildren(current_node, open_stack, closed_stack):
    for i in range(len(current_node)):
        for j in range(len(current_node)):
            temp_node = copy.deepcopy(current_node)
            if temp_node[i][j] == 1:
                temp_node[i][j] = 0
            else:
                temp_node[i][j] = 1
            try:
                if temp_node[i + 1][j] == 1:
                    temp_node[i + 1][j] = 0
                else:
                    temp_node[i + 1][j] = 1
            except:
                print("")

            try:
                if i - 1 < 0:
                    raise Exception('A very specific bad thing happened.')
                if temp_node[i - 1][j] == 1:
                    temp_node[i - 1][j] = 0
                else:
                    temp_node[i - 1][j] = 1
            except:
                print("")

            try:
                if temp_node[i][j + 1] == 1:
                    temp_node[i][j + 1] = 0
                else:
                    temp_node[i][j + 1] = 1

            except:
                print("")

            try:
                if j - 1 < 0:
                    raise Exception('A very specific bad thing happened.')
                if temp_node[i][j - 1] == 1:
                    temp_node[i][j - 1] = 0
                else:
                    temp_node[i][j - 1] = 1
            except:
                print("")
            print(temp_node)
            if temp_node not in closed_stack:
                open_stack.append(temp_node)


# print(create_boards())
initial_board = create_boards()
initial_node = Node(initial_board, 0)
open_stack = []
closed_stack = []
max_d = 2
open_stack.append(initial_board)

current_node = open_stack.pop()
closed_stack.append(current_node)

findChildren(current_node, open_stack, closed_stack)
print(open_stack)

current_node = open_stack.pop()
closed_stack.append(current_node)
findChildren(current_node, open_stack, closed_stack)
print(open_stack)

while not open_stack:
    current_node = open_stack.pop()
    max_d_clone = 0
    while max_d > max_d_clone:
        findChildren(current_node, open_stack, closed_stack)
        max_d_clone += 1