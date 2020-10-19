#animals = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
#new_animals = [animals[len(animals)-1], *animals[1:len(animals)-1], animals[0]]
#animals = new_animals

animals = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
print("original list:", "\t\t", animals)
first_element = animals[0]
animals[0] = animals[len(animals)-1]
animals[len(animals)-1] = first_element

print("after the switch:", "\t", animals)
#print(new_animals)