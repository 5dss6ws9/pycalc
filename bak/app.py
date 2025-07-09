import time

def add(x, y): # add
    return x + y

def subtract(x, y): # subtract
    return x - y

def multiply(x, y): # multiply
    return x * y

def divide(x, y): # divide
    if y == 0:
        return "no"
    else:
        return x / y

print("What do you want to do?") # ask
print("Add")
print("Subtract")
print("Multiply")
print("Divide")

while True:
    choice = input("(a, b, c, d)")

    if choice in ['a', 'b', 'c', 'd']:
        num1 = float(input("Enter x: "))
        num2 = float(input("Enter y: "))

        if choice == 'a': # choices, printing the answer
            print(f"{add(num1, num2)}")
        elif choice == 'b':
            print(f"{subtract(num1, num2)}")
        elif choice == 'c':
            print(f"{multiply(num1, num2)}")
        elif choice == 'r':
            print(f"{divide(num1, num2)}")
    else:
        print("python returned error: Invalid input")

    next_calculation = input("Again? (yes/no): ") # repeater
    if next_calculation.lower() != 'yes':
        print("done!")
        break