import time
import datetime
from datetime import timedelta

"""
Ovo je implementacija Bellman Forda koja uzima samo najnižu cijenu puta do određenih gradova.
Bellman Ford ne konstruira Hamiltonov put što od nas zadatak zapravo i traži. Taj problem nema efikasan algoritam za rješavanje.
Težine su zadane u sekundama a predstavljaju vremena dolaska u drugi grad. 
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
    townList=["Pozega","Cakovec","Karlovac","Koprivnica","Varazdin","Zagreb"]
    graf = {
        'Pozega': {"Karlovac": 160.90, "Koprivnica": 100.70 ,"Zagreb":100.70},
        'Cakovec': {"Karlovac": 87.90, "Koprivnica": 36.20, "Varazdin": 11.70, "Zagreb": 69.80},
        'Karlovac': {"Cakovec":  87.90, "Koprivnica": 77.50, "Varazdin": 84.10, "Zagreb": 36.20},
        'Koprivnica': {"Cakovec": 36.20},
        'Varazdin': {"Cakovec": 11.70, "Karlovac": 84.10, "Zagreb": 61.00},
        'Zagreb':{"Cakovec": 69.80, "Karlovac":36.20, "Varazdin": 61.00}
    }
    d, p = bellman_ford(graf, 'Pozega')

    for city in townList:
        for destination in d:
            if city in destination:
                print("Karta do " + city + " košta " + str(d[destination]))

    print(d)
    print(p)

if __name__ == '__main__': main()