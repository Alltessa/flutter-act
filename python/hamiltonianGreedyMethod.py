vertices = ["Home", "Post Office", "Grocery Store", "Video Rental Store", "Bank"]

graph = [
    [0, 14, 12, 20, 23], #home
    [14, 0, 8, 12, 21], #Post Office
    [12, 8, 0, 17, 11], #Grocery Store
    [20, 12, 17, 0, 18], #Video Rental
    [23, 21, 11, 18, 0] #Bank
]

def hamiltonian(start):
    n = len(graph)
    visited_vertex = [False] * n
    path = [start]
    totalTime = 0
    current = start
    visited_vertex[current] = True

    for _ in range(n-1):
        next_vertex = None
        minDistance = float('inf')

        for i in range(n):
            if not visited_vertex[i] and 0 < graph[current][i] < minDistance:
                minDistance = graph[current][i]
                next_vertex = i

        if next_vertex is not None:
            visited_vertex[next_vertex] = True
            path.append(next_vertex)
            totalTime += minDistance
            current = next_vertex
    
    totalTime += graph[current][start]
    path.append(start)

    return path, totalTime

if __name__ == "__main__":
    route, totalTime = hamiltonian(0)

    print("The Hamiltonian Circuit is:")
    for i in range(len(route)):
        print(vertices[route[i]], end="")
        if i != len(route) - 1:
            print(" -> ", end="")
    print()

    print("The weight of the circuit is:")
    for i in range(len(route) - 1):
        u = route[i]
        v = route[i + 1]
        print(graph[u][v], end="")
        if i != len(route) - 2:
            print(" + ", end="")
    print(" =", totalTime)

    