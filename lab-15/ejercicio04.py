test_results = []

# Function to log the result of each test case with a checkmark or cross
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# Define the Graph class
class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list
        self.adjacency_list = {}
    
    # Add a vertex to the graph if it doesn't already exist
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    # Add an undirected edge between two vertices
    def add_edge(self, vertex1, vertex2):
        # Ensure both vertices exist in the graph
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        # Add vertex2 to vertex1's adjacency list if not already present
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        # Add vertex1 to vertex2's adjacency list (because the graph is undirected)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    # Find the shortest path between two vertices using BFS
    def find_path(self, start_vertex, end_vertex):
        # If either vertex does not exist, return an empty path
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            return []

        # If start and end vertices are the same, return a path with just that vertex
        if start_vertex == end_vertex:
            return [start_vertex]

        visited = set()  # Keep track of visited vertices
        queue = [(start_vertex, [start_vertex])]  # Store pairs of (current_vertex, path_so_far)

        # Perform BFS
        while queue:
            current, path = queue.pop(0)  # Dequeue the next vertex and path
            visited.add(current)  # Mark current vertex as visited

            # Iterate over neighbors of the current vertex
            for neighbor in self.adjacency_list[current]:
                # If neighbor is the target, return the full path
                if neighbor == end_vertex:
                    return path + [neighbor]    
                # If neighbor hasn't been visited, enqueue it with the updated path
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        # If no path is found, return empty list
        return []

    # Check if two vertices are connected (i.e., a path exists between them)
    def is_connected(self, vertex1, vertex2):
        # If the path length is greater than 0, the vertices are connected
        return len(self.find_path(vertex1, vertex2)) > 0

# Test function for challenge 4
def test_1_4():
    graph = Graph()
    
    # Create a graph: Lima - Cusco - Arequipa (Trujillo is disconnected)
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_vertex("Trujillo")  # Add isolated vertex

    # 1.4.1: Check direct connection path from Lima to Cusco
    path = graph.find_path("Lima", "Cusco")
    record_test("1.4.1 Direct connection path", path == ["Lima", "Cusco"])
    
    # 1.4.2: Check indirect path from Lima to Arequipa (through Cusco)
    path = graph.find_path("Lima", "Arequipa")
    is_valid_path = len(path) == 3 and path[0] == "Lima" and path[-1] == "Arequipa"
    record_test("1.4.2 Indirect connection path", is_valid_path)
    
    # 1.4.3: Check that no path exists between Lima and isolated Trujillo
    path = graph.find_path("Lima", "Trujillo")
    record_test("1.4.3 No path case", path == [])
    
    # 1.4.4: Check self path (Lima to Lima)
    path = graph.find_path("Lima", "Lima")
    record_test("1.4.4 Self path", path == ["Lima"])
    
    # 1.4.5: Check connectivity – Lima and Arequipa should be connected, but not Trujillo
    connected = graph.is_connected("Lima", "Arequipa")
    not_connected = graph.is_connected("Lima", "Trujillo")
    record_test("1.4.5 Connectivity check", connected and not not_connected)

# 🚀 Run all tests
test_1_4()

# 📋 Print test summary
for r in test_results:
    print(r)