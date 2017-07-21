import random

graph = {}

with open('kargerMinCut.txt', 'r') as f:
    for line in f:
        line = line.rstrip().split('\t')
        graph[line[0]] = line[1:]


# print(graph)
random_node = random.choice(list(graph.keys()))
edges = [edge for node_edges in list(graph.values()) for edge in node_edges]
random_edge = random.choice(edges)
graph_items = list(graph.items())

print(random_edge)
print([item for item in graph_items if random_edge in item[1]])


# print([for edges in ])
# print("Random node: " + random_node)
# print(graph[random_node])


