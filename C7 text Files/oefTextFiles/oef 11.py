#Write a program that cancels the numbering of the previous exercise
with open("oef1b.py") as file:
    line = file.readline().rstrip()
    while line:
        code = line[2:]
        print(code)
        line = file.readline().rstrip()