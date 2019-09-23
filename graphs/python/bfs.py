
def bfs(root, graph):
    V = len(graph.keys())
    visiteds = [False] * V
    queue = [root]
    
    while(len(queue) != 0):
        node = queue.pop(0)
        visiteds[node] = True
        for child in graph[node]:
            if(not visiteds[child]):
                queue.append(child)

            
