current_exchange_dollar = float(input("enter the current exchange dollar rate(€->$): "))
amount_in_euro = float(input("enter your amount in euro: "))
print(str(amount_in_euro) + "€ = " + str(current_exchange_dollar*amount_in_euro)+ "$")