# Lista para almacenar los resultados de cada prueba
test_results = []

# Función para registrar el resultado de una prueba con emoji (✅ o ❌)
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"  # Selecciona el emoji según si la condición es verdadera o falsa
    test_results.append(f"{emoji} {test_name}")  # Agrega el resultado a la lista

# Clase que representa un grafo no dirigido usando una lista de adyacencia
class Graph:
    def __init__(self):
        self.adjacency_list = {}  # Diccionario que representa la lista de adyacencia

    # Agrega un vértice al grafo si no existe
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    # Agrega una arista bidireccional entre vertex1 y vertex2
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)  # Asegura que vertex1 exista
        self.add_vertex(vertex2)  # Asegura que vertex2 exista

        # Agrega vertex2 a los vecinos de vertex1 si no está duplicado
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)

        # Agrega vertex1 a los vecinos de vertex2 si no está duplicado
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    # Verifica si existe una arista entre vertex1 y vertex2
    def has_edge(self, vertex1, vertex2):
        return vertex1 in self.adjacency_list and vertex2 in self.adjacency_list[vertex1]

    # Devuelve la lista de vecinos de un vértice
    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])  # Retorna lista vacía si el vértice no existe

    # Verifica si un vértice existe en el grafo
    def has_vertex(self, vertex):
        return vertex in self.adjacency_list

# Función de pruebas automáticas para la funcionalidad del grafo
def test_1_3():
    graph = Graph()  # Crea una nueva instancia del grafo

    # 1.3.1 Crear arista básica entre Lima y Cusco
    graph.add_vertex("Lima")
    graph.add_vertex("Cusco")
    graph.add_edge("Lima", "Cusco")
    record_test("1.3.1 Basic edge creation", graph.has_edge("Lima", "Cusco"))

    # 1.3.2 Verifica conexión bidireccional (Cusco → Lima)
    record_test("1.3.2 Bidirectional connection", graph.has_edge("Cusco", "Lima"))

    # 1.3.3 Verifica creación automática de vértices al agregar una arista
    graph.add_edge("Arequipa", "Trujillo")
    has_both = graph.has_vertex("Arequipa") and graph.has_vertex("Trujillo")
    record_test("1.3.3 Auto vertex creation", has_both)

    # 1.3.4 Verifica que no se agreguen aristas duplicadas
    initial_neighbors = len(graph.get_neighbors("Lima"))
    graph.add_edge("Lima", "Cusco")  # Intento de duplicado
    final_neighbors = len(graph.get_neighbors("Lima"))
    record_test("1.3.4 Duplicate edge prevention", initial_neighbors == final_neighbors)

    # 1.3.5 Verifica que Cusco esté en los vecinos de Lima
    lima_neighbors = graph.get_neighbors("Lima")
    record_test("1.3.5 Connection verification", "Cusco" in lima_neighbors)

# Ejecuta las pruebas
test_1_3()

# Muestra los resultados
for r in test_results:
    print(r)