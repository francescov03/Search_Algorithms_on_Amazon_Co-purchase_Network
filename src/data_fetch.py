from collections import defaultdict

def graph_generation(file_path: str, weighted=True) -> defaultdict:
    """
    Function for create a graph reading nodes e weights from file.
    - weighted=True → Keep weight (Dijkstra).
    - weighted=False → Ignore weight (BFS, DFS, DLS, IDS).
    """
    graph = defaultdict(list)
    
    try:
        
        with open(file_path, 'r') as file:
            for row in file:
                if row.startswith('#'):
                    continue

                parts = row.strip().split('\t')
                
                if len(parts) == 3:
                    from_node, to_node, weight = int(parts[0]), int(parts[1]), int(parts[2])

                    if weighted:
                        graph[from_node].append((to_node, weight))  # Keep weight

                    else:
                        graph[from_node].append(to_node)  # Ignore weight

                elif len(parts) == 2:  # Manage file without weight
                    from_node, to_node = int(parts[0]), int(parts[1])
                    graph[from_node].append(to_node)
    
    except Exception as e:
        print(f"Error while reading file: {e}")
    
    return graph
