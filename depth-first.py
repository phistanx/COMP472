import copy
import pickle
from pathlib import Path
import re

class Node:
    state: []
    depth: int
    parent: None
    coordinates: None

    def __init__(self, state, depth, parent, coordinates):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.coordinates = coordinates


def get_maxd(contents):
    x = contents.split()
    return int(x[1])


def create_boards(contents):
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

def convertNestedListToString(nested_list):
    string_of_list =  ",".join( repr(e) for e in nested_list)
    string_of_list = string_of_list.replace(",", "")
    string_of_list = string_of_list.replace("[","")
    string_of_list = string_of_list.replace("]","")
    string_of_list = string_of_list.replace(" ","")
    return string_of_list

def writeToSearchFile(string_of_list, search_file):
    search_file.write("0" + " 0 " + "0 " + string_of_list+"\n")

def writeSolutionFile(result_node):
    print('PRINT TO FILE')
    solution_path = []
    while result_node.parent != None:
        solution_path.append(result_node)
        result_node = result_node.parent
    solution_path.reverse()
    for i in solution_path:
        print(i.coordinates, end='')
        print(i.state)

def DFS():
    open_list = []
    closed_list = []


def findChildren(current_node, open_stack, closed_stack):
    temp_list = []
    actual_temp_nodes = []
    for i in range(len(current_node.state)):
        for j in range(len(current_node.state)):
            temp_node = pickle.loads(pickle.dumps(current_node.state, -1))
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
                print(end='')

            try:
                if i - 1 < 0:
                    raise Exception('A very specific bad thing happened.')
                if temp_node[i - 1][j] == 1:
                    temp_node[i - 1][j] = 0
                else:
                    temp_node[i - 1][j] = 1
            except:
                print(end='')

            try:
                if temp_node[i][j + 1] == 1:
                    temp_node[i][j + 1] = 0
                else:
                    temp_node[i][j + 1] = 1

            except:
                print(end='')

            try:
                if j - 1 < 0:
                    raise Exception('A very specific bad thing happened.')
                if temp_node[i][j - 1] == 1:
                    temp_node[i][j - 1] = 0
                else:
                    temp_node[i][j - 1] = 1
            except:
                print(end='')
            actual_temp_nodes.append(Node(temp_node, current_node.depth + 1, current_node, [i, j]))
            temp_list.append(temp_node)
    temp_list.sort(reverse=True)
    for i in range(len(temp_list)):
        for j in range(len(actual_temp_nodes)):
            if temp_list[i] == actual_temp_nodes[j].state:
                temp_list[i] = actual_temp_nodes[j]

    for node in temp_list:
        if check_in_closed_stack(node.state, closed_stack):
            open_stack.append(node)
        elif find_depth_in_list(node.state, current_node.depth + 1, closed_stack):
             open_stack.append(node)

def check_in_closed_stack(state, closed_stack):
    for i in range(len(closed_stack)):
        if state == closed_stack[i].state:
            return False
    return True


def find_depth_in_list(state, depth, closed_list):
    try:
        for i in range(len(closed_list)):
            if state == closed_list[i].state:
                if depth < closed_list[i].depth:
                    closed_list[i].state = state
                    closed_list[i].depth = depth
                    return True
    except:
        print('error')

def start_dfs(initial_board, max_d, search_file):

    # create Node object containing the state and the depth
    initial_node = Node(initial_board, 1, None, None)

    # initialize closed and open stack
    open_stack = []
    closed_stack = []

    print("MAX D")
    print(max_d)
    # adding initial node to the stack
    open_stack.append(initial_node)


    no_solution = True

    while len(open_stack) > 0:
        current_node = open_stack.pop()
        writeToSearchFile(convertNestedListToString(current_node.state), search_file)
        closed_stack.append(current_node)
        print(current_node.state)
        if success(current_node.state):
            no_solution = False
            print(current_node.state)
            break

        while max_d > current_node.depth:
            findChildren(current_node, open_stack, closed_stack)
            if len(open_stack) == 0:
                break
            current_node = open_stack.pop()
            writeToSearchFile(convertNestedListToString(current_node.state), search_file)
            if success(current_node.state):
                no_solution = False
                break
            closed_stack.append(current_node)
            print(current_node.state)

        if success(current_node.state):
            no_solution = False
            print("====== SOLUTION ======")
            print(current_node.state)
            print(current_node.coordinates)
            writeSolutionFile(current_node)
            break

    if no_solution:
        print("NO SOLUTION")
        
def play_game():
    file = open("input-text/initial.txt", "r")
    for index, line in enumerate(file):
        print("====== START GAME ======")
        search_file_name = str(index) + "_dfs_search.txt"
        search_file = open(search_file_name,"w+")
        start_dfs(create_boards(line), get_maxd(line), search_file)
        print("====== END GAME ======")
        print("")


play_game()    
