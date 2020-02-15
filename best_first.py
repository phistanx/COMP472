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

    def __init__(self, state, depth, parent, coordinates, heuristic):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.coordinates = coordinates
        self.heuristic = heuristic


def play_game():
    file = open("input-text/initial.txt", "r")
    for index, line in enumerate(file):
        print("====== START GAME ======")
        search_file_name = "bfs-output/" + str(index) + "_bfs_search.txt"
        search_file = open(search_file_name, "w+")
        solution_file_name = "bfs-output/" + str(index) + "_bfs_solution.txt"
        solution_file = open(solution_file_name, "w+")
        board = shared_functions.create_boards(line)
        start_dfs(board, shared_functions.get_maxl(line), search_file, solution_file)
        print("====== END GAME ======")
        print("")


def get_maxd(contents):
    x = contents.split()
    return int(x[1])


def start_dfs(initial_board, max_l, search_file, solution_file):
    # create Node object containing the state and the depth
    initial_node = Node(initial_board, 1, None, None, 0)

    # initialize closed and open stack
    open_stack = []
    closed_stack = []

    print("MAX D")
    print(max_l)
    # adding initial node to the stack
    open_stack.append(initial_node)

    no_solution = True

    while len(open_stack) > 0:
        current_node = open_stack.pop(0)
        # add the current node to the search file and append it to the closed stack
        shared_functions.writeToSearchFile(shared_functions.convertNestedListToString(current_node.state), search_file, current_node.heuristic)
        closed_stack.append(current_node)
        print(current_node.state)
        if shared_functions.success(current_node.state):
            no_solution = False
            print("====== SOLUTION ======")
            print(current_node.state)
            print(current_node.coordinates)
            shared_functions.writeSolutionFile(current_node, solution_file, initial_board)
            break

        while max_l > len(closed_stack):
            findChildren(current_node, open_stack, closed_stack)
            if len(open_stack) == 0:
                break
            current_node = open_stack.pop(0)
            shared_functions.writeToSearchFile(shared_functions.convertNestedListToString(current_node.state),
                                               search_file, current_node.heuristic)
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
            shared_functions.writeSolutionFile(current_node, solution_file, initial_board)
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
            heuristic = 0
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
            actual_temp_nodes.append(Node(temp_node, current_node.depth + 1, current_node, [i, j + 1], 0))

    find_heuristic(actual_temp_nodes)

    # sort so it enters the stack properly
    # ctual_temp_nodes.sort(key=lambda x: x.heuristic)

    # compare each node in the list to check if it should go to the open_stack or not
    for node in actual_temp_nodes:
        if shared_functions.check_in_closed_stack(node.state, closed_stack):
            open_stack.append(node)
    open_stack.sort(key=lambda x: x.heuristic)

    for i in range(len(open_stack)):
        for j in range(0, len(open_stack) - i - 1):
            if open_stack[j].heuristic == open_stack[j + 1].heuristic:
                if open_stack[j].state > open_stack[j + 1].state:
                    open_stack[j], open_stack[j + 1] = open_stack[j + 1], open_stack[j]


def count_number_of_ones(node):
    count = 0;
    for i in node.state:
        for j in i:
            if j == 1:
                count += 1
    return count;


def find_adjacent_ones(node):
    real_counter = 0
    for i in range(len(node.state)):
        for j in range(len(node.state)):
            counter = 0
            # make a deep copy to not have reference
            temp_node = node.state
            # change the current index to 0/1
            if temp_node[i][j] == 1:
                counter += 1
            # try changing all the nodes next to the current one to 0/1
            try:
                if temp_node[i + 1][j] == 1:
                    counter += 1
            except:
                print(end='')
            # if index array is negative, we want to throw an exception, it shows that the tile is outside of the board
            try:
                if i - 1 < 0:
                    raise Exception('Index array is negative')
                if temp_node[i - 1][j] == 1:
                    counter += 1
            except:
                print(end='')

            try:
                if temp_node[i][j + 1] == 1:
                    counter += 1
            except:
                print(end='')

            try:
                if j - 1 < 0:
                    raise Exception('Index array is negative')
                if temp_node[i][j - 1] == 1:
                    counter += 1
            except:
                print(end='')
            if real_counter < counter:
                real_counter = counter

    if real_counter == 5:
        return 1
    elif real_counter == 4:
        return 2
    elif real_counter == 3:
        return 3
    elif real_counter == 2:
        return 4
    elif real_counter == 1:
        return 5


def find_heuristic(list_nodes):
    for node in list_nodes:
        if count_number_of_ones(node) == 1:
            node.heuristic = 100
        elif count_number_of_ones(node) == 2:
            node.heuristic = 99
        elif count_number_of_ones(node) >= 3:
            node.heuristic = find_adjacent_ones(node)


play_game()
