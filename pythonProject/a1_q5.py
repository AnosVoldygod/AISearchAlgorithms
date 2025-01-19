import sys
import csv
from collections import deque

def bfs(graph, start_state, goal_state):

    # Starting node to the node stack

    node_stack = deque([[start_state]])

    # A way to track the visited nodes to avoid repeats
    visited_nodes = [False] * len(graph)

    current_node = 0

    while current_node != goal_state:
        #Add first node to the path and remove it from the stack
        path = node_stack.popleft()
        #Define the current node
        current_node = path[-1]
        #Check if the goal node has been reached
        if current_node == goal_state:
            return path

        #Mark current node as visited on the list
        visited_nodes[current_node] = True

        for neighbor_nodes, node_weight in enumerate(graph[current_node]):
            if node_weight is not None and not visited_nodes[neighbor_nodes]:
                # Mark explored neighbor node as visited on the list
                visited_nodes[neighbor_nodes] = True
                new_path = list(path)
                new_path.append(neighbor_nodes)
                node_stack.append(new_path)


    # Return None if no path exists
    return None
def dfs(graph, start_state, goal_state):

    # A way to track the visited nodes to avoid repeats
    visited_nodes = [False] * len(graph)

    node_stack = deque([[start_state]])

    def dfs_loop(current_node, goal_node, graph_thing):

        path = node_stack.popleft()
        # Define the current node
        current_node = path[-1]

        # Makes sure loop ends at goal
        if current_node == goal_node:
            return path

        # Mark the visited node as true because already confirmed not false
        visited_nodes[current_node] = True

        for neighbor_nodes, neighbor_weights in enumerate(graph_thing[current_node]):
            if neighbor_weights is not None and not visited_nodes[neighbor_nodes]:
                # Mark the first visited neighbor node as true
                visited_nodes[neighbor_nodes] = True
                new_path = list(path)
                new_path.append(neighbor_nodes)
                node_stack.append(new_path)

                # Make sure results are returned
                result = dfs_loop(neighbor_nodes, goal_node, graph_thing)
                if result is not None:
                    return result

        # If no path is found, return None
        return None

    return dfs_loop(start_state, goal_state, graph)

def graph_search():
    """
    You are free to implement this however you like but you will most likely need to input the graph data structure G, the heuristic function h, the start state s, the goal state t, and the search strategy X  
    """

    match search_strategy:
        case "B":
            return bfs(graph, start_state, goal_state)
        case "D":
            return dfs(graph, start_state, goal_state)
        case "C":
            return None
        case "D":
            return None


# ---- INCLUDE ANY OTHER CODE THAT YOU NEED HERE ----


if __name__ == "__main__":

    # get parameters from command line. We need -1 for our vertex numbers since our indexing starts at 0 in python
    start_state = int(sys.argv[1]) - 1
    goal_state = int(sys.argv[2]) - 1
    search_strategy = sys.argv[3]
    graph_csv = sys.argv[4]
    heuristic_csv = sys.argv[5]

    # get the graph
    graph = []
    with open(graph_csv, "r", encoding='utf-8-sig') as csvfile:
        reader_variable = csv.reader(csvfile, delimiter=",")
        for row in reader_variable:
            row_as_ints = [int(val) if val != '' else None for val in row]
            graph.append(row_as_ints)

    # get the heuristic matrix
    heuristic = []
    with open(heuristic_csv, "r", encoding='utf-8-sig') as csvfile:
        reader_variable = csv.reader(csvfile, delimiter=",")
        for row in reader_variable:
            heuristic_row = [float(val) if val != '' else None for val in row]
            heuristic.append(heuristic_row)

    # once we have the goal we can create the heuristic function using the matrix
    heuristic_func = lambda n: heuristic[n][goal_state]        
            
    # find and print the path. The vertices are numbered as they appear in the original graph. Add whatever inputs you need to your graph search function
    path = graph_search()
    if path is not None:
        path = str([state + 1 for state in path])
    print(path)


