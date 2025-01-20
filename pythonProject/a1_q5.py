import heapq
import sys
import csv
from collections import deque

def bfs(graph, start_state, goal_state):
    node_stack = deque([[start_state]])
    visited_nodes = [False] * len(graph)

    while node_stack:
        path = node_stack.popleft()
        current_node = path[-1]

        if current_node == goal_state:
            return path

        if not visited_nodes[current_node]:
            visited_nodes[current_node] = True

            for neighbor_nodes, node_weight in enumerate(graph[current_node]):
                if node_weight is not None and not visited_nodes[neighbor_nodes]:
                    new_path = list(path)
                    new_path.append(neighbor_nodes)
                    node_stack.append(new_path)

    return None

def dfs(graph, start_state, goal_state):

    # A way to track the visited nodes to avoid repeats
    visited_nodes = [False] * len(graph)

    # Stack for DFS (LIFO)
    node_stack = [[start_state]]

    while node_stack:
        # Pop the last path (DFS uses LIFO)
        path = node_stack.pop()
        current_node = path[-1]

        # Check if the goal node is reached
        if current_node == goal_state:
            return path

        # Mark the current node as visited
        if not visited_nodes[current_node]:
            visited_nodes[current_node] = True

            # Add neighbors to the stack
            for neighbor_node, weight in enumerate(graph[current_node]):
                if weight is not None and not visited_nodes[neighbor_node]:
                    new_path = list(path)  # Copy the current path
                    new_path.append(neighbor_node)
                    node_stack.append(new_path)

    # If no path is found, return None
    return None

def greedy_bfs(graph, start_state, goal_state, heuristic):
    priority_queue = [[start_state]]  # Priority queue managed as a list
    visited_nodes = [False] * len(graph)

    while priority_queue:
        # Find and remove the path with the lowest heuristic value
        min_index = 0
        for i in range(1, len(priority_queue)):
            current_path = priority_queue[i]
            best_path = priority_queue[min_index]
            if heuristic[current_path[-1]][goal_state] < heuristic[best_path[-1]][goal_state]:
                min_index = i

        path = priority_queue.pop(min_index)
        current_node = path[-1]

        if current_node == goal_state:
            return path

        if not visited_nodes[current_node]:
            visited_nodes[current_node] = True

            for neighbor_nodes, node_weight in enumerate(graph[current_node]):
                if node_weight is not None and not visited_nodes[neighbor_nodes]:
                    new_path = list(path)
                    new_path.append(neighbor_nodes)
                    priority_queue.append(new_path)

    return None

def a_star(start_state, goal_state, graph, heuristic):
    return None

def graph_search():
    """
    You are free to implement this however you like but you will most likely need to input the graph data structure G, the heuristic function h, the start state s, the goal state t, and the search strategy X  
    """

    match search_strategy:
        case "B":
            return bfs(graph, start_state, goal_state)
        case "D":
            return dfs(graph, start_state, goal_state)
        case "G":
            return greedy_bfs(graph, start_state, goal_state, heuristic)
        case "D":
            return a_star(start_state, goal_state, graph, heuristic)


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


