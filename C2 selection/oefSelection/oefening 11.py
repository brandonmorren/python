weight_in_kilogram = float(input("yout weight in kilograms: "))
length_in_centimeters = int(input("your length in centimeters: "))

bmi = (weight_in_kilogram/length_in_centimeters**2) * 10000
person_status = ""

if bmi < 18:
    person_status = "underweight"
elif 18 <= bmi < 25:
    person_status = "normal weight"
elif 25 <= bmi < 27:
    person_status = "slightly overweight"
elif 27 <= bmi < 30:
    person_status = "moderate overweight"
elif 30 <= bmi < 40:
    person_status = "obese"
elif 40 <= bmi:
    person_status = "sickly obese"

print("A person of " + str(weight_in_kilogram) + " kg with a length of " + str(length_in_centimeters) + " cm has as BMI " + str(bmi))
print("this is a " + person_status)