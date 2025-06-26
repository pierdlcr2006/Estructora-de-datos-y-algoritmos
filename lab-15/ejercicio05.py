# Definimos la clase que representa el grafo
class Graph:
    # Constructor: crea el grafo vacío
    def __init__(self):
        self.adjacency_list = {}

    # Agrega un vértice si no existe
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    # Agrega una arista entre dos vértices (conexión bidireccional)
    def add_edge(self, v1, v2):
        # Se aseguran que ambos vértices existan
        self.add_vertex(v1)
        self.add_vertex(v2)
        # Agrega v2 a la lista de v1 si no estaba
        if v2 not in self.adjacency_list[v1]:
            self.adjacency_list[v1].append(v2)
        # Agrega v1 a la lista de v2 si no estaba
        if v1 not in self.adjacency_list[v2]:
            self.adjacency_list[v2].append(v1)

    # Devuelve el número de conexiones (grado) de un vértice
    def get_degree(self, vertex):
        return len(self.adjacency_list.get(vertex, []))

    # Encuentra todos los caminos posibles entre dos vértices (opcionalmente limitados por longitud)
    def find_all_paths(self, start, end, max_length=None):
        # Función auxiliar DFS recursiva
        def dfs(current, path):
            # Si supera la longitud máxima, termina la búsqueda
            if max_length is not None and len(path) > max_length:
                return
            # Si llegó al destino, guarda el camino encontrado
            if current == end:
                paths.append(list(path))
                return
            # Recorre vecinos no visitados
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in path:
                    path.append(neighbor)
                    dfs(neighbor, path)
                    path.pop()  # Retrocede (backtracking)

        paths = []  # Lista de caminos encontrados
        # Verifica que los nodos existan
        if start in self.adjacency_list and end in self.adjacency_list:
            dfs(start, [start])  # Inicia la búsqueda desde el nodo inicial
        return paths

    # Encuentra todos los componentes conectados del grafo
    def get_connected_components(self):
        visited = set()      # Conjunto de nodos ya visitados
        components = []      # Lista de componentes encontrados

        # DFS para recorrer componentes
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        # Se recorre cada vértice del grafo
        for vertex in self.adjacency_list:
            if vertex not in visited:
                component = []
                dfs(vertex, component)  # Inicia DFS para nuevo componente
                components.append(component)  # Se agrega el componente completo

        return components

# Sección de pruebas
test_results = []

# Registra los resultados de las pruebas
def record_test(name, cond):
    emoji = "[OK]" if cond else "[FAIL]"
    test_results.append(f"{emoji} {name}")

# Función que ejecuta las pruebas del Challenge 5
def test_1_5():
    graph = Graph()

    # Construye el grafo de prueba
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Lima", "Arequipa")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_edge("Trujillo", "Piura")  # Otro componente

    # Prueba 1: Grado del nodo "Lima"
    record_test("1.5.1 Degree calculation", graph.get_degree("Lima") == 2)

    # Prueba 2: Múltiples caminos entre Lima y Arequipa
    paths = graph.find_all_paths("Lima", "Arequipa", max_length=3)
    record_test("1.5.2 Multiple paths finding", len(paths) >= 2)

    # Prueba 3: Detectar componentes conectados
    comps = graph.get_connected_components()
    record_test("1.5.3 Connected components", len(comps) == 2)

    # Prueba 4: Grafo vacío retorna lista vacía
    empty = Graph()
    record_test("1.5.4 Empty graph analysis", empty.get_connected_components() == [])

    # Prueba 5: Nodo inexistente retorna grado 0
    record_test("1.5.5 Non-existent vertex handling", graph.get_degree("Nada") == 0)

    # Imprime los resultados
    for r in test_results:
        print(r)

# Ejecuta las pruebas
test_1_5()
