class Edge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, source, target, weight):
        if source < 0 or source >= self.vertices:
            raise ValueError("Source vertex is out of range")
        if target < 0 or target >= self.vertices:
            raise ValueError("Target vertex is out of range")
        if weight < 0:
            raise ValueError("Dijkstra's algorithm does not support negative weights")

        self.adjacency_list[source].append(Edge(target, weight))

    def dijkstra(self, start):
        if start < 0 or start >= self.vertices:
            raise ValueError("Start vertex is out of range")

        distances = [float("inf")] * self.vertices
        visited = [False] * self.vertices
        distances[start] = 0

        for _ in range(self.vertices):
            current = self._find_nearest_unvisited_vertex(distances, visited)

            if current == -1:
                break

            visited[current] = True

            for edge in self.adjacency_list[current]:
                if not visited[edge.target]:
                    new_distance = distances[current] + edge.weight
                    if new_distance < distances[edge.target]:
                        distances[edge.target] = new_distance

        self._print_distances(start, distances)

    def _find_nearest_unvisited_vertex(self, distances, visited):
        minimum_distance = float("inf")
        nearest_vertex = -1

        for vertex in range(self.vertices):
            if not visited[vertex] and distances[vertex] < minimum_distance:
                minimum_distance = distances[vertex]
                nearest_vertex = vertex

        return nearest_vertex

    def _print_distances(self, start, distances):
        print(f"Shortest distances from vertex {start}:")
        for vertex, distance in enumerate(distances):
            if distance == float("inf"):
                print(f"Vertex {vertex}: unreachable")
            else:
                print(f"Vertex {vertex}: {distance}")


def main():
    graph = Graph(6)

    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 2)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 10)
    graph.add_edge(2, 4, 3)
    graph.add_edge(4, 3, 4)
    graph.add_edge(3, 5, 11)

    graph.dijkstra(0)


if __name__ == "__main__":
    main()
