def dfs(graph, source):
    global visited

    visited[source] = True

    print(source, end="  ")
    for i in graph[source]:
        if not visited[i]:
            dfs(graph, i)

graph = [[1, 2], [0, 2, 3], [0, 1, 4], [1, 4], [2,3]]
visited = len(graph)*[False]
dfs(graph, 0)