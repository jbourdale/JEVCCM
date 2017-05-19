import heapq

def shorter_way(depart, goal):
    closedList = PriorityQueue()
    openList = PriorityQueue()
    openList.put(depart)
    while not openList.empty():
        currentCase = openList.get()
        #Si on est sur goal on arrete
        if currentCase == goal:
            return "YOLO ON A TROUV2"
        #Sinon on check tous les voisins
        voisin = currentCase.getVoisin()

        for currentVoisin in voisin:#si on l'a pour moins chère on pass
            if(closedList.has_and_cheaper(currentVoisin, currentCase +1) or closedList.has_and_cheaper(currentVoisin,currentCase+1)):
                continue
            else:#currentVoisin.parent = currentCase
                currentVoisin.setCost(currentCase.cost+1)
                currentVoisin.heuristique = compute_heuristique(currentVoisin, goal)
                openList.add(currentVoisin)
        closedList.put(currentCase.heuristique,currentCase)
    return "ERROR"


def compute_heuristique(currentCase, goal):
    return currentCase.cost + currentCase.distance(goal)
        

class MyPriorityQueue:
    def __init__(self):
        self.elements = []

    def put(self,case_to_put):
        heapq.heappush(self.elements,(case_to_put.heuristique,case_to_put))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def has_and_cheaper(currentCase, currentCost):
        for (prio,case) in elements:
            if(case == currentCase):
                return prio < currentCost
        return False

class Case:#ONLY FOR TESTING PURPOSE
    def __init__(self, x,y):
        self.x=x
        self.y=y
        self.cost=None
        self.heuristique=None

