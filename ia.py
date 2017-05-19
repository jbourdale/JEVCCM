import heapq

def shorter_way(depart, goal):
    closedList = Queue(0)
    openList = PriorityQueue(0)
    openList.put(depart)
    while !openList.empty():
        currentCase = openList.get()
        #Si on est sur goal on arrete
        if currentCase == goal:
            return "YOLO ON A TROUV2"
        #Sinon on check tous les voisins
        voisin = []
        voisin.add(getCase(currentCase.x-1,currentCase.y))
        voisin.add(getCase(currentCase.x+1,currentCase.y))
        voisin.add(getCase(currentCase.x,currentCase.y-1))
        voisin.add(getCase(currentCase.x,currentCase.y+1))

        for currentVoisin in voisin:#si on l'a pour moins chère on pass
            if(openList.get_and_cheaper(currentVoisin) || closedList.get_and_cheaper(currentVoisin)):
                continue
            else:#currentVoisin.parent = currentCase
                currentVoisin.setCost(currentCase.cost+1)
                currentVoisin.heuristique = compute_heuristique(currentVoisin, goal)
                openList.add(currentVoisin)
        closedList.add(currentCase)
    return "ERROR"


def compute_heuristique(currentCase, goal):
    return currentCase.cost + currentCase.distance(goal)
        



