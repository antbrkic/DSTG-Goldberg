
"""
Ovo je implementacija Bellman Forda koja uzima najkraće trajanje putovanja između gradova kao težinu. 
Nažalost ovo rješenje ne predstavlja pravi problem jer je ovo idealna situacija, slično kao putovanje
osobnim automobilom.
Problem s pronalaskom Hamiltonove ture  nema efikasan algoritam za rješavanje.
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
        'Pozega': {"Karlovac": 36180, "Koprivnica": 22440,"Zagreb":9900},
        'Cakovec': {"Karlovac": 12060, "Koprivnica": 3660, "Varazdin": 600, "Zagreb": 8700},
        'Karlovac': {"Cakovec":  13020, "Koprivnica": 7740, "Varazdin": 79440, "Zagreb":8700},
        'Koprivnica': {"Cakovec": 3180},
        'Varazdin': {"Cakovec": 600, "Karlovac": 9300, "Zagreb": 4800},
        'Zagreb':{"Cakovec": 6900, "Karlovac": 2040, "Varazdin": 4500}
    }
    d, p = bellman_ford(graf, 'Pozega')

    for city in townList:
        for destination in d:
            if city in destination and city!="Pozega":
                minutes = d[destination]/60
                print("Najkraći put do " + city + " bi u idealnim uvjetima trajao " + str(minutes) + " minuta")

    for city in townList:
        for predecessorCity in p:
            if city in predecessorCity and city!="Pozega":
                print("Do " + city + " se moze doci preko " + str(p[predecessorCity]))

if __name__ == '__main__': main()