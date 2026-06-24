def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Cannot divide by zero."
    else:
        return x / y

print("Select an operation [a/b/c/d]")
print("Letter corresponds to operation in order: addition, subtraction, multiplication, division")

while True:
    iask = input("(a, b, c, d)")
    if iask in ["a", "b", "c", "d"]:
        x = float(input("Enter x:"))
        y = float(input("Enter y:"))

        if iask == "a":
            print(f"{add(x, y)}")
        elif iask == "b":
            print(f"{subtract(x, y)}")
        elif iask == "c":
            print(f"{multiply(x, y)}")
        elif iask == "d":
            print(f"{divide(x, y)}")
    else:
        print("Invalid input.")
    
    nextcalc = input("Again? [y/n]")
    if nextcalc.lower() != "y":
        print("done!")
        break