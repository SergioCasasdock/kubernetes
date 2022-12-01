# Programa Python para el algoritmo de Kruskal para encontrar
 
 
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  
# Nº de vértices
        self.graph = []
        
# para almacenar grap
 
   
# función para agregar un borde al gráfico
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
   # Una función de utilidad para encontrar el conjunto de un elemento i
    # (realmente usa la técnica de compresión de ruta)
    def find(self, parent, i):
        if parent[i] != i:
         Reasignación del padre del nodo al nodo raíz como
          # requiere compresión de ruta
            parent[i] = self.find(parent, parent[i])
        return parent[i]
 
    # Una función que hace la unión de dos conjuntos de x e y
    # (usa unión por rango)
    def union(self, parent, rank, x, y):
        
        # Adjunte un árbol de clasificación más pequeño debajo de la raíz de
        # árbol de rango alto (Unión por rango)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
 
       # Si los rangos son los mismos, entonces haz uno como root
        # e incrementar su rango en uno
        else:
            parent[y] = x
            rank[x] += 1
 
    
        # algoritmoion to construct MST using Kruskal's
        # algorithm
    def KruskalMST(self):
 
        result = []  # Esto almacenará el MST resultante
 
        # Una variable de índice, utilizada para bordes ordenados
        i = 0
 
        # Una variable de índice, utilizada para result[]
        e = 0
 
        # Paso 1: ordenar todos los bordes en
        # orden no decreciente de sus
        # peso. Si no se nos permite cambiar el
        # gráfico dado, podemos crear una copia del gráfico
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Crear subconjuntos V con elementos individuales
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        # El número de aristas a tomar es igual a V-1
        while e < self.V - 1:
 
          # Paso 2: Elija el borde más pequeño e incremente
            # el índice para la próxima iteración
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
           # Si incluir este borde no
            # causa el ciclo, luego inclúyelo en el resultado
            # e incrementar el índice de resultado
            # para el borde siguiente
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # De lo contrario descartar el borde
        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)
 
 
# Código del conductor
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)
 
  
    g.KruskalMST()
