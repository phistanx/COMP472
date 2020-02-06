import copy


class Node:
    state: []
    depth: int
    parent: None

    def __init__(self, state, depth, parent):
        self.state = state
        self.depth = depth
        self.parent = parent


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
    for i in range(len(current_node.state)):
        for j in range(len(current_node.state)):
            temp_node = copy.deepcopy(current_node.state)
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
            if check_in_closed_stack(temp_node, closed_stack):
                open_stack.append(Node(temp_node, current_node.depth + 1, current_node))
            elif find_depth_in_list(temp_node, current_node.depth+1, closed_stack):
                open_stack.append(Node(temp_node, current_node.depth + 1, current_node))

def check_in_closed_stack(temp_node, closed_stack):
    for i in range(len(closed_stack)):
        if temp_node == closed_stack[i].state:
            return False
    return True

def find_depth_in_list(node, depth, closed_list):
    try:
        for i in range(len(closed_list)):
            if node == closed_list[i].state:
                if depth < closed_list[i].depth:
                    closed_list[i].state = node
                    closed_list[i].depth = depth
                    return True
    except:
        print('bruh')


# print(create_boards())

# get initial board
initial_board = create_boards()

# create Node object containing the state and the depth
initial_node = Node(initial_board, 0, None)

# initialize closed and open stack
open_stack = []
closed_stack = []

# dummy max depth for now
max_d = 4

# adding initial node to the stack
open_stack.append(initial_node)

# popping the stack
# current_node = open_stack.pop()

# adding the first pop to the closed stack
# closed_stack.append(current_node)

# find the children of the current node that was popped from the open stack
# findChildren(current_node, open_stack, closed_stack)
# print(open_stack)

# pop the next node at the top of the stack
# current_node = open_stack.pop()

# rinse and repeat
# closed_stack.append(current_node)
# findChildren(current_node, open_stack, closed_stack)
# print(open_stack)

# NEW LOGIC TO BE IMPLEMENTED WITH LOOPS
while len(open_stack) > 0:
    current_node = open_stack.pop()
    closed_stack.append(current_node)
    print(current_node.state)
    if current_node.state == [[0, 0, 0],[0, 0, 0],[0, 0, 0]]:
        print("break")
        print(current_node.state)
        break

    while max_d > current_node.depth:
        findChildren(current_node, open_stack, closed_stack)
        if len(open_stack) == 0:
            break
        current_node = open_stack.pop()
        if current_node.state == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]:
            break
        closed_stack.append(current_node)
        print(current_node.state)

    if current_node.state == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]:
        print("break")
        print(current_node.state)
        break

print("D0ne")
