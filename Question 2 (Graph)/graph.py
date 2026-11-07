class Graph:

    def __init__(self):
        self.vertices = {}

    # Add a new vertex
    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    # Add a directed edge
    def addEdge(self, source, destination):
        if source in self.vertices and destination in self.vertices:
            if destination not in self.vertices[source]:
                self.vertices[source].append(destination)
                return True

        return False

    # Remove a directed edge
    def removeEdge(self, source, destination):
        if source in self.vertices and destination in self.vertices[source]:
            self.vertices[source].remove(destination)
            return True

        return False

    # List all incoming adjacent vertices
    def listIncomingAdjacentVertex(self, vertex):

        incoming_vertices = []

        for source in self.vertices:
            if vertex in self.vertices[source]:
                incoming_vertices.append(source)

        return incoming_vertices

    # List all outgoing adjacent vertices
    def listOutgoingAdjacentVertex(self, vertex):

        if vertex in self.vertices:
            return self.vertices[vertex]

        return []