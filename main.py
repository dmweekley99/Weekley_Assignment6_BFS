from searches import Searches
from vertex import Vertex

def main():
    # Create an array of Vertex objects
    nodes = [Vertex(i) for i in range(10)]  # Create 10 Vertex objects

    # Define the adjacency matrix
    adjacency = [
        [False, True, False, True, False, False, False, False, False, False],
        [True, False, True, True, False, False, False, False, False, False],
        [False, True, False, True, False, True, False, False, False, False],
        [True, True, False, False, True, True, False, False, False, False],
        [False, False, False, True, False, False, True, False, False, False],
        [False, False, True, True, False, False, False, True, True, False],
        [False, False, False, False, True, False, False, True, False, False],
        [False, False, False, False, False, True, False, False, False, True],
        [False, False, False, False, False, True, False, True, False, False],
        [False, False, False, False, False, False, False, True, False, False]
    ]

    # Create an instance of Searches
    search = Searches()

    # Call the BFS method
    search.BFS(nodes, adjacency, len(nodes), 0)  # Starting from index 0

if __name__ == "__main__":
    main()