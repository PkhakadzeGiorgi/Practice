def whe(s,x):
    if "Wisc" in s:
        s = str(input("Where ? : "))
    elif "Illinois" in s:
        return ilPro(x)
    elif "Eau Claire" in s or "Dunn" in s:
        return pro(x)
    else: 
        return "Total Price : " + str(x) + "$"
        

def ilPro(x):
    p = (x * 8) / 100
    tax = "The Tax is :" + str(p) + "$"
    stx = "Total : " + str(x + p) + "$"
    return tax,stx

def pro(x):
    p = (x * 5) / 100
    tax = "The Tax is :" + str(p) + "$"
    stx = "Total : " + str(x + p) + "$"
    return tax,stx
        
a = int(input("What is the order amount? : "))
s = input("what state do you live in? : ")

print(whe(s,a))
print(pro(a))