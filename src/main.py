import time
import os
import algorithms
from data_fetch import graph_generation

if __name__ == "__main__":

    file_path = "dataset/amazon0312-weighted.txt"

    # Generate the graph one time because the struct don't change
    graph_weighted = graph_generation(file_path, weighted=True) # This works for Dijkstra (weighted graph)
    graph_unweighted = graph_generation(file_path, weighted=False) # For the others agorithms (non-weighted)

    keys = list(graph_weighted.keys()) # The nodes are the same in both graph
    elements = list()

    # Add the nodes of the archs to the exsits nodes for get all the nodes of the graph
    for key in keys:

        for elem in graph_weighted[key]:

            if isinstance(elem, tuple): # For weighted graph
                elements.append(elem[0])

            else:
                elements.append(elem)

    all_nodes = set(keys + elements) # Create a set that contains all the unique nodes

    while True: 

        # Delete the shell every search session
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n\n--- SEARCH ALGORITHM ---")

        depth = 0 # Depth default value

        # Start node
        while True:

            try:

                start_node = int(input("Write the start node: "))

                if start_node not in all_nodes:
                    raise ValueError
                
                break

            except ValueError:
                print("Error: Node not found. Retry.")

        # End node
        while True:

            try:

                goal_node = int(input("Write the end node: "))

                if goal_node not in all_nodes:
                    raise ValueError
                
                break

            except ValueError:
                print("Error: Node not found. Retry.")

         # Select of algorithm
        while True:

            try:

                print("\nSelect the search algorithm:")
                print("0 -> Breadth-First (BFS)")
                print("1 -> Depth-First (DFS)")
                print("2 -> Depth-Limited (DLS)")
                print("3 -> Iterative Deepening (IDS)")
                print("4 -> Dijkstra")

                choice = int(input("\nChoice: "))

                match choice:
                    
                    case 0:
                        search_type = "BFS"
                        graph = graph_unweighted
                    case 1:
                        search_type = "DFS"
                        graph = graph_unweighted
                    case 2:
                        depth = int(input("\nSelect the maximum depth for the search: "))
                        if depth < 0:
                            raise ValueError
                        search_type = "DLS"
                        graph = graph_unweighted
                    case 3:
                        search_type = "IDS"
                        graph = graph_unweighted
                    case 4:
                        search_type = "Dijkstra"
                        graph = graph_weighted
                    case _:
                        raise ValueError

                break
            
            except ValueError:
                print("Error: Choice not allowed. Retry.")

        # Execute the search
        timer = time.perf_counter() # Start of the timer for calculate the execution time
        algorithms.search(start_node, goal_node, graph, search_type, depth, timer)

        # Check for another serach
        answer = input("Do you want to do another search? (y/n): ").strip().lower()
        if answer != 'y':  
            break # End the program

    print("Bye. See you the next time")