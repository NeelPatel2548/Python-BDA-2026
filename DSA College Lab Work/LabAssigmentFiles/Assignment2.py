
import math
from collections import deque

vertices = ['A', 'B', 'C', 'D', 'E', 'F']

edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2),
    ('D', 'F', 6),
    ('E', 'F', 3)
]

adj = {v: [] for v in vertices}

matrix = [[math.inf for j in vertices] for i in vertices]

for i in range(len(vertices)):
    matrix[i][i] = 0

for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

    i = vertices.index(u)
    j = vertices.index(v)

    matrix[i][j] = w
    matrix[j][i] = w

for v in vertices:
    adj[v].sort()


# (A) DISPLAY GRAPH

def displayList():
    print("\nADJACENCY LIST")
    for v in vertices:
        print(v, ":", adj[v])


def displayMatrix():
    print("\nWEIGHTED ADJACENCY MATRIX")

    print("    ", end="")
    for v in vertices:
        print(v, end="   ")
    print()

    for i in range(len(vertices)):
        print(vertices[i], end="   ")

        for j in range(len(vertices)):
            if matrix[i][j] == math.inf:
                print("∞", end="   ")
            else:
                print(matrix[i][j], end="   ")

        print()


# (B) BFS

def BFS(start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbour, weight in adj[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print("BFS Traversal:", order)


# (C) DFS

def DFS(start):
    visited = set()
    order = []

    def dfsVisit(current):
        visited.add(current)
        order.append(current)

        for neighbour, weight in adj[current]:
            if neighbour not in visited:
                dfsVisit(neighbour)

    dfsVisit(start)

    print("DFS Traversal:", order)


# (D) DIJKSTRA

def dijkstra(start):
    distance = {v: math.inf for v in vertices}
    predecessor = {v: None for v in vertices}
    visited = set()

    distance[start] = 0

    print("\nDIJKSTRA FINALIZATION")

    while len(visited) < len(vertices):

        current = None
        minimum = math.inf

        for v in vertices:
            if v not in visited and distance[v] < minimum:
                minimum = distance[v]
                current = v

        if current is None:
            break

        visited.add(current)

        print(current, "Distance:", distance[current],
              "Predecessor:", predecessor[current])

        for neighbour, weight in adj[current]:
            if neighbour not in visited:
                newDistance = distance[current] + weight

                if newDistance < distance[neighbour]:
                    distance[neighbour] = newDistance
                    predecessor[neighbour] = current

    return distance, predecessor


# (E) SHORTEST PATH

def shortestPath():
    start = input("Enter source vertex: ").upper()
    destination = input("Enter destination vertex: ").upper()

    if start not in vertices or destination not in vertices:
        print("Invalid vertex")
        return

    distance, predecessor = dijkstra(start)

    if distance[destination] == math.inf:
        print("No path exists")
        return

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = predecessor[current]

    path.reverse()

    print("\nShortest Path:", path)
    print("Total Cost:", distance[destination])


# MAIN MENU

while True:

    print("\n========== GRAPH MENU ==========")
    print("1. Display Adjacency List")
    print("2. Display Weighted Adjacency Matrix")
    print("3. Breadth First Search (BFS)")
    print("4. Depth First Search (DFS)")
    print("5. Dijkstra's Algorithm")
    print("6. Find Shortest Path")
    print("7. Display Time Complexities")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        displayList()

    elif choice == 2:
        displayMatrix()

    elif choice == 3:
        start = input("Enter starting vertex: ").upper()
        if start in vertices:
            BFS(start)
        else:
            print("Invalid vertex")

    elif choice == 4:
        start = input("Enter starting vertex: ").upper()
        if start in vertices:
            DFS(start)
        else:
            print("Invalid vertex")

    elif choice == 5:
        start = input("Enter starting vertex: ").upper()
        if start in vertices:
            dijkstra(start)
        else:
            print("Invalid vertex")

    elif choice == 6:
        shortestPath()

    elif choice == 7:
        print("BFS: O(V + E)")
        print("DFS: O(V + E)")
        print("Dijkstra: O(V^2 + E)")

    elif choice == 0:
        print("Program terminated.")
        break

    else:
        print("Invalid choice")
