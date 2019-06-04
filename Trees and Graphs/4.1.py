# Route Between Nodes
from collections import deque


# BFS solution, O(V + E)
def route_between_nodes(graph, S, E):
    if not graph or S is None or E is None:
        raise Exception("The graph is empty or S and E are none, please enter a valid"
                        "graph along with valid start and end nodes.")

    queue = deque()
    visited = set()
    queue.append(S)

    while queue:
        node = queue.popleft()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if neighbor == E:
                    return True
                visited.add(neighbor)
                queue.append(neighbor)

    return False


# S - 1, E - 7
# contains route
graph_1 = {
    1: [2, 3],
    2: [],
    3: [4, 5],
    4: [6],
    5: [6],
    6: [7],
    7: []
}

# does not contain route
graph_2 = {
    1: [2, 3],
    2: [4],
    3: [4, 6],
    4: [5],
    5: [],
    6: [],
    7: [8],
    8: [9],
    9: [7]
}

# empty graph
graph_3 = {}

if __name__ == "__main__":
    print(route_between_nodes(graph_1, 1, 7))
    print(route_between_nodes(graph_2, 1, 7))
    print(route_between_nodes(graph_3, 1, 7))
