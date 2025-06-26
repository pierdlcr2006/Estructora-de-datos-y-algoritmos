# Lista donde se guardarán los resultados de las pruebas
test_results = []

# Función para registrar si una prueba pasó o no
def record_test(test_name, condition):
    # Muestra un ✅ si la condición es verdadera, ❌ si es falsa
    emoji = "[OK]" if condition else "[FAIL]"
    # Agrega el resultado a la lista de pruebas
    test_results.append(f"{emoji} {test_name}")

# Clase que representa un grafo
class Graph:
    # Constructor del grafo
    def __init__(self):
        # Se crea una lista de adyacencia como un diccionario vacío
        self.adjacency_list = {}

    # Método para agregar un vértice
    def add_vertex(self, vertex):
        # Si el vértice no existe aún, lo agrega con una lista vacía
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    # Método que devuelve todos los vértices del grafo
    def get_vertices(self):
        # Se devuelven las claves del diccionario como lista
        return list(self.adjacency_list.keys())

    # Método que devuelve la cantidad total de vértices
    def get_vertex_count(self):
        # El número de claves en el diccionario es igual al número de vértices
        return len(self.adjacency_list)

    # Método para verificar si un vértice existe
    def has_vertex(self, vertex):
        # Retorna True si el vértice está en la lista de adyacencia
        return vertex in self.adjacency_list

# Función que realiza las pruebas del Challenge 2
def test_1_2():
    # Crea un grafo nuevo
    graph = Graph()

    # Prueba 1: Agrega un vértice
    graph.add_vertex("Lima")
    record_test("1.2.1 Single vertex addition", graph.has_vertex("Lima"))

    # Prueba 2: Agrega múltiples vértices
    graph.add_vertex("Cusco")
    graph.add_vertex("Arequipa")
    record_test("1.2.2 Multiple vertex addition", graph.get_vertex_count() == 3)

    # Prueba 3: Previene duplicados
    initial_count = graph.get_vertex_count()
    graph.add_vertex("Lima")  # Este ya existe
    record_test("1.2.3 Duplicate prevention", graph.get_vertex_count() == initial_count)

    # Prueba 4: El vértice agregado está aislado
    lima_neighbors = graph.adjacency_list.get("Lima", [])
    record_test("1.2.4 Vertex isolation", len(lima_neighbors) == 0)

    # Prueba 5: Se actualiza el conteo de vértices
    graph.add_vertex("Trujillo")
    record_test("1.2.5 Graph size tracking", "Trujillo" in graph.get_vertices())

# Ejecuta las pruebas
test_1_2()

# Imprime el resumen de resultados
for r in test_results:
    print(r)