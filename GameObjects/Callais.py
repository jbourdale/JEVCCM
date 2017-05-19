class Case :
	def __init__(self, x,y) :
		self.x = x
		self.y = y

	def __eq__(self,case) :
		return self.x == case.x and self.y == case.y

	def distance(self,case) :
		return Math.sqrt(Math.pow(case.x - case.x,2) + Math.pow(case.y - self.y,2))

	def __str__(self):
		return 'Case ('+self.x+";"+self.y+")"




class Sable (Case) :
	def __init__(self, x,y):
		Case.__init__(self,x,y)

	def __str__(self):
		return 'Case ('+str(self.x)+";"+str(self.y)+") > Sable"

class Dune (Case) :
	def __init__(self, x,y):
		Case.__init__(self,x,y)

	def __str__(self):
		return 'Case ('+str(self.x)+";"+str(self.y)+") > Dune"


class Frite (Case):
	def __init__(self, x,y):
		Case.__init__(self,x,y)

	def __str__(self):
		return 'Case ('+str(self.x)+";"+str(self.y)+") > Frite"

class Moule (Case) :
	def __init__(self,nbrDePoints, x, y):
		Case.__init__(self,x,y)
		self.nbrDePoints = nbrDePoints

	def __str__(self):
		return 'Case ('+str(self.x)+";"+str(self.y)+") > Moule"

class Biere(Case):
	def __init__(self,x,y):
		Case.__init__(self,x,y)

	def __str__(self):
		return 'Case ('+str(self.x)+";"+str(self.y)+") > Biere"



class Player (Case) :
	def __init__ (self,nomEquipe) :
		self.nomEquipe = nomEquipe

	def setEquipe(self,nomEquipe):
		self.nomEquipe = nomEquipe;

	def getEquipe(self):
		return self.nomEquipe;



class Callais () :
	def __init__(self,width, height) :
		width = int(width)
		height = int(height)
		self.cases = [[Case(x,y) for x in range(height)] for y in range(width)]
		self.height = height
		self.width = width


	def getCase(self,x,y) :
		return self.cases[x][y];

	def setCase(self,x,y,case) :
		self.cases[y][x] = case;

	def donnerVoisins(self,case) :
		casesPossibles = []
		if (type(self.getCase(case.x - 1,case.y)) != Dune) :
			casesPossibles.append(self.getCase(case.x - 1,case.y))
		if (type(self.getCase(case.x ,case.y + 1)) != Dune) :
			casesPossibles.append(self.getCase(case.x,case.y + 1))
		if (type(self.getCase(case.x,case.y - 1)) != Dune) :
			casesPossibles.append(self.getCase(case.x,case.y - 1))
		if (type(self.getCase(case.x + 1,case.y)) != Dune) :
			casesPossibles.append(self.getCase(case.x + 1,case.y))
		return casesPossibles


	def __str__(self):
		s=""
		for x in range(self.width):
			for y in range(self.height):
				s += str(self.getCase(x,y)) +" | "
			s += "\n"
		return s



