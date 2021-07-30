W = float (input("Your Weight(kg): "))
H = float (input("Your Height(Meter): "))
BMI = W/ (H*H)
if BMI < 18.5 :
    result = "underweight"
if BMI > 18.5 and BMI < 24.9:
    result = "Normal"
if BMI > 24.9 and  BMI < 29.9:
    result = "Overweight"
if BMI > 29.9 and  BMI < 34.9:
    result = "Obses"
if BMI > 34.9:
    result = "Over obses"
print(result)


