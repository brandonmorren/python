1 with open("./Files/first_names.txt") as file:
2     count = 0
3     line = file.readline()
4     while line:
5         count += 1
6         if line != "\n":
7             if line.count("z") >= 1 or line.count("Z") >= 1:
8                 print(line.rstrip())
9         line = file.readline()
10     print("There are", count, "first names in the file.")
