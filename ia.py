import heapq
import math

def shorter_way(depart, goal):
    closedList = PriorityQueue()
    openList = PriorityQueue()
    openList.put(depart)
    while not openList.empty():
        currentCase = openList.get()
        print('currentCase: '+currentCase)
        #Si on est sur goal on arrete
        if currentCase == goal:
            print("YOLO ON A TROUV2")
            return (corresponding_move(depart,first_destination(currentCase)), currentCase.cost)
        #Sinon on check tous les voisins
        voisin = currentCase.getVoisin()

        for currentVoisin in voisin:#si on l'a pour moins chere on pass
            if(closedList.has_and_cheaper(currentVoisin, currentCase +1) or closedList.has_and_cheaper(currentVoisin,currentCase+1)):
                print('already in queue: '+currentVoisin )
            else:
                currentVoisin.parent = currentCase
                currentVoisin.setCost(currentCase.cost+1)
                currentVoisin.heuristique = compute_heuristique(currentVoisin, goal)
                openList.add(currentVoisin)

        closedList.put(currentCase.heuristique,currentCase)
    return "C"

def corresponding_move(depart,destination):
    if depart.x<destination.x:
        return "E"
    elif depart.x>destination.x:
        return "O"
    elif depart.y<destination.y:
        return "S"
    else: 
        return "N"

def compute_heuristique(currentCase, goal):
    return currentCase.cost + currentCase.distance(goal)

#return the first move made        
def first_destination(currentCase):
    if currentCase.parent.parent==None:
        return currentCase
    else:
        return firstMove(currentCase.parent)

def shorter_way_2(depart, goal):
    closedList = PriorityQueue()
    openList = PriorityQueue()
    openList.put(depart)
    while not openList.empty():
        currentCase = openList.get()
        print('currentCase: '+currentCase)
        #Si on est sur goal on arrete
        if currentCase == goal:
            print("YOLO ON A TROUV2")
            return corresponding_move(depart,first_destination(currentCase))
        #Sinon on check tous les voisins
        voisin = Callai.getVoisin(currentCase)

        for currentVoisin in voisin:#si on l'a pour moins chere on pass
            if(closedList.has_and_cheaper(currentVoisin, currentCase +1) or closedList.has_and_cheaper(currentVoisin,currentCase+1)):
                print('already in queue: '+currentVoisin )
            else:
                currentVoisin.parent = currentCase
                currentVoisin.setCost(currentCase.cost+1)
                currentVoisin.heuristique = compute_heuristique(currentVoisin, goal)
                openList.add(currentVoisin)

        closedList.put(currentCase.heuristique,currentCase)
    return "C"

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
"""
class Case:#ONLY FOR TESTING PURPOSE
    def __init__(self, x,y):
        self.x=x
        self.y=y
        self.cost=None
        self.heuristique=None
        self.voisin = None
        self.id = None

    def __eq__(self, other):
        return self.x==other.x and self.y== other.y

    def distance(self,other):
        return sqrt(pow(case.x - case.x,2) + pow(case.y - self.y,2))

"""
def sortMoule(listeMoule):
    for i in range(len(listeMoule)):
        currentMoule = listeMoule[i]
        for j in range (len(listeMoule)):
            if currentMoule.nbrDePoints < listeMoule[j]:
                listeMoule[i] = listeMoule[j]
                listeMoule[j] = currentMoule
    return listMoule



#def find_goal(depart, listeMoule):
    #sort listMoule
def find_goal(depart,listeMoule,listeDepartOthers):
    listeMoule = sortMoule(listeMoule)
    for i in range (len(listeMoule)):
        mouleCourante = listeMoule[i]
        ok = True
        for departOther in listeDepartOthers:
            if (shorter_way(depart,mouleCourante)[1]>shorter_way(departOther,mouleCourante)[1]):
                ok = False
        if ok:
            return mouleCourante
    return listeMoule[0]
"""
class Callai () :
    def __init__(self,width, height) : 
        self.cases = Case[height][width]
        self.height = height
        self.width = width
        
        for y in height : 
            for x in width : 
                self.cases[y][x] = None


    def getCase(self,x,y) :
        return self.cases[y][x];

    def setCase(self,x,y,case) :
        self.cases[y][x] = case;

    @staticmethod
    def getVoisin(currentCase) : 
        casesPossibles = []
        if (type(cases[currentCase.y][currentCase.x+1]) != Dune) : 
            casesPossibles.append(cases[currentCase.y][currentCase.x+1])
        if (type(cases[currentCase.y][currentCase.x-1]) != Dune) : 
            casesPossibles.append(cases[currentCase.y][currentCase.x-1])
        if (type(cases[currentCase.y-1][currentCase.x]) != Dune) : 
            casesPossibles.append(cases[currentCase.y-1][currentCase.x])
        if (type(cases[currentCase.y+1][currentCase.x]) != Dune) : 
            casesPossibles.append(cases[currentCase.y+1][currentCase.x])

        return casesPossibles

"""