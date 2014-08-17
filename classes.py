class Animal(object):
    
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
	def description(self):
		print self.name
        print self.age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)



    
hippo = Animal("hippo",24)

hippo.description()
print (zebra.name, zebra.age, zebra.is_alive)
print (giraffe.name, giraffe.age, giraffe.is_alive)
print (panda.name, panda.age, panda.is_alive)