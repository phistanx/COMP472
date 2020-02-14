import copy
import pickle
from pathlib import Path
import re 
import shared_functions

class Node:
    state: []
    depth: int
    parent: None
    coordinates: None
    heuristic: int

    def __init__(self, state, depth, parent, coordinates,heuristic):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.coordinates = coordinates
        self.heuristic = heuristic

def play_game():
    file = open("input-text/initial.txt", "r")
    for index, line in enumerate(file):
        print("====== START GAME ======")
        search_file_name = str(index) + "_dfs_search.txt"
        search_file = open(search_file_name,"w+")
        solution_file_name = str(index) + "_dfs_solution.txt"
        solution_file = open(solution_file_name,"w+")
        board = shared_functions.create_boards(line)
        start_dfs(board, get_maxd(line), search_file, solution_file)
        print("====== END GAME ======")
        print("")

def get_maxd(contents):
    x = contents.split()
    return int(x[1])
   
def start_dfs(initial_board, max_d, search_file, solution_file):

    # create Node object containing the state and the depth
    initial_node = Node(initial_board, 1, None, None,0)

    # initialize closed and open stack
    open_stack = []
    closed_stack = []

    print("MAX D")
    print(max_d)
    # adding initial node to the stack
    open_stack.append(initial_node)

    no_solution = True

    while len(open_stack) > 0:
        current_node = open_stack.pop(0)
        # add the current node to the search file and append it to the closed stack
        shared_functions.writeToSearchFile(shared_functions.convertNestedListToString(current_node.state), search_file)
        closed_stack.append(current_node)
        print(current_node.state)
        if shared_functions.success(current_node.state):
            no_solution = False
            print("====== SOLUTION ======")
            print(current_node.state)
            print(current_node.coordinates)
            shared_functions.writeSolutionFile(current_node, solution_file, initial_board)
            break

        while max_d > current_node.depth:
            findChildren(current_node, open_stack, closed_stack)
            if len(open_stack) == 0:
                break
            current_node = open_stack.pop(0)
            shared_functions.writeToSearchFile(shared_functions.convertNestedListToString(current_node.state), search_file)
            if shared_functions.success(current_node.state):
                no_solution = False
                break
            closed_stack.append(current_node)
            print(current_node.state)

        if shared_functions.success(current_node.state):
            no_solution = False
            print("====== SOLUTION ======")
            print(current_node.state)
            print(current_node.coordinates)
            shared_functions.writeSolutionFile(current_node,solution_file, initial_board)
            break

    if no_solution:
        solution_file.write("No solution")
        print("NO SOLUTION")

def findChildren(current_node, open_stack, closed_stack):
    temp_list = []
    actual_temp_nodes = []
    # iterate through the board
    for i in range(len(current_node.state)):
        for j in range(len(current_node.state)):
            # make a deep copy to not have reference
            temp_node = pickle.loads(pickle.dumps(current_node.state, -1))
            # change the current index to 0/1
            if temp_node[i][j] == 1:
                temp_node[i][j] = 0
            else:
                temp_node[i][j] = 1
            # try changing all the nodes next to the current one to 0/1
            try:
                if temp_node[i + 1][j] == 1:
                    temp_node[i + 1][j] = 0
                else:
                    temp_node[i + 1][j] = 1
            except:
                print(end='')
            # if index array is negative, we want to throw an exception, it shows that the tile is outside of the board
            try:
                if i - 1 < 0:
                    raise Exception('Index array is negative')
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
                    raise Exception('Index array is negative')
                if temp_node[i][j - 1] == 1:
                    temp_node[i][j - 1] = 0
                else:
                    temp_node[i][j - 1] = 1
            except:
                print(end='')
            # we create a Node object containing the values and add it to the list
            actual_temp_nodes.append(Node(temp_node, current_node.depth + 1, current_node, [i, j+1],0))

            heuristic(actual_temp_nodes)
 
    # sort so it enters the stack properly
    actual_temp_nodes.sort(key=lambda x: x.heuristic)

    # compare each node in the list to check if it should go to the open_stack or not
    for node in actual_temp_nodes:
        if shared_functions.check_in_closed_stack(node.state, closed_stack):
            open_stack.append(node)      

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


def heuristic (list_nodes):
    for node in list_nodes:
        for i in node.state:
            for j in i:
                if j == 1:
                    node.heuristic += 1

play_game()


