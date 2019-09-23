graph = []

def find(node):
    if(graph[node] != node)
        return find(node)
    return node

def connected(first, second):
    return find(first) == find(second)

def union(first, second):
    first_parent = find(first)
    second_parent = find(second)

    if(first_parent != second_parent):
        graph[first_parent] = second_parent
