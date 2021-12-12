class Graph:
    class Vertex:
        def __init__(self, id, large=False):
            self.id = id
            self.large = large
            self.neighbors = {}

    def __init__(self):
        self.vertices = {}

    def connect(self, v1, v2):
        if self.vertices.get(v1, None) is None:
            self.vertices[v1] = Graph.Vertex(v1, large=(v1 != v1.casefold()))
        if self.vertices.get(v2, None) is None:
            self.vertices[v2] = Graph.Vertex(v2, large=(v2 != v2.casefold()))

        self.vertices[v1].neighbors[v2] = self.vertices[v2]
        self.vertices[v2].neighbors[v1] = self.vertices[v1]

def dfs(current="start", visited=()):
    if current == "end":
        return 1

    result = 0
    current = graph.vertices[current]
    if not current.large:
        visited += (current.id,)
    for next in current.neighbors:
        if next not in visited:
            result += dfs(next, visited)

    return result

with open("12in.txt", "r") as file:
    graph = Graph()
    for line in file:
        v1, v2 = line.strip("\n").split("-")
        graph.connect(v1, v2)
    print(dfs(visited=()))
