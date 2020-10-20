print("enter your name and the distance to school.")
print("type stop when you want to close the entry.")

list_name = []
list_distance = []

name = input("Your name: ")
while name != "stop":
    distance = float(input("distance to school: "))
    list_name.append(name)
    list_distance.append(distance)
    name = input("Your name: ")

for i in range(len(list_name)):
    print(list_name[i], "\t", list_distance[i])

average = sum(list_distance)/len(list_distance)
print(list_name[list_distance.index(max(list_distance))], "lives farthest, namely", max(list_distance), "km")
print("the average distance is", average)