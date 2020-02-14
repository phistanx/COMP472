
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

def writeToSearchFile(string_of_list, search_file):
    search_file.write("0" + " 0 " + "0 " + string_of_list+"\n")

def writeSolutionFile(result_node, solution_file, initial_board):
    print('PRINT TO FILE')
    solution_file.write('0 ' + convertNestedListToString(initial_board) + "\n")
    solution_path = []
    # append result node and iterate the parents all the way to the root
    while result_node.parent != None:
        solution_path.append(result_node)
        result_node = result_node.parent
    solution_path.reverse()
    for i in solution_path:
        coordinate = convertNestedListToString(convert_coordinate(i.coordinates))
        state = convertNestedListToString(i.state)
        solution_file.write(coordinate + " " + state + "\n")
        print(coordinate, end=' ')
        print(state)
 
def convert_coordinate(coordinate):
    number = coordinate[0] + 65
    coordinate[0] = chr(number)
    return coordinate

def convertNestedListToString(nested_list):
    string_of_list =  ",".join( repr(e) for e in nested_list)
    string_of_list = string_of_list.replace(",", "")
    string_of_list = string_of_list.replace("[","")
    string_of_list = string_of_list.replace("]","")
    string_of_list = string_of_list.replace(" ","")
    string_of_list = string_of_list.replace("'","")
    return string_of_list

def success(board):
    is_successful = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] != 0):
                is_successful = False
    return is_successful    

def get_maxl(contents):
    x = contents.split()
    return int(x[2])

def check_in_closed_stack(state, closed_stack):
    for i in range(len(closed_stack)):
        if state == closed_stack[i].state:
            return False
    return True
