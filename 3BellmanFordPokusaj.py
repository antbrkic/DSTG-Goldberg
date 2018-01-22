import time
import datetime
from datetime import timedelta

"""
Ovo je implementacija Bellman Forda koja uzima najkraće vrijeme dolaska u određene gradove, ali Bellman ford ne 
konstruira Hamiltonov put što od nas zadatak zapravo i traži. Taj problem nema efikasan algoritam za rješavanje.
Težine su zadane u sekundama a predstavljaju vremena dolaska u drugi grad. Ovdje se u obzir ne uzima cijeli raspored
vožnje vlakova i autobusa već samo 
"""

def initialize(graph, source):
    destination = {}
    predecessor = {}
    for node in graph:
        destination[node] = float('Inf')
        predecessor[node] = None
    destination[source] = 0
    return destination, predecessor

def relax(node, neighbour, graph, d, p):
    if d[neighbour] > d[node] + graph[node][neighbour]:
        d[neighbour] = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    destination, predecessor = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, destination, predecessor)

    #Provjera negativnih ciklusa
    for u in graph:
        for v in graph[u]:
            assert destination[v] <= destination[u] + graph[u][v]

    return destination, predecessor

def main():

    graf = {
        'Pozega': {"Karlovac": 63900, "Koprivnica": 55320 ,"Zagreb":33780},
        'Cakovec': {"Karlovac": 63900, "Koprivnica": 60780, "Varazdin": 69450, "Zagreb": 63660},
        'Karlovac': {"Cakovec":  68400, "Koprivnica": 72840, "Varazdin": 79440, "Zagreb":73080},
        'Koprivnica': {"Cakovec": 53100 },
        'Varazdin': {"Cakovec":39000, "Karlovac": 38760 , "Zagreb": 67320},
        'Zagreb':{"Cakovec": 64500, "Karlovac":32640, "Varazdin": 42000 }
    }
    d, p = bellman_ford(graf, 'Pozega')
    print("vremena dolaska u gradove izražena su u sekundama")
    print(d)
    print(p)

if __name__ == '__main__': main()