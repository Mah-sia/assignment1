name = input ("Please enter your name: ")
Family = input ("Please enter your family: ")
g1 = float (input("Enter Grade1: "))
g2 = float (input("Enter Grade2: "))
g3 = float (input("Enter Grade3: "))
avr = (g1+g2+g3)/3
if avr >= 17:
    result = "You've done Great!!!"
if avr < 17 and avr >= 12:
    result = "Your Grades are Normal"
if avr < 12:
    result = "Oops!You are fail"
print(name, Family , result)


    
