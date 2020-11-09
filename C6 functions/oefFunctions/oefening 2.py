def exchange(current_dollar_rate, Euro):
    return current_dollar_rate * Euro


Current_dollar_rate2 = float(input("Current dollar rate (€ -> $): "))
Euro2 = float(input("Your amount in Euro: "))
print("€ " + str(Euro2) + " = $ " + str(exchange(Current_dollar_rate2, Euro2)))