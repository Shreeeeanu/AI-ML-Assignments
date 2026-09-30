from collections import deque

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['G'],
    'F':[],
    'G':[]
}

# ---- Show graph structure ----
print("         A")
print("        / \\")
print("       B   C")
print("      / \\   \\")
print("     D   E   F")
print("          \\")
print("           G")
print()

def bfs(graph, start):
  visited=[]
  queue=deque()

  visited.append(start)
  queue.append(start)

  while queue:
    node=queue.popleft()
    print(node,end=" ")

    for neighbour in graph[node]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

  return visited

start=input("Enter start node: ").upper()
bfs(graph, start)
print()


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# ---- Show graph structure ----
print("         A")
print("        / \\")
print("       B   C")
print("      / \\   \\")
print("     D   E   F")
print("          \\")
print("           G")
print()

def dfs(graph, start):
    visited = []
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            print(node, end=" ")


            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

    return visited

start = input("Enter start node: ").upper()
dfs(graph, start)
print()
