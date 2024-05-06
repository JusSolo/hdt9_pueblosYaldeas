import networkx as nx

import matplotlib.pyplot as plt
from tabulate import tabulate

def imprimir_diccionario(d1,d2):
    headers = ['Ciudad', 'Distancia minima','ciudad anterior']
    tabla = [[clave, valor] for clave, valor in d1.items()]
    for i in range(len(tabla)):
    	tabla[i].append(d2[tabla[i][0]])
    tabla_formateada = tabulate(tabla, headers=headers, tablefmt='fancy_grid')
    print(tabla_formateada)

# cargar la info necesaria para crear los grafos
def leo(nombre_archivo):
	nodos = {}
	aristas = []
	distancias = []
	G = nx.Graph()
	with open(nombre_archivo, 'r') as archivo:
		for linea in archivo:
			partes = linea.strip().split(", ")
			G.add_node(partes[0][1:-1])  
			G.add_node(partes[1][1:-1])  
			G.add_edge(partes[0][1:-1], partes[1][1:-1], weight = (int(partes[2])))
	return G
    

	
def printG (G):
	
	options = {
		 "font_size": 6,
		 "node_size": 3000,
		 "node_color": "white",
		 "edgecolors": "black",
		 "linewidths": 5,
		 "width": 5,
	}

	pos = nx.spring_layout(G)
	node_labels = {node: str(node) for node in G.nodes()}

	nx.draw(G, pos, with_labels=True, labels=node_labels, **options)
	plt.show()
	
def dijkstra(G, nodo_inicial):
    
    nodos_no_visitados = set(G.nodes())
    distancia = {nodo: float('inf') for nodo in G.nodes()}
    nodo_anterior = {nodo: None for nodo in G.nodes()}
    distancia[nodo_inicial] = 0
    
    while nodos_no_visitados:
       
        nodo_actual = None
        for nodo in nodos_no_visitados:
            if nodo_actual is None or distancia[nodo] < distancia[nodo_actual]:
                nodo_actual = nodo
        
       
        if nodo_actual is None:
            break
        
        
        nodos_no_visitados.remove(nodo_actual)
        
       
        for vecino in G.neighbors(nodo_actual):
            peso = G[nodo_actual][vecino]['weight']
            distancia_potencial = distancia[nodo_actual] + peso
            if distancia_potencial < distancia[vecino]:
                distancia[vecino] = distancia_potencial
                nodo_anterior[vecino] = nodo_actual
    print(nodo_anterior)
    return distancia , nodo_anterior
	




