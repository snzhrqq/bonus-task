# Dijkstra's Shortest Path Algorithm

A Python implementation of Dijkstra's algorithm for finding shortest paths in a weighted directed graph.

---

## Overview

This project implements Dijkstra's algorithm using an adjacency list representation. Given a source vertex, it computes the minimum-cost path to every reachable vertex in the graph.

---

## Project Structure

```
.
├── bonus task.py   # Main source file
└── README.md
```

---

## Classes

### `Edge`

Represents a directed edge in the graph.

| Attribute | Type  | Description                  |
|-----------|-------|------------------------------|
| `target`  | `int` | Index of the destination vertex |
| `weight`  | `int` | Cost of traversing this edge |

---

### `Graph`

Represents a weighted directed graph via an adjacency list.

#### Constructor

```python
Graph(vertices: int)
```

| Parameter  | Type  | Description                    |
|------------|-------|--------------------------------|
| `vertices` | `int` | Total number of vertices (0-indexed) |

#### Methods

| Method | Description |
|--------|-------------|
| `add_edge(source, target, weight)` | Adds a directed edge from `source` to `target` with the given `weight`. Raises `ValueError` for out-of-range vertices or negative weights. |
| `dijkstra(start)` | Runs Dijkstra's algorithm from `start` and prints shortest distances to all vertices. |

---

## Algorithm

The implementation uses a simple **O(V²)** approach with a linear scan to find the nearest unvisited vertex at each step — suitable for dense graphs or educational use.

**Steps:**
1. Initialize all distances to `∞`, set `distance[start] = 0`.
2. Repeat `V` times:
   - Pick the unvisited vertex with the smallest known distance.
   - Mark it as visited.
   - Relax all outgoing edges from it.
3. Print the final distances.

> **Note:** Negative edge weights are not supported and will raise a `ValueError`.

---

## Example

The `main()` function builds the following graph and runs Dijkstra from vertex `0`:

```
0 --4--> 1
0 --2--> 2
1 --5--> 2
1 --10-> 3
2 --3--> 4
4 --4--> 3
3 --11-> 5
```

**Running the example:**

```bash
python dijkstra.py
```

**Expected output:**

```
Shortest distances from vertex 0:
Vertex 0: 0
Vertex 1: 4
Vertex 2: 2
Vertex 3: 9
Vertex 4: 5
Vertex 5: 20
```

**How the shortest paths are computed:**

| Destination | Path             | Cost |
|-------------|------------------|------|
| 0           | 0                | 0    |
| 1           | 0 → 1            | 4    |
| 2           | 0 → 2            | 2    |
| 3           | 0 → 2 → 4 → 3   | 9    |
| 4           | 0 → 2 → 4        | 5    |
| 5           | 0 → 2 → 4 → 3 → 5 | 20 |

---

## Error Handling

| Condition | Exception |
|-----------|-----------|
| Source or target vertex out of range | `ValueError` |
| Start vertex out of range | `ValueError` |
| Negative edge weight | `ValueError` |

---

## Requirements

- Python 3.6+
- No external dependencies

---

## Complexity

| | Complexity |
|---|---|
| Time | O(V²) |
| Space | O(V + E) |

Where **V** = number of vertices, **E** = number of edges.

For large sparse graphs, consider replacing the linear scan with a priority queue (`heapq`) to achieve **O((V + E) log V)**.

## Screenshots

<img width="1919" height="1079" alt="Screenshot 2026-05-21 191733" src="https://github.com/user-attachments/assets/007463a2-93a0-4400-8833-a9bc595e3b8d" />
<img width="1919" height="1072" alt="Screenshot 2026-05-21 191743" src="https://github.com/user-attachments/assets/ed78124c-70f2-4f3c-a5fe-5f746b3b5eec" />
<img width="1919" height="1079" alt="Screenshot 2026-05-21 191751" src="https://github.com/user-attachments/assets/71e1bdc9-bdd4-4408-a34a-34c7aa2e6b9e" />



