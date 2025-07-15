# Search_Algorithms_on_Amazon_Co-purchase_Network

This project implements and analyzes several uninformed and informed search algorithms applied to large-scale real-world graphs.

## Dataset

The dataset used is [`amazon0312.txt`](https://snap.stanford.edu/data/amazon0312.html) from the Stanford Large Network Dataset Collection (SNAP), representing the Amazon product co-purchasing network.

A preprocessed version, `amazon0312-weighted.txt`, is used to include weights on the edges to allow cost-based search (e.g., Dijkstra).

## Implemented Algorithms

The following search algorithms are implemented:

- **Breadth-First Search (BFS)** – explores level by level, returns the shortest path in number of steps.
- **Depth-First Search (DFS)** – explores deep into one branch before backtracking.
- **Depth-Limited Search (DLS)** – DFS with a maximum depth constraint.
- **Iterative Deepening Search (IDS)** – multiple DLS passes with increasing depth.
- **Dijkstra’s Algorithm** – informed, cost-optimal path search based on edge weights.

## Metrics Collected

For each algorithm, the following metrics are evaluated:

- **Path found** (if any)
- **Path length** (number of nodes)
- **Execution time**
- **Number of iterations**
- **Maximum memory usage** (based on queue or stack size)
- **Path cost** (only for Dijkstra)

## 📂 Project Structure

```
.
├── weight/
│   └── converter.py       # Used for generate a random weight for every arch
├── src/
│   ├── algorithms.py       # All algorithm implementations
│   ├── data_fetch.py       # Graph loading and parsing logic
│   └── main.py             # Command-line user interface
├── dataset/
│   ├── amazon0312.txt
│   └── amazon0312-weighted.txt
├── LICENSE             # License
└── README.md           # Project documentation
```

## ▶️ How to Run

Make sure you have Python 3 installed, then simply run:

```bash
python main.py
```
or
```bash
python3 main.py
```

Follow the terminal prompts to:
1. Select start and end nodes
2. Choose a search algorithm
3. View the results and metrics
4. Optionally run another search

## 📈 Example Output

```
-- RESULT --
Path from Node 12 to Node 999:
[12, 45, 201, ..., 999]

PATH LENGTH: 14 nodes
TIME COMPLEXITY: 1890 iterations
EXECUTION TIME: 0.084501s
MAXIMUM MEMORY USAGE: 120 queue elements
ALGORITHM USED: Breadth-First Search
```

For Dijkstra:

```
COST: 521
```

## Author

Francesco Pio Vitiello,
Luigi Mercurio,
Mario Sorrentino
