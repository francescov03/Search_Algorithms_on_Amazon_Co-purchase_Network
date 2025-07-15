from collections import deque, defaultdict
import sys
import time
import heapq

sys.setrecursionlimit(500000) # Set the limit of recursion to 500000 (need to adact for your necessity)

def configure_recursion_limit(new_limit: int) -> bool:
    """
    Set a new recursion limit for prevent RecursionError in the DFS search.
    """

    try:
        if new_limit > 1:
            sys.setrecursionlimit(new_limit)
            return True
        
    except (TypeError, RecursionError):
        print("The recursion limit must be an integer >= 2")

    return False



#BREADTH-FIRST SEARCH
def breadth_first_search(graph: defaultdict, start: int, goal: int):

    iterations = 1
    memory_used = 1

    if start == goal:
        return ("Breadth-First Search", [start], iterations, memory_used)
    
    queue = deque([(start, [start])])
    explored = set()

    while queue:

        current_node, path = queue.popleft()

        if current_node in explored:
            continue

        explored.add(current_node)

        for nearby in graph[current_node]:

            iterations += 1
            memory_used = max(memory_used, len(queue))

            if nearby == goal:
                return ("Breadth-First Search", path + [nearby], iterations, memory_used)
            
            queue.append((nearby, path + [nearby]))

    return None # Path not found



#DIJKSTRA ALGORITHM
def dijkstra_search(graph, start, goal):

    priority_queue = [(0, start, [start])] # (cost, current node, path)
    explored = {}
    iterations = 1
    memory_used = 1

    while priority_queue:

        cost, current_node, path = heapq.heappop(priority_queue)

        if current_node in explored and explored[current_node] <= cost:
            continue

        explored[current_node] = cost

        if current_node == goal:
            return ("Dijkstra Search", path, iterations, memory_used, cost)
        
        for neighbor, weight in graph.get(current_node, []):
            new_cost = cost + weight
            heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))
            iterations += 1
            memory_used = max(memory_used, len(priority_queue))

    return None # Path not found



#DEPTH-FIRST SEARCH
def depth_first_search(graph: defaultdict, start_node: int, goal_node: int):

    explored = set()
    path = []
    performance = [0, 0] # Iterations, Memory used

    if dfs_recursion(graph, start_node, goal_node, path, explored, performance):
        return ("Depth-First Search", path, *performance)
    
    return None # Path not found

def dfs_recursion(graph, current_node, goal_node, path, explored, performance):

    # Add current node to the path and on explored set
    path.append(current_node)
    explored.add(current_node)

    # Increase the number of iterations and monitor memory
    performance[0] += 1 # Iterations
    performance[1] = max(performance[1], len(path)) # Memory used

    # If the current node is the target node, end the search
    if current_node == goal_node:
        return True
    
    # Explore adjacent nodes
    for nearby in graph[current_node]: # Check if the adjacent node has not been explored yet

        if nearby not in explored: # Continue the search recursively

            if dfs_recursion(graph, nearby, goal_node, path, explored, performance):
                return True
            
    # Remove the current node if path not found
    path.pop()

    return False



#DEPTH-LIMITED SEARCH
def depth_limited_search(graph, start_node, goal_node, recursion_limit):

    explored = set()
    path = []
    performance = [0, 0, -1, recursion_limit] # Iterations, Memory, Actual depth, Limit depth
    
    if dls_recursion(graph, start_node, goal_node, path, explored, performance):
        return (f"Depth-Limited Search [LIMIT: {recursion_limit}]", path, *performance)
    
    return None # Path not found

def dls_recursion(graph, current_node, goal_node, path, explored, performance):

    path.append(current_node)
    explored.add(current_node)
    performance[2] += 1 # Actual depth
    performance[0] += 1 # Iterations
    performance[1] = max(performance[1], len(path))

    if current_node == goal_node:
        return True
    
    if performance[2] < performance[3]: # Check of the depth limit

        for nearby in graph[current_node]:

            if nearby not in explored and dls_recursion(graph, nearby, goal_node, path, explored, performance):
                return True
            
    performance[2] -= 1
    path.pop()

    return False



#ITERATIVE-DEEPING SEARCH
def iterative_deepening_search(graph, start_node, goal_node):

    recursion_limit = 0
    start_time = time.time()

    while True:

        result = depth_limited_search(graph, start_node, goal_node, recursion_limit)

        if result:
            return (f"Iterative Deepening Search [DEPTH SOLUTION: {recursion_limit}]", result[1], *result[2:])
        
        recursion_limit += 1
        
        if time.time() - start_time > 1800: # Failsafe after 30 minutes
            return None # Path not found



# SEARCH METHOD
def search(start_node, goal_node, graph, search_type, depth, start_time):
    """
    Principal function for execute the search on the type of selected algorithm.
    """
    
    result = ()

    #CHOICE
    match search_type:

        case "BFS":
            result = breadth_first_search(graph, start_node, goal_node)
            
        case "DFS":
            result = depth_first_search(graph, start_node, goal_node)

        case "DLS":
            result = depth_limited_search(graph, start_node, goal_node, depth)

        case "IDS":
            result = iterative_deepening_search(graph, start_node, goal_node)

        case "Dijkstra":
            result = dijkstra_search(graph, start_node, goal_node)

    timer = time.perf_counter()

    if result:

        print(f"\n\n-- RESULT --\nPath from Node {start_node} to Node {goal_node}: \n{result[1]}"
              f"\n\nPATH LENGTH: {len(result[1])} nodes\nTIME COMPLEXITY: {result[2]} iterations"
              f"\nEXECUTION TIME: {timer - start_time:.6f}s\nMAXIMUM MEMORY USAGE: {result[3]} queue elements"
              f"\nALGORITHM USED: {result[0]}")
        
        if search_type == "Dijkstra":
            print(f"COST: {result[4]}")

    else:
        print(f"\nNo path found from Node {start_node} to Node {goal_node}\n")