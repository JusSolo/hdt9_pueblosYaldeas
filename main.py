from funciones import*

G = leo('rutas.txt')
printG(G)

nodo = input('ingrese el nombre de el pueblo en el que se encuantra: ')

t , d = dijkstra(G, nodo)
print('Distancias minimas partiendo de', nodo + ':')
imprimir_diccionario(t,d)
