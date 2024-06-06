def question(x):
    if "F" in x:
        print("your choice is F .")
        c = int(input("How Many F : "))
        c = (c - 32)* 5 / 9
        print("The temperature in C is :" + str(c) + "C")
    elif "C" in x:
        print("your choise is C")
        f = int(input("How Many C : "))
        f = (f * 9 / 5) + 32
        print("The temperature in F is :" + str(f) + "F")
        return 

    
print("Press C to convert from Fahrenheit to Celsius")
print("Press F to convert from Celsius to Fahrenheit")

y = str(input("Type : "))

print(question(y))