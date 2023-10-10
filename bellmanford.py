import sys

def bellman_ford(graph, src):
    dist = []
    previous = []

    v = len(graph)

    for i in range(v):
        dist.append(sys.maxsize)
        previous.append(None)

    dist[src] = 0

    for i in range(v-1):
        for j in range(v):
            for k in range(v):
                if (graph[j][k] != 0 and dist[j] < sys.maxsize and dist[j] + graph[j][k] < dist[k]):
                    dist[k] = dist[j] + graph[j][k]
                    previous[k] = j

    for i in range(v-1):
        for j in range(v):
            if (graph[i][j] != 0 and dist[i] < sys.maxsize and dist[i] + graph[i][j] < dist[j]):
                    print("There is a negative cycle in the graph")
                    previous[j] = i
                    get_cycle(previous, i, j)
                    print(previous)
                    return 0

    print("Distance of each vertex from the source is: ");
    print("Vertex\t\tDistance from Vertex")
    for i  in range(v):
        print(f"{i}\t\t{dist[i]}")

def get_cycle(previous, k, s):
    if k==s:
        print(k)
        return
    get_cycle(previous, previous[k], s)
    print(k)




# graph = [ [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ],
#                         [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ],
#                         [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ],
#                         [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ],
#                         [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ],
#                         [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ],
#                         [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ],
#                         [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ],
#                         [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] ]

# graph = [[0, 10, 0, 0, 0, 0, 0, 8],
#          [0, 0, 0, 0, 0, 2, 0, 0],
#          [0, 1, 0, 1, 0, 0, 0, 0],
#          [0, 0, 0, 0, 3, 0, 0, 0],
#          [0, 0, 0, 0, 0, -1, 0, 0],
#          [0, 0, -2, 0, 0, 0, 0, 0],
#          [0, -4, 0, 0, 0, -1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 1, 0]]

graph = [[0, 6, 0, 7, 0],
         [0, 0, 5, 8, -4],
         [0, -2, 0, 0, 0],
         [0, 0, -3, 0, 9],
         [2, 0, 4, 0, 0]]

# graph = [[0, 4, 0],
#          [0, 0, 5],
#          [-11, 0, 0]]


if __name__=="__main__":
    bellman_ford(graph, 0)