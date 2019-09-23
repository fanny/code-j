import sys

def get_node_with_min_distance(distances, visiteds):
    min_distance = sys.maxint
    min_index = 0

    for i in xrange(0, len(distances)):
        if distances[i] < min_distance and (not i in visiteds):
            min_index = i
            min_distance = distances[i]

    return min_index

def shortest_paths(node, graph):
    V = len(graph.keys())
    distances = [sys.maxint] * V
    distances[node] = 0
    visiteds = set()

    while(len(visiteds) != V):
        min_index = get_node_with_min_distance(distances, visiteds)
        visiteds.add(min_index)
        childs = graph[min_index]
        for child in childs:
            if(not child in visiteds):
                node, my_distance = child
                if(distances[node] > distances[min_index] + my_distance):
                    distances[node] = distances[min_index] + my_distance

    return distances

