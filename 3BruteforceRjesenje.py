"""
Ovo je implementacija rješenja ovog zadatka sirovom snagom. Broj različitih opcija može biti vidljiv iz ove tablice
koju nažalost nismo dobili u tekstualnom obliku pa smo je morali pretipkavati. Kod većeg broja gradova ovaj algoritam
bio bi krajnje neefikasan.
"""
import time
import datetime
from datetime import timedelta

listaVlakova = {
    "Pozega": {"Karlovac": ["0601 1745 1144 V",
                            "0742 1745 1003 V",
                            "0911 1745 3234 V",
                            "1321 1745 2824 V",
                            "1431 1745 2714 V",
                            "1719 1745 2426 V",
                            "1923 1745 2222 V",
                            "2024 1745 2121 V",
                            "2215 1745 1930 V"],
               "Koprivnica": ["0601 1522 0921 V",
                              "0742 1522 0740 V",
                              "0911 1935 1024 V",
                              "1321 1935 0614 V",
                              "1431 0429 1358 V",
                              "1719 0429 1110 V",
                              "1923 0429 0906 V",
                              "2024 1522 1858 V",
                              "2215 1522 1707 V"],
               "Zagreb": ["0555 0840 0245 B",
                          "0601 0923 0322 V",
                          "0742 1058 0316 V",
                          "0911 1220 0309 V",
                          "1000 1509 0509 V",
                          "1130 1400 0230 B",
                          "1321 1730 0409 V",
                          "1415 1715 0300 B",
                          "1431 1814 0343 V",
                          "1700 1945 0245 B",
                          "1719 2110 0351 V",
                          "1745 2030 0245 B",
                          "1923 0011 0448 V",
                          "2024 0011 0347 V",
                          "2215 0425 0610 V"]},
    "Cakovec": {"Karlovac": ["0456 0904 0408 V",
                             "0618 1046 0428 V",
                             "1004 1517 0513 V",
                             "1143 1555 0412 V",
                             "1218 1555 0337 V",
                             "1234 1555 0321 V",
                             "1401 1745 0344 V",
                             "1538 2049 0511 V",
                             "1732 2234 0502 V",
                             "1909 2330 0421 V",
                             "2027 0709 1042 V",
                             "2039 0709 1030 V",
                             "2158 0709 0911 V",
                             "2254 0709 0815 V"],
                "Koprivnica": ["0456 0607 0111 V",
                               "0618 0736 0118 V",
                               "0709 0840 0131 V",
                               "0849 1105 0216 V",
                               "1004 1105 0101 V",
                               "1030 1245 0215 B",
                               "1143 1348 0205 V",
                               "1218 1348 0130 V",
                               "1234 1348 0114 V",
                               "1320 1518 0158 V",
                               "1401 1518 0117 V",
                               "1538 1653 0115 V",
                               "1732 2008 0236 V",
                               "1909 2008 0059 V",
                               "2027 2259 0232 V",
                               "2039 2259 0220 V",
                               "2158 2259 0101 V",
                               "2254 0515 0621 V"],
                "Varazdin": ["0456 0506 0010 V",
                             "0505 0528 0023 B",
                             "0535 0600 0025 B",
                             "0618 0628 0010 V",
                             "0630 0655 0025 B",
                             "0709 0719 0010 V",
                             "0730 0755 0025 B",
                             "0820 0845 0025 B",
                             "0849 0859 0010 V",
                             "0930 0955 0025 B",
                             "1004 1014 0010 V",
                             "1130 1155 0025 B",
                             "1143 1153 0010 V",
                             "1218 1228 0010 V",
                             "1230 1255 0025 B",
                             "1300 1325 0025 B",
                             "1320 1330 0010 V",
                             "1325 1350 0025 B",
                             "1401 1411 0010 V",
                             "1415 1440 0025 B",
                             "1525 1550 0025 B",
                             "1538 1548 0010 V",
                             "1615 1640 0025 B",
                             "1730 1753 0023 B",
                             "1732 1742 0010 V",
                             "1909 1919 0010 V",
                             "2027 2037 0010 V",
                             "2039 2049 0010 V",
                             "2100 2125 0025 B",
                             "2158 2208 0010 V",
                             "2254 2304 0010 V"],
                "Zagreb": ["0456 0725 0229 V",
                           "0618 0935 0317 V",
                           "0709 0953 0244 V",
                           "1004 1321 0317 V",
                           "1143 1451 0308 V",
                           "1234 1518 0244 V",
                           "1400 1635 0235 B",
                           "1401 1741 0340 V",
                           "1538 1842 0304 V",
                           "1732 2015 0243 V",
                           "1909 2203 0254 V",
                           "1915 2140 0225 B",
                           "2027 0518 0851 V",
                           "2039 0518 0839 V",
                           "2158 0518 0720 V",
                           "2254 0518 0624 V"]},
    "Karlovac": {"Cakovec": ["0424 0846 0422 V",
                             "0504 1027 0523 V",
                             "0521 1027 0506 V",
                             "0608 1027 0419 V",
                             "0632 1257 0625 V",
                             "0848 1257 0409 V",
                             "0953 1445 0452 V",
                             "1136 1707 0531 V",
                             "1327 1707 0340 V",
                             "1409 1755 0346 V",
                             "1520 1900 0340 V",
                             "1728 0011 0643 V",
                             "1928 0011 0443 V",
                             "2034 0011 0337 V",
                             "2128 0703 0935 V"],
                 "Koprivnica": ["0424 0803 0339 V",
                                "0504 0803 0259 V",
                                "0521 0803 0242 V",
                                "0608 0857 0249 V",
                                "0848 1101 0213 V",
                                "0953 1251 0258 V",
                                "1136 1418 0242 V",
                                "1327 1618 0251 V",
                                "1409 1618 0209 V",
                                "1520 1747 0227 V",
                                "1728 2014 0246 V",
                                "1928 2212 0244 V",
                                "2034 0000 0326 V",
                                "2128 0000 0232 V"],
                 "Varazdin": ["0424 0831 0407 V",
                              "0504 0948 0444 V",
                              "0521 0948 0427 V",
                              "0608 1010 0402 V",
                              "0632 1140 0508 V",
                              "0754 1140 0346 V",
                              "0848 1208 0320 V",
                              "0953 1357 0404 V",
                              "1136 1557 0421 V",
                              "1327 1653 0326 V",
                              "1405 1635 0230 B",
                              "1409 1733 0324 V",
                              "1520 1937 0417 V",
                              "1728 2204 0436 V",
                              "1928 0000 0432 V",
                              "1930 2155 0225 B",
                              "2034 0000 0326 V",
                              "2110 2340 0230 B",
                              "2128 0056 0328 V"],
                 "Zagreb": ["0010 0105 0055 B",
                            "0445 0600 0115 B",
                            "0424 0514 0050 V",
                            "0504 0546 0042 V",
                            "0521 0614 0042 V",
                            "0608 0703 0055 V",
                            "0632 0730 0058 V",
                            "0754 0849 0055 V",
                            "0848 0930 0042 V",
                            "0953 1046 0053 V",
                            "1136 1230 0054 V",
                            "1327 1420 0053 V",
                            "1409 1445 0036 V",
                            "1520 1612 0052 V",
                            "1728 1825 0057 V",
                            "1928 2018 0050 V",
                            "2034 2115 0041 V",
                            "2128 2218 0050 V"]},
    "Koprivnica": {"Cakovec": ["0432 0532 0100 V",
                               "0543 0703 0120 V",
                               "0813 1027 0214 V",
                               "0903 1027 0124 V",
                               "1123 1257 0134 V",
                               "1303 1445 0142 V",
                               "1435 1532 0057 V",
                               "1542 1707 0125 V",
                               "1702 1755 0053 V",
                               "1800 1900 0100 V",
                               "1923 2022 0059 V"]},
    "Varazdin": {"Cakovec": ["0001 0011 0010 V",
                             "0440 0450 0010 V",
                             "0522 0532 0010 V",
                             "0653 0703 0010 V",
                             "0744 0754 0010 V",
                             "0836 0846 0010 V",
                             "1017 1027 0010 V",
                             "1040 1050 0010 V",
                             "1247 1257 0010 V",
                             "1305 1315 0010 V",
                             "1435 1445 0010 V",
                             "1522 1532 0010 V",
                             "1657 1707 0010 V",
                             "1745 1755 0010 V",
                             "1850 1900 0010 V",
                             "1922 1930 0010 V",
                             "2012 2022 0010 V",
                             "2120 2130 0010 V",
                             "2218 2228 0010 V"],
                 "Karlovac": ["0240 0709 0429 V",
                              "0328 0709 0341 V",
                              "0420 0904 0444 V",
                              "0524 0904 0340 V",
                              "0531 0904 0333 V",
                              "0646 1046 0400 V",
                              "0652 1046 0354 V",
                              "0930 1220 0250 B",
                              "1020 1404 0344 V",
                              "1042 1517 0435 V",
                              "1213 1555 0342 V",
                              "1303 1555 0252 V",
                              "1430 1745 0315 V",
                              "1600 2049 0449 V",
                              "1608 2049 0441 V",
                              "1746 2234 0448 V",
                              "1921 2330 0409 V",
                              "1924 2330 0406 V",
                              "2215 1745 1930 V"],
                 "Zagreb": ["0240 0518 0238 V",
                            "0328 0606 0238 V",
                            "0420 0729 0309 V",
                            "0524 0748 0224 V",
                            "0531 0725 0154 V",
                            "0646 0935 0249 V",
                            "0800 0945 0145 B",
                            "0850 1010 0120 B",
                            "0930 1055 0125 B",
                            "1042 1321 0239 V",
                            "1213 1451 0238 V",
                            "1414 1741 0327 V",
                            "1600 1842 0242 V",
                            "1746 2015 0229 V",
                            "1921 2203 0242 V"]},
    "Zagreb": {"Cakovec": ["0541 0846 0305 V",
                           "0730 1027 0257 V",
                           "0800 1024 0224 B",
                           "0930 1155 0225 B",
                           "1100 1325 0225 B",
                           "1300 1524 0224 B",
                           "1518 1755 0237 V",
                           "2125 0011 2046 V"],
               "Karlovac": ["0630 0709 0039 V",
                            "0636 0728 0052 V",
                            "0812 0904 0052 V"
                            "0952 1046 0054 V",
                            "1140 1231 0051 V",
                            "1314 1404 0050 V",
                            "1422 1517 0055 V",
                            "1521 1555 0034 V",
                            "1545 1639 0054 V",
                            "1631 1724 0053 V",
                            "1705 1745 0040 V",
                            "1714 1807 0053 V",
                            "1834 1927 0053 V",
                            "1951 2049 0058 V",
                            "2140 2234 0054 V",
                            "2237 2330 0053 V",
                            "2300 2338 0038 V"],
               "Koprivnica": [],
               "Varazdin": ["0541 0831 0250 V",
                            "0730 1010 0240 V",
                            "0859 1140 0241 V",
                            "1117 1357 0240 V",
                            "1309 1557 0248 V",
                            "1425 1653 0228 V",
                            "1518 1733 0215 V",
                            "1536 1842 0306 V",
                            "1538 1738 0200 V",
                            "1642 1937 0255 V",
                            "1812 2103 0251 V",
                            "1925 2204 0239 V",
                            "2125 0000 0235 V",
                            "2226 0056 0230 V"]}
}


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                # print(newpath)
                paths.append(newpath)
    return paths


