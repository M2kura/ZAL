class Vertex:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float('inf')
        self.previousVertex = None


class Edge:
    def __init__(self, source: int, target: int, weight: int):
        self.source = source
        self.target = target
        self.weight = weight


class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def computePath(self, sourceId):
        sourceVertex = next(vertex for vertex in self.vertexes if vertex.id == sourceId)
        sourceVertex.minDistance = 0
        unvisitedVertexes = set(self.vertexes)

        while unvisitedVertexes:
            currentVertex = min(unvisitedVertexes, key=lambda vertex: vertex.minDistance)

            unvisitedVertexes.remove(currentVertex)

            for edge in currentVertex.edges:
                neighborVertex = next(vertex for vertex in self.vertexes if vertex.id == edge.target)
                newDistance = currentVertex.minDistance + edge.weight

                if newDistance < neighborVertex.minDistance:
                    neighborVertex.minDistance = newDistance
                    neighborVertex.previousVertex = currentVertex

    def getShortestPathTo(self, targetId):
        targetVertex = next(vertex for vertex in self.vertexes if vertex.id == targetId)
        path = []
        currentVertex = targetVertex

        while currentVertex is not None:
            path.insert(0, currentVertex)
            currentVertex = currentVertex.previousVertex

        return path

    def createGraph(self, vertexes: list[Vertex], edgesToVertexes: list[Edge]):
        self.vertexes = vertexes

        for edge in edgesToVertexes:
            sourceVertex = next(vertex for vertex in self.vertexes if vertex.id == edge.source)
            targetVertex = next(vertex for vertex in self.vertexes if vertex.id == edge.target)
            sourceVertex.edges.append(edge)

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('inf')
            vertex.previousVertex = None

    def getVertexes(self):
        return self.vertexes
