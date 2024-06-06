def bmi(h,w):
    b = (w / (h * h)) * 703
    if b >= 18.5 and b <= 25:
        print("Your BMI is " + str(b))
        print("You are within the ideal weight range.")
    else:
        print("Midi Doktortan simon")

x = float(input("Please, enter your height: "))
y = float(input("Please, enter your weight: "))

print(bmi(x,y))