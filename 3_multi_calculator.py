# Humphery
# Calculator to add two numbers and display the result

# 1. Input
x1 = input ("Type x1: ")
x2 = input ("Type x2: ")
op = input (" Type operator:")

# 2. Process
if op == "+":
    sum = int (x1) + int (x2)
elif op == "-":
    sum = int (x1) - int (x2)
elif op == "*":
    sum = int (x1) * int (x2)


#3. Output

print (f"Sum: {sum}")