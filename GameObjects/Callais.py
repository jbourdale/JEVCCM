class Case :
	def __init__(self) : 
		pass
	def __eq__(self,case) :
		return self.x == case.x and self.y == case.y 

	def distance(self,case) : 
		return sqrt(pow(case.x - case.x,2) + pow(case.y - self.y,2))

class Frite (Case):
	def __init__(self) : 
		pass

class Moule (Case) : 
	def __init__(self,nbrDePoints) :
		self.nbrDePoints = nbrDePoints

class Player (Case) : 
	def __init__ (self,nomEquipe) : 
		self.nomEquipe = nomEquipe
	
	def setEquipe(self,nomEquipe): 
		self.nomEquipe = nomEquipe; 	

	def getEquipe(self): 
		return self.nomEquipe; 

class Sable (Case) : 
	def __init__(self) : 
		pass

class Dune (Case) : 
	def __init__(self):
		pass


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





