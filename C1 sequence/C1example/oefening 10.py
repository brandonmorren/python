consumption_day = int(input("power consumption during the day(kilowatt per hour): "))
consumption_night = int(input("power consumption during the night(kilowatt per hour): "))

print("invoice")
print("*" * 7)

fixed_cost = 83.6
consumption_day_price = 0.068 * consumption_day
consumption_night_price = 0.035 * consumption_night

total_exluding_vat = fixed_cost + consumption_night_price + consumption_day_price
total_including_vat = total_exluding_vat * 1.21

print("fixed costs: € " + str(fixed_cost))
print("daily consumption: € " + str(consumption_day_price))
print("night consumption: € " + str(consumption_night_price))
print("total exluding VAT: € " + str(total_exluding_vat))
print("total including VAT: € " + str(total_including_vat))