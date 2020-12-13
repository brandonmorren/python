with open("./Files/books.txt", encoding="UTF-8") as file:
    book = file.readline()
    counter = 1
    while book:
        author = file.readline()
        print(str(counter) + ".", book.rstrip(), "-->", author.rstrip())
        counter += 1
        book = file.readline()