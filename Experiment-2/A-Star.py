import heapq

def astar(graph, h, start, goal):
    queue = [(h[start], 0, start, [])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]

        if node == goal:
            return path, cost

        for next_node, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            new_f = new_cost + h[next_node]
            heapq.heappush(queue, (new_f, new_cost, next_node, path))

    return None, float('inf')


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 2)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}


h = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 2, 'F': 1, 'G': 0}


print("         A")
print("      1 / \\ 3")
print("       B   C")
print("     3/ \\1  \\2")
print("     D   E   F")
print("    2 \\ 3\\  /1")
print("       \\  \\/")
print("        \\ /")
print("         G")
print()

path, cost = astar(graph, h, 'A', 'G')

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)
