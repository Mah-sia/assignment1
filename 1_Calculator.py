import math
op = input (" please enter your operator: ")
if op== "+" or op== "-" or op== "*" or op== "/" :
    a = float(input("please enter 1st operand: "))
    b = float(input("please enter 2nd operand: "))
    

    if op == "+":
        result = a + b
    if op == "-":
        result = a - b
    if op == "*":
        result = a*b
    if op == "/" and b == 0 :
        result = "ERR"
    else:
        result = a / b

    print(result)
if op== "sin" or op== "cos" or op== "tan" or op== "cot" or op== "factorial" :
    a = float(input("please enter operand: "))
    if op == "sin":
        result = math.sin(math.radians(a))
    if op == "cos":
        result = math.cos(math.radians(a))
    if op == "tan":
        result = math.tan(math.radians(a))
    if op == "cot":
        result = 1/math.tan(math.radians(a))
    if op == "factorial":
        result = math.factorial(a)
else :
    result = "this operator is not in our calculate list!!"
print(result)