def findEarliestArrival(gradPolaziste, gradOdrediste, trenutniSati, lista):
    listaDolazaka = []
    listaPolazaka = []
    for zapis in listaVlakova[gradPolaziste][gradOdrediste]:
        listaVremena = zapis.split()
        stringVrijemePolaska = listaVremena[0]
        stringVrijemeDolaska = listaVremena[1]

        satiVremenaPolaska = stringVrijemePolaska[:2]
        minuteVremenaPolaska = stringVrijemePolaska[2:]

        satiVremenaDolaska = stringVrijemeDolaska[:2]
        minuteVremenaDolaska = stringVrijemeDolaska[2:]

        vrijemePolaska = datetime.datetime(2018, 1, 1, int(satiVremenaPolaska), int(minuteVremenaPolaska), 0)
        vrijemeDolaska = datetime.datetime(2018, 1, 1, int(satiVremenaDolaska), int(minuteVremenaDolaska), 0)

        listaPolazaka.append(vrijemePolaska)
        listaDolazaka.append(vrijemeDolaska)

    brojac = 0
    pomocniBrojac = 0
    minimalnoVrijemeDolaska = listaDolazaka[0]
    for item in listaPolazaka:
        if (item > trenutniSati):
            for i in range(brojac, len(listaDolazaka)):
                flag = False
                if (listaDolazaka[i] < minimalnoVrijemeDolaska):
                    flag = True
                    minimalnoVrijemeDolaska = listaDolazaka[i]
                    if (flag):
                        pomocniBrojac = i
            #break
        else:
            brojac += 1

    lista.append(gradPolaziste + "->" + gradOdrediste + " " + str(listaPolazaka[pomocniBrojac]) + " " + str(
        listaDolazaka[pomocniBrojac]))
    trenutniSati = trenutniSati + timedelta(hours=6)
    return lista, trenutniSati


def main():
    townList = ["Pozega", "Cakovec", "Karlovac", "Koprivnica", "Varazdin", "Zagreb"]

    graf = {
        'Pozega': ["Karlovac", "Koprivnica", "Zagreb"],
        'Cakovec': ["Karlovac", "Koprivnica", "Varazdin", "Zagreb"],
        'Karlovac': ["Cakovec", "Koprivnica", "Varazdin", "Zagreb"],
        'Koprivnica': ["Cakovec"],
        'Varazdin': ["Cakovec", "Karlovac", "Zagreb"],
        'Zagreb': ["Cakovec", "Karlovac", "Varazdin"]
    }
    konacnaLista = []
    print("Prikaz svih puteva")
    for town in townList:
        if town != "Pozega":
            putanja = find_all_paths(graf, "Pozega", town)
            for path in putanja:
                if len(path) > 5:
                    trenutniSat = datetime.datetime(2018, 1, 1, 0, 0)
                    print(path)
                    for i in range(0, 4):
                        j = i + 1
                        konacnaLista, trenutniSat = findEarliestArrival(path[i], path[j], trenutniSat, konacnaLista)

    print(konacnaLista)
    # print("Gotova putanja")


if __name__ == '__main__': main()
