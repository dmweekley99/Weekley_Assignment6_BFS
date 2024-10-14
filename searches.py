from MUQueue import MUQueue

class Searches():
    queue = MUQueue() # initialize queue
    
    def BFS(self, nodes, adjacency, n, start):
        self.queue.enqueue(nodes[start]) # enqueue starting node
        nodes[start].set_visited(True) # set visited as true in starting node

        while self.queue.size() != 0:  # While the queue is not empty
            to_visit = self.queue.dequeue().get_index()  # Get the index of the node to visit
            print(f"Visiting node {to_visit}")  # Print the visited node

            # Check all adjacent nodes
            for j in range(n):
                if adjacency[to_visit][j] and not nodes[j].get_visited():  # Check adjacency and visited status
                    self.queue.enqueue(nodes[j])  # Enqueue the unvisited adjacent node
                    nodes[j].set_visited(True)  # Mark it as visited
