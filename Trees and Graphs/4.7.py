# Build Order
from collections import defaultdict


# Time - O(P + D)
def build_order(projects, dependencies):
    if not projects:
        raise Exception("Please enter a valid list of projects")

    graph = defaultdict(list)
    for pair in dependencies:   # Builds the graph from the list of dependencies
        graph[pair[0]].append(pair[1])

    projs_clone = projects

    order = []
    edge_queue = set()
    for node in graph:
        for edge in graph[node]:
            edge_queue.add(edge)

    while projs_clone:
        to_be_processed = []
        for node in projs_clone:
            if node not in edge_queue:
                to_be_processed.append(node)
                order.append(node)
                projs_clone.remove(node)

        if not to_be_processed:
            raise Exception("A build order could not be found for these projects.")

        for node in to_be_processed:
            for edge in graph[node]:
                if edge in edge_queue:
                    edge_queue.remove(edge)

    return order


if __name__ == '__main__':
    # Build order
    projs_1 = ['a', 'b', 'c', 'd', 'e', 'f']
    deps_1 = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    print(build_order(projs_1, deps_1))

    # No build order
    projs_2 = ['a', 'b', 'c']
    deps_2 = [('a', 'b'), ('b', 'c'), ('c', 'a')]

    print(build_order(projs_2, deps_2))

    # Empty projects
    projs_3 = []
    deps_3 = []

    print(build_order(projs_3, deps_3))
