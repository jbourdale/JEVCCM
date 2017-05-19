class Case :
	def __init__(self) : 
		pass

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



