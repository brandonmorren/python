animals = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
print("original list:" "\t", animals)
animals.append(animals[0])
animals.remove(animals[0])
print("after sliding:" "\t", animals)
