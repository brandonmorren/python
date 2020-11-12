quote = "keep looking up"
quote_invisible = ""
for letter in quote:
    if letter != " ":
        quote_invisible += "#"
    else:
        quote_invisible += " "

print("you have to guess this quote:", quote_invisible)
letter_guess = input("guess a letter or press / if you think you know the quote: ")
while quote != quote_invisible:
    if letter_guess != "/" and letter_guess in quote:
        for i in range(0, len(quote)-1):
            if letter_guess == quote[i]:
                quote_invisible.replace(quote_invisible[i], letter_guess)

    else:
        letter_guess = input("OK. You think you know, just say it. ")
        if letter_guess == quote:
            quote_invisible = quote
    print("you already have this result:", quote_invisible)
    letter_guess = input("guess another letter: ")
print("yes you win")