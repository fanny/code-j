
visiteds = [False] * 10e4

def dfs(node, graph):
    visiteds[node] = True
    for child in graph[node]:
        if(not visiteds[child])
            dfs(child)


