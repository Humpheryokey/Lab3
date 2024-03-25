    # Humphery
    # Calculator to add two numbers and display the result
print(f"calculator")

sum = 0

while True:
    # 1. Input
    x1 = input ("Enter first number : ")
    x2 = input ("Enter first number : ")
    op = input ("Enter operator     : ")

    # 2. Process
    if op == "+":
        sum = int (x1) + int (x2)
    elif op == "-":
        sum = int (x1) - int (x2)
    elif op == "*":
        sum = int (x1) * int (x2)
    elif op == "/":
        sum = int (x1) / int (x2)
    
    #3. Output
    print (f"Sum                : {sum}")
    res = input("continue? (Yes/No) : ")
    if res == "No":
        print(f"Exit")
        break;