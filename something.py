print("hello world")

class Animal(object):

	def __init__(self, weight, age, name):
		self.weight = weight
		self.age = age
		self.name = name
		self.children = dict()

	def addChild(self, child):
		self.children[child.name] = child

	def hasChild(self, name):
		return name in self.children

	def feedChild(self):
		for kid in self.children.values():
			kid.weight += .5
			print(kid.name, kid.weight)

	def numDescendants(self):
		num = len(self.children)
		for kid in self.children.values():
			num = num + kid.numDescendants()
		return num



class AquaticAnimal(Animal):
	"""docstring for ClassName"""
	def __init__(self, weight, age, name, floatiness,):
		super(AquaticAnimal, self).__init__(weight, age, name)
		self.floatiness = floatiness
	def speed(self):
		fastness = 100
		return fastness - self.age - (self.weight/10)

class LandAnimal(Animal):
	"""docstring for ClassName"""
	def __init__(self, weight,age,name):
		super(LandAnimal, self).__init__(weight, age, name)
	def speed(self):
		speed = 100
		return speed/(self.age*self.weight*0.5) 
	
# array zoo that has three aquatic and three land animals

angelfish = AquaticAnimal(5, 10, "Bubba", 0.4)
turtle = AquaticAnimal(7, 100, "Lady", 0.8)
shark = AquaticAnimal(250, 10, "JoJo", 0.7)
puppy = LandAnimal(15, 1, "Vinny")
bunny = LandAnimal(5, 3, "Bunnie")
human = LandAnimal(140, 26, "Kara")

zoo = [angelfish, turtle, shark, puppy, bunny, human]

for x in zoo:
	print(x.name)

print(angelfish.speed())
print(human.speed())
print(puppy.speed())
print(bunny.speed())
JoJoShark = AquaticAnimal(50,0.6,"JoJo Jr.",0.7)
BobTurtle = AquaticAnimal(7,0.6,"Bob",0.7)
JoanneShark = AquaticAnimal(60,0.6,"Joanne",0.7)
JoanneSharkJR = AquaticAnimal(35,0.6,"Joanne Jr.",0.7)
JonnyShark = AquaticAnimal(32,0.6,"Jonny",0.7)
JoelShark = AquaticAnimal(33,0.6,"Joel",0.7)
JamieShark = AquaticAnimal(34,0.6,"Jamie",0.7)


shark.addChild(JoJoShark) 
turtle.addChild(BobTurtle)
shark.addChild(JoanneShark)

print(shark.children['JoJo Jr.'].name)
print(shark.children['JoJo Jr.'].weight)
print(shark.children['JoJo Jr.'].speed())

shark.feedChild()
turtle.feedChild()

JoanneShark.addChild(JoanneSharkJR)
JoanneShark.addChild(JoelShark)
JoJoShark.addChild(JonnyShark)
JoJoShark.addChild(JamieShark)

print(shark.numDescendants())

		
