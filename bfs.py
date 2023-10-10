def bfs(graph, source):
    visited = len(graph) * [False]

    queue = []

    visited[source] = True
    queue.append(source)

    while (len(queue)):
        s = queue[0]
        print(s, end="  ")
        queue.remove(s)

        for i in graph[s]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


graph = [[1, 2], [0, 2, 3], [0, 1, 4], [1, 4], [2,3]]

bfs(graph, 0)