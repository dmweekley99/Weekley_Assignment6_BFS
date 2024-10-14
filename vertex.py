class Vertex:
    def __init__(self, index):  # Initialize a vertex with an index and a visited status
        self.visited = False  # Indicates whether the vertex has been visited
        self.index = index    # The unique index of the vertex

    def get_visited(self):
        """Returns the visited status of the vertex."""
        return self.visited

    def get_index(self):
        """Returns the index of the vertex."""
        return self.index
    
    def set_visited(self, visited):
        """Sets the visited status of the vertex."""
        self.visited = visited  # Update the visited status
        