s1 = int (input("Enter Side 1: "))
s2 = int (input("Enter Side 2: "))
s3 = int (input("Enter Side 3: "))
if s1+s2 > s3 and s2+s3 > s1 and s1+s3 > s2 :
    result = "These sides can be a triangle together:)"
else :
    result = "it's not possible to be a triangle"
print(result)