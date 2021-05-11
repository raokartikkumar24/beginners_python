__author__ = 'KRao4'
menu = {} #an empty dictionary
houses = { "lannister":111, "stark":234} #init with some key pair value


menu['lannister'] = 123 #key valye pair
menu['stark'] = 34

print(menu, len(menu))

# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

print(zoo_animals,len(zoo_animals))

animals = { "tiger","lion","cheetah","lepoard"}

animals.remove("tiger")

print(animals)


inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

inventory['pocket'] = ['seashell','strange berry','lint']

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')

inventory['gold'] = 550


